from LexListener import LexListener
from LexParser import LexParser


def find_offset(ctx):
    ctx_parent = ctx.parentCtx
    while ctx_parent is not None and not hasattr(ctx_parent, "offset"):
        ctx_parent = ctx_parent.parentCtx
    return ctx_parent.offset if ctx_parent is not None else ''


def is_declaration(ctx):
    ctx_parent = ctx.parentCtx
    while ctx_parent is not None and not hasattr(ctx_parent, "declaration"):
        ctx_parent = ctx_parent.parentCtx
    return ctx_parent.declaration if ctx_parent is not None else False


class CSharpListener(LexListener):
    def __init__(self, output):
        self.output = output
        self.mainPart = []
        self.declarationPart = []
        self.mainOffset = ''
        self.declarationOffset = ''

    def enterCode(self, ctx: LexParser.CodeContext):
        self.mainPart.extend([f"static void Main()", '{'])
        self.mainOffset = self.mainOffset + '\t'

    def exitCode(self, ctx: LexParser.CodeContext):
        self.mainPart.append('}')
        self.output.write("\n".join(self.declarationPart))
        self.output.write("\n".join(self.mainPart))
        self.output.close()

    def enterMainStatement(self, ctx: LexParser.MainStatementContext):
        ctx.offset = '\t'
        ctx.declaration = False

    def exitMainStatement(self, ctx: LexParser.MainStatementContext):
        child_ctx = ctx.getChild(0)
        if hasattr(child_ctx, "text"):
            text = child_ctx.text
            self.mainPart.append(text)

    def enterMainStatementNoNewLine(self, ctx: LexParser.MainStatementNoNewLineContext):
        ctx.offset = '\t'

    # def exitMainStatementNoNewLine(self, ctx: LexParser.MainStatementNoNewLineContext):
    #     child_ctx = ctx.getChild(0)
    #     if hasattr(child_ctx, "text"):
    #         text = child_ctx.text
    #         self.mainPart.append(text)


    def exitMethodHeader(self, ctx: LexParser.MethodHeaderContext):
        self.declarationPart.append(f"public void {ctx.methodName().getText()} ({ctx.methodHeaderVariables().text})")

    def exitMethodHeaderVariables(self, ctx: LexParser.MethodHeaderVariablesContext):
        if ctx.children:
            vars = [child.text for child in ctx.children]
            ctx.text = ", ".join(vars)
        else:
            ctx.text = ""
            
    def enterMethodHeaderVariable(self, ctx: LexParser.MethodHeaderVariableContext):
        ctx.text = f"{ctx.variableType().getText()} {ctx.variableName().getText()}"


    def enterMethodBody(self, ctx: LexParser.MethodBodyContext):
        self.declarationPart.append('{')
        ctx.offset = '\t'
        ctx.declaration = True

    def exitMethodBody(self, ctx: LexParser.MethodBodyContext):
        self.declarationPart.extend(['}', '\n'])
        

    def exitMethodStatement(self, ctx: LexParser.MethodStatementContext):
        child_ctx = ctx.getChild(0)
        if hasattr(child_ctx, "text"):
            text = child_ctx.text
            self.declarationPart.append(text)

    
    def exitForHead(self, ctx: LexParser.ForHeadContext):
        offset = find_offset(ctx)
        if is_declaration(ctx):
            add_to = self.declarationPart
        else:
            add_to = self.mainPart
        add_to.append(offset + f"for(int {ctx.VariableName().getText()} = 0; {ctx.VariableName().getText()} < {ctx.IntegerLiteral().getText()}; {ctx.VariableName().getText()}++)")

    def enterForBody(self, ctx: LexParser.ForBodyContext):
        if is_declaration(ctx):
            add_to = self.declarationPart
        else:
            add_to = self.mainPart
        offset = find_offset(ctx)
        add_to.append(offset + '{')
        ctx.offset = offset + '\t'

    def exitForBody(self, ctx: LexParser.ForBodyContext):
        if is_declaration(ctx):
            add_to = self.declarationPart
        else:
            add_to = self.mainPart
        offset = find_offset(ctx)
        add_to.append(offset + '}')


    def exitForStatement(self, ctx:LexParser.ForStatementContext):
        if is_declaration(ctx):
            add_to = self.declarationPart
        else:
            add_to = self.mainPart
        child_ctx = ctx.getChild(0)
        if hasattr(child_ctx, "text"):
            text = child_ctx.text
            add_to.append(text)

    
    def exitIfHead(self, ctx:LexParser.IfHeadContext):
        offset = find_offset(ctx)
        if is_declaration(ctx):
            add_to = self.declarationPart
        else:
            add_to = self.mainPart
        add_to.append(offset + f"if {ctx.condition().getText()}")

    def enterTruePart(self, ctx:LexParser.TruePartContext):
        if is_declaration(ctx):
            add_to = self.declarationPart
        else:
            add_to = self.mainPart
        offset = find_offset(ctx)
        add_to.append(offset + '{')
        ctx.offset = offset + '\t'

    def exitTruePart(self, ctx:LexParser.TruePartContext):
        if is_declaration(ctx):
            add_to = self.declarationPart
        else:
            add_to = self.mainPart
        offset = find_offset(ctx)
        add_to.append(offset + '}')

    def enterElsePart(self, ctx:LexParser.ElsePartContext):
        if is_declaration(ctx):
            add_to = self.declarationPart
        else:
            add_to = self.mainPart
        offset = find_offset(ctx)
        add_to.append(offset + 'else')
        add_to.append(offset + '{')
        ctx.offset = offset + '\t'

    def exitElsePart(self, ctx:LexParser.ElsePartContext):
        if is_declaration(ctx):
            add_to = self.declarationPart
        else:
            add_to = self.mainPart
        offset = find_offset(ctx)
        add_to.append(offset + '}')

    
    def exitIfStatement(self, ctx:LexParser.IfStatementContext):
        if is_declaration(ctx):
            add_to = self.declarationPart
        else:
            add_to = self.mainPart
        child_ctx = ctx.getChild(0)
        if hasattr(child_ctx, "text"):
            text = child_ctx.text
            add_to.append(text)


    def exitVariableDeclaration(self, ctx: LexParser.VariableDeclarationContext):
        # for child in ctx.children:
        #     print(child.getText())
        offset = find_offset(ctx)
        if hasattr(ctx.variableType(), "text"):
            varType = ctx.variableType().text
        else:
            varType = ctx.variableType().getText()

        if ctx.variableValue():
            ctx.text = offset + f"{varType} {ctx.variableName().getText()} = {ctx.variableValue().getText()};"
        else:
            ctx.text = offset + f"{varType} {ctx.variableName().getText()};"
    
    def enterVariableType(self, ctx: LexParser.VariableTypeContext):
        if ctx.getText() == "float":
            ctx.text = "double"
        elif ctx.getText() == "str":
            ctx.text = "string"
    
    def exitVariableInitialization(self, ctx: LexParser.VariableInitializationContext):
        offset = find_offset(ctx)
        ctx.text = offset + f"{ctx.variableName().getText()} = {ctx.variableValue().getText()};"

    def exitMethodCall(self, ctx: LexParser.MethodCallContext):
        offset = find_offset(ctx)
        ctx.text = offset + f"{ctx.methodName().getText()} ({ctx.methodHeaderVariables().text})"
