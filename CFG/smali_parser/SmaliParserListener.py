# Generated from SmaliParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SmaliParser import SmaliParser
else:
    from SmaliParser import SmaliParser

# This class defines a complete listener for a parse tree produced by SmaliParser.
class SmaliParserListener(ParseTreeListener):

    # Enter a parse tree produced by SmaliParser#registerIdentifier.
    def enterRegisterIdentifier(self, ctx:SmaliParser.RegisterIdentifierContext):
        pass

    # Exit a parse tree produced by SmaliParser#registerIdentifier.
    def exitRegisterIdentifier(self, ctx:SmaliParser.RegisterIdentifierContext):
        pass


    # Enter a parse tree produced by SmaliParser#stringLiteral.
    def enterStringLiteral(self, ctx:SmaliParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by SmaliParser#stringLiteral.
    def exitStringLiteral(self, ctx:SmaliParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by SmaliParser#negativeNumericLiteral.
    def enterNegativeNumericLiteral(self, ctx:SmaliParser.NegativeNumericLiteralContext):
        pass

    # Exit a parse tree produced by SmaliParser#negativeNumericLiteral.
    def exitNegativeNumericLiteral(self, ctx:SmaliParser.NegativeNumericLiteralContext):
        pass


    # Enter a parse tree produced by SmaliParser#decimalNumericLiteral.
    def enterDecimalNumericLiteral(self, ctx:SmaliParser.DecimalNumericLiteralContext):
        pass

    # Exit a parse tree produced by SmaliParser#decimalNumericLiteral.
    def exitDecimalNumericLiteral(self, ctx:SmaliParser.DecimalNumericLiteralContext):
        pass


    # Enter a parse tree produced by SmaliParser#hexNumericLiteral.
    def enterHexNumericLiteral(self, ctx:SmaliParser.HexNumericLiteralContext):
        pass

    # Exit a parse tree produced by SmaliParser#hexNumericLiteral.
    def exitHexNumericLiteral(self, ctx:SmaliParser.HexNumericLiteralContext):
        pass


    # Enter a parse tree produced by SmaliParser#octNumericLiteral.
    def enterOctNumericLiteral(self, ctx:SmaliParser.OctNumericLiteralContext):
        pass

    # Exit a parse tree produced by SmaliParser#octNumericLiteral.
    def exitOctNumericLiteral(self, ctx:SmaliParser.OctNumericLiteralContext):
        pass


    # Enter a parse tree produced by SmaliParser#binaryNumericLiteral.
    def enterBinaryNumericLiteral(self, ctx:SmaliParser.BinaryNumericLiteralContext):
        pass

    # Exit a parse tree produced by SmaliParser#binaryNumericLiteral.
    def exitBinaryNumericLiteral(self, ctx:SmaliParser.BinaryNumericLiteralContext):
        pass


    # Enter a parse tree produced by SmaliParser#floatNumericLiteral.
    def enterFloatNumericLiteral(self, ctx:SmaliParser.FloatNumericLiteralContext):
        pass

    # Exit a parse tree produced by SmaliParser#floatNumericLiteral.
    def exitFloatNumericLiteral(self, ctx:SmaliParser.FloatNumericLiteralContext):
        pass


    # Enter a parse tree produced by SmaliParser#hexFloatLiteral.
    def enterHexFloatLiteral(self, ctx:SmaliParser.HexFloatLiteralContext):
        pass

    # Exit a parse tree produced by SmaliParser#hexFloatLiteral.
    def exitHexFloatLiteral(self, ctx:SmaliParser.HexFloatLiteralContext):
        pass


    # Enter a parse tree produced by SmaliParser#positiveNumericLiteral.
    def enterPositiveNumericLiteral(self, ctx:SmaliParser.PositiveNumericLiteralContext):
        pass

    # Exit a parse tree produced by SmaliParser#positiveNumericLiteral.
    def exitPositiveNumericLiteral(self, ctx:SmaliParser.PositiveNumericLiteralContext):
        pass


    # Enter a parse tree produced by SmaliParser#numericLiteral.
    def enterNumericLiteral(self, ctx:SmaliParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by SmaliParser#numericLiteral.
    def exitNumericLiteral(self, ctx:SmaliParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by SmaliParser#identifier.
    def enterIdentifier(self, ctx:SmaliParser.IdentifierContext):
        pass

    # Exit a parse tree produced by SmaliParser#identifier.
    def exitIdentifier(self, ctx:SmaliParser.IdentifierContext):
        pass


    # Enter a parse tree produced by SmaliParser#referenceType.
    def enterReferenceType(self, ctx:SmaliParser.ReferenceTypeContext):
        pass

    # Exit a parse tree produced by SmaliParser#referenceType.
    def exitReferenceType(self, ctx:SmaliParser.ReferenceTypeContext):
        pass


    # Enter a parse tree produced by SmaliParser#voidType.
    def enterVoidType(self, ctx:SmaliParser.VoidTypeContext):
        pass

    # Exit a parse tree produced by SmaliParser#voidType.
    def exitVoidType(self, ctx:SmaliParser.VoidTypeContext):
        pass


    # Enter a parse tree produced by SmaliParser#booleanType.
    def enterBooleanType(self, ctx:SmaliParser.BooleanTypeContext):
        pass

    # Exit a parse tree produced by SmaliParser#booleanType.
    def exitBooleanType(self, ctx:SmaliParser.BooleanTypeContext):
        pass


    # Enter a parse tree produced by SmaliParser#byteType.
    def enterByteType(self, ctx:SmaliParser.ByteTypeContext):
        pass

    # Exit a parse tree produced by SmaliParser#byteType.
    def exitByteType(self, ctx:SmaliParser.ByteTypeContext):
        pass


    # Enter a parse tree produced by SmaliParser#shortType.
    def enterShortType(self, ctx:SmaliParser.ShortTypeContext):
        pass

    # Exit a parse tree produced by SmaliParser#shortType.
    def exitShortType(self, ctx:SmaliParser.ShortTypeContext):
        pass


    # Enter a parse tree produced by SmaliParser#charType.
    def enterCharType(self, ctx:SmaliParser.CharTypeContext):
        pass

    # Exit a parse tree produced by SmaliParser#charType.
    def exitCharType(self, ctx:SmaliParser.CharTypeContext):
        pass


    # Enter a parse tree produced by SmaliParser#intType.
    def enterIntType(self, ctx:SmaliParser.IntTypeContext):
        pass

    # Exit a parse tree produced by SmaliParser#intType.
    def exitIntType(self, ctx:SmaliParser.IntTypeContext):
        pass


    # Enter a parse tree produced by SmaliParser#longType.
    def enterLongType(self, ctx:SmaliParser.LongTypeContext):
        pass

    # Exit a parse tree produced by SmaliParser#longType.
    def exitLongType(self, ctx:SmaliParser.LongTypeContext):
        pass


    # Enter a parse tree produced by SmaliParser#floatType.
    def enterFloatType(self, ctx:SmaliParser.FloatTypeContext):
        pass

    # Exit a parse tree produced by SmaliParser#floatType.
    def exitFloatType(self, ctx:SmaliParser.FloatTypeContext):
        pass


    # Enter a parse tree produced by SmaliParser#doubleType.
    def enterDoubleType(self, ctx:SmaliParser.DoubleTypeContext):
        pass

    # Exit a parse tree produced by SmaliParser#doubleType.
    def exitDoubleType(self, ctx:SmaliParser.DoubleTypeContext):
        pass


    # Enter a parse tree produced by SmaliParser#primitiveType.
    def enterPrimitiveType(self, ctx:SmaliParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by SmaliParser#primitiveType.
    def exitPrimitiveType(self, ctx:SmaliParser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by SmaliParser#nonArrayType.
    def enterNonArrayType(self, ctx:SmaliParser.NonArrayTypeContext):
        pass

    # Exit a parse tree produced by SmaliParser#nonArrayType.
    def exitNonArrayType(self, ctx:SmaliParser.NonArrayTypeContext):
        pass


    # Enter a parse tree produced by SmaliParser#methodParameterLiteral.
    def enterMethodParameterLiteral(self, ctx:SmaliParser.MethodParameterLiteralContext):
        pass

    # Exit a parse tree produced by SmaliParser#methodParameterLiteral.
    def exitMethodParameterLiteral(self, ctx:SmaliParser.MethodParameterLiteralContext):
        pass


    # Enter a parse tree produced by SmaliParser#arrayType.
    def enterArrayType(self, ctx:SmaliParser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by SmaliParser#arrayType.
    def exitArrayType(self, ctx:SmaliParser.ArrayTypeContext):
        pass


    # Enter a parse tree produced by SmaliParser#referenceOrArrayType.
    def enterReferenceOrArrayType(self, ctx:SmaliParser.ReferenceOrArrayTypeContext):
        pass

    # Exit a parse tree produced by SmaliParser#referenceOrArrayType.
    def exitReferenceOrArrayType(self, ctx:SmaliParser.ReferenceOrArrayTypeContext):
        pass


    # Enter a parse tree produced by SmaliParser#nonVoidType.
    def enterNonVoidType(self, ctx:SmaliParser.NonVoidTypeContext):
        pass

    # Exit a parse tree produced by SmaliParser#nonVoidType.
    def exitNonVoidType(self, ctx:SmaliParser.NonVoidTypeContext):
        pass


    # Enter a parse tree produced by SmaliParser#anyType.
    def enterAnyType(self, ctx:SmaliParser.AnyTypeContext):
        pass

    # Exit a parse tree produced by SmaliParser#anyType.
    def exitAnyType(self, ctx:SmaliParser.AnyTypeContext):
        pass


    # Enter a parse tree produced by SmaliParser#nullLiteral.
    def enterNullLiteral(self, ctx:SmaliParser.NullLiteralContext):
        pass

    # Exit a parse tree produced by SmaliParser#nullLiteral.
    def exitNullLiteral(self, ctx:SmaliParser.NullLiteralContext):
        pass


    # Enter a parse tree produced by SmaliParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:SmaliParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by SmaliParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:SmaliParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by SmaliParser#assignableValue.
    def enterAssignableValue(self, ctx:SmaliParser.AssignableValueContext):
        pass

    # Exit a parse tree produced by SmaliParser#assignableValue.
    def exitAssignableValue(self, ctx:SmaliParser.AssignableValueContext):
        pass


    # Enter a parse tree produced by SmaliParser#classModifier.
    def enterClassModifier(self, ctx:SmaliParser.ClassModifierContext):
        pass

    # Exit a parse tree produced by SmaliParser#classModifier.
    def exitClassModifier(self, ctx:SmaliParser.ClassModifierContext):
        pass


    # Enter a parse tree produced by SmaliParser#methodModifier.
    def enterMethodModifier(self, ctx:SmaliParser.MethodModifierContext):
        pass

    # Exit a parse tree produced by SmaliParser#methodModifier.
    def exitMethodModifier(self, ctx:SmaliParser.MethodModifierContext):
        pass


    # Enter a parse tree produced by SmaliParser#fieldModifier.
    def enterFieldModifier(self, ctx:SmaliParser.FieldModifierContext):
        pass

    # Exit a parse tree produced by SmaliParser#fieldModifier.
    def exitFieldModifier(self, ctx:SmaliParser.FieldModifierContext):
        pass


    # Enter a parse tree produced by SmaliParser#labelName.
    def enterLabelName(self, ctx:SmaliParser.LabelNameContext):
        pass

    # Exit a parse tree produced by SmaliParser#labelName.
    def exitLabelName(self, ctx:SmaliParser.LabelNameContext):
        pass


    # Enter a parse tree produced by SmaliParser#label.
    def enterLabel(self, ctx:SmaliParser.LabelContext):
        pass

    # Exit a parse tree produced by SmaliParser#label.
    def exitLabel(self, ctx:SmaliParser.LabelContext):
        pass


    # Enter a parse tree produced by SmaliParser#leftRegister.
    def enterLeftRegister(self, ctx:SmaliParser.LeftRegisterContext):
        pass

    # Exit a parse tree produced by SmaliParser#leftRegister.
    def exitLeftRegister(self, ctx:SmaliParser.LeftRegisterContext):
        pass


    # Enter a parse tree produced by SmaliParser#rightRegister.
    def enterRightRegister(self, ctx:SmaliParser.RightRegisterContext):
        pass

    # Exit a parse tree produced by SmaliParser#rightRegister.
    def exitRightRegister(self, ctx:SmaliParser.RightRegisterContext):
        pass


    # Enter a parse tree produced by SmaliParser#registerListRegisters.
    def enterRegisterListRegisters(self, ctx:SmaliParser.RegisterListRegistersContext):
        pass

    # Exit a parse tree produced by SmaliParser#registerListRegisters.
    def exitRegisterListRegisters(self, ctx:SmaliParser.RegisterListRegistersContext):
        pass


    # Enter a parse tree produced by SmaliParser#registerRange.
    def enterRegisterRange(self, ctx:SmaliParser.RegisterRangeContext):
        pass

    # Exit a parse tree produced by SmaliParser#registerRange.
    def exitRegisterRange(self, ctx:SmaliParser.RegisterRangeContext):
        pass


    # Enter a parse tree produced by SmaliParser#registerList.
    def enterRegisterList(self, ctx:SmaliParser.RegisterListContext):
        pass

    # Exit a parse tree produced by SmaliParser#registerList.
    def exitRegisterList(self, ctx:SmaliParser.RegisterListContext):
        pass


    # Enter a parse tree produced by SmaliParser#gotoInstruction.
    def enterGotoInstruction(self, ctx:SmaliParser.GotoInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#gotoInstruction.
    def exitGotoInstruction(self, ctx:SmaliParser.GotoInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#goto16Instruction.
    def enterGoto16Instruction(self, ctx:SmaliParser.Goto16InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#goto16Instruction.
    def exitGoto16Instruction(self, ctx:SmaliParser.Goto16InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#goto32Instruction.
    def enterGoto32Instruction(self, ctx:SmaliParser.Goto32InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#goto32Instruction.
    def exitGoto32Instruction(self, ctx:SmaliParser.Goto32InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#moveResultInstruction.
    def enterMoveResultInstruction(self, ctx:SmaliParser.MoveResultInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#moveResultInstruction.
    def exitMoveResultInstruction(self, ctx:SmaliParser.MoveResultInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#moveResultWideInstruction.
    def enterMoveResultWideInstruction(self, ctx:SmaliParser.MoveResultWideInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#moveResultWideInstruction.
    def exitMoveResultWideInstruction(self, ctx:SmaliParser.MoveResultWideInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#moveResultObjectInstruction.
    def enterMoveResultObjectInstruction(self, ctx:SmaliParser.MoveResultObjectInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#moveResultObjectInstruction.
    def exitMoveResultObjectInstruction(self, ctx:SmaliParser.MoveResultObjectInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#moveExceptionInstruction.
    def enterMoveExceptionInstruction(self, ctx:SmaliParser.MoveExceptionInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#moveExceptionInstruction.
    def exitMoveExceptionInstruction(self, ctx:SmaliParser.MoveExceptionInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#returnInstruction.
    def enterReturnInstruction(self, ctx:SmaliParser.ReturnInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#returnInstruction.
    def exitReturnInstruction(self, ctx:SmaliParser.ReturnInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#returnWideInstruction.
    def enterReturnWideInstruction(self, ctx:SmaliParser.ReturnWideInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#returnWideInstruction.
    def exitReturnWideInstruction(self, ctx:SmaliParser.ReturnWideInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#returnObjectInstruction.
    def enterReturnObjectInstruction(self, ctx:SmaliParser.ReturnObjectInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#returnObjectInstruction.
    def exitReturnObjectInstruction(self, ctx:SmaliParser.ReturnObjectInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#monitorEnterInstruction.
    def enterMonitorEnterInstruction(self, ctx:SmaliParser.MonitorEnterInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#monitorEnterInstruction.
    def exitMonitorEnterInstruction(self, ctx:SmaliParser.MonitorEnterInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#monitorExitInstruction.
    def enterMonitorExitInstruction(self, ctx:SmaliParser.MonitorExitInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#monitorExitInstruction.
    def exitMonitorExitInstruction(self, ctx:SmaliParser.MonitorExitInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#throwInstruction.
    def enterThrowInstruction(self, ctx:SmaliParser.ThrowInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#throwInstruction.
    def exitThrowInstruction(self, ctx:SmaliParser.ThrowInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#returnVoidInstruction.
    def enterReturnVoidInstruction(self, ctx:SmaliParser.ReturnVoidInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#returnVoidInstruction.
    def exitReturnVoidInstruction(self, ctx:SmaliParser.ReturnVoidInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#nopInstruction.
    def enterNopInstruction(self, ctx:SmaliParser.NopInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#nopInstruction.
    def exitNopInstruction(self, ctx:SmaliParser.NopInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#moveInstruction.
    def enterMoveInstruction(self, ctx:SmaliParser.MoveInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#moveInstruction.
    def exitMoveInstruction(self, ctx:SmaliParser.MoveInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#moveFrom16Instruction.
    def enterMoveFrom16Instruction(self, ctx:SmaliParser.MoveFrom16InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#moveFrom16Instruction.
    def exitMoveFrom16Instruction(self, ctx:SmaliParser.MoveFrom16InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#move16Instruction.
    def enterMove16Instruction(self, ctx:SmaliParser.Move16InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#move16Instruction.
    def exitMove16Instruction(self, ctx:SmaliParser.Move16InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#moveWideInstruction.
    def enterMoveWideInstruction(self, ctx:SmaliParser.MoveWideInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#moveWideInstruction.
    def exitMoveWideInstruction(self, ctx:SmaliParser.MoveWideInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#moveWideFrom16Instruction.
    def enterMoveWideFrom16Instruction(self, ctx:SmaliParser.MoveWideFrom16InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#moveWideFrom16Instruction.
    def exitMoveWideFrom16Instruction(self, ctx:SmaliParser.MoveWideFrom16InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#moveWide16Instruction.
    def enterMoveWide16Instruction(self, ctx:SmaliParser.MoveWide16InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#moveWide16Instruction.
    def exitMoveWide16Instruction(self, ctx:SmaliParser.MoveWide16InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#moveObjectInstruction.
    def enterMoveObjectInstruction(self, ctx:SmaliParser.MoveObjectInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#moveObjectInstruction.
    def exitMoveObjectInstruction(self, ctx:SmaliParser.MoveObjectInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#moveObjectFrom16Instruction.
    def enterMoveObjectFrom16Instruction(self, ctx:SmaliParser.MoveObjectFrom16InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#moveObjectFrom16Instruction.
    def exitMoveObjectFrom16Instruction(self, ctx:SmaliParser.MoveObjectFrom16InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#moveObject16Instruction.
    def enterMoveObject16Instruction(self, ctx:SmaliParser.MoveObject16InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#moveObject16Instruction.
    def exitMoveObject16Instruction(self, ctx:SmaliParser.MoveObject16InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#constInstruction.
    def enterConstInstruction(self, ctx:SmaliParser.ConstInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#constInstruction.
    def exitConstInstruction(self, ctx:SmaliParser.ConstInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#const4Instruction.
    def enterConst4Instruction(self, ctx:SmaliParser.Const4InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#const4Instruction.
    def exitConst4Instruction(self, ctx:SmaliParser.Const4InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#const16Instruction.
    def enterConst16Instruction(self, ctx:SmaliParser.Const16InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#const16Instruction.
    def exitConst16Instruction(self, ctx:SmaliParser.Const16InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#constHigh16Instruction.
    def enterConstHigh16Instruction(self, ctx:SmaliParser.ConstHigh16InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#constHigh16Instruction.
    def exitConstHigh16Instruction(self, ctx:SmaliParser.ConstHigh16InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#constWide16Instruction.
    def enterConstWide16Instruction(self, ctx:SmaliParser.ConstWide16InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#constWide16Instruction.
    def exitConstWide16Instruction(self, ctx:SmaliParser.ConstWide16InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#constWide32Instruction.
    def enterConstWide32Instruction(self, ctx:SmaliParser.ConstWide32InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#constWide32Instruction.
    def exitConstWide32Instruction(self, ctx:SmaliParser.ConstWide32InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#constWideInstruction.
    def enterConstWideInstruction(self, ctx:SmaliParser.ConstWideInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#constWideInstruction.
    def exitConstWideInstruction(self, ctx:SmaliParser.ConstWideInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#constWideHigh16Instruction.
    def enterConstWideHigh16Instruction(self, ctx:SmaliParser.ConstWideHigh16InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#constWideHigh16Instruction.
    def exitConstWideHigh16Instruction(self, ctx:SmaliParser.ConstWideHigh16InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#constString.
    def enterConstString(self, ctx:SmaliParser.ConstStringContext):
        pass

    # Exit a parse tree produced by SmaliParser#constString.
    def exitConstString(self, ctx:SmaliParser.ConstStringContext):
        pass


    # Enter a parse tree produced by SmaliParser#constStringJumbo.
    def enterConstStringJumbo(self, ctx:SmaliParser.ConstStringJumboContext):
        pass

    # Exit a parse tree produced by SmaliParser#constStringJumbo.
    def exitConstStringJumbo(self, ctx:SmaliParser.ConstStringJumboContext):
        pass


    # Enter a parse tree produced by SmaliParser#constClass.
    def enterConstClass(self, ctx:SmaliParser.ConstClassContext):
        pass

    # Exit a parse tree produced by SmaliParser#constClass.
    def exitConstClass(self, ctx:SmaliParser.ConstClassContext):
        pass


    # Enter a parse tree produced by SmaliParser#sGetInstruction.
    def enterSGetInstruction(self, ctx:SmaliParser.SGetInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#sGetInstruction.
    def exitSGetInstruction(self, ctx:SmaliParser.SGetInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#sGetWideInstruction.
    def enterSGetWideInstruction(self, ctx:SmaliParser.SGetWideInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#sGetWideInstruction.
    def exitSGetWideInstruction(self, ctx:SmaliParser.SGetWideInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#sGetObjectInstruction.
    def enterSGetObjectInstruction(self, ctx:SmaliParser.SGetObjectInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#sGetObjectInstruction.
    def exitSGetObjectInstruction(self, ctx:SmaliParser.SGetObjectInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#sGetBooleanInstruction.
    def enterSGetBooleanInstruction(self, ctx:SmaliParser.SGetBooleanInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#sGetBooleanInstruction.
    def exitSGetBooleanInstruction(self, ctx:SmaliParser.SGetBooleanInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#sGetByteInstruction.
    def enterSGetByteInstruction(self, ctx:SmaliParser.SGetByteInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#sGetByteInstruction.
    def exitSGetByteInstruction(self, ctx:SmaliParser.SGetByteInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#sGetCharInstruction.
    def enterSGetCharInstruction(self, ctx:SmaliParser.SGetCharInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#sGetCharInstruction.
    def exitSGetCharInstruction(self, ctx:SmaliParser.SGetCharInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#sGetShortInstruction.
    def enterSGetShortInstruction(self, ctx:SmaliParser.SGetShortInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#sGetShortInstruction.
    def exitSGetShortInstruction(self, ctx:SmaliParser.SGetShortInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#sPutInstruction.
    def enterSPutInstruction(self, ctx:SmaliParser.SPutInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#sPutInstruction.
    def exitSPutInstruction(self, ctx:SmaliParser.SPutInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#sPutWideInstruction.
    def enterSPutWideInstruction(self, ctx:SmaliParser.SPutWideInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#sPutWideInstruction.
    def exitSPutWideInstruction(self, ctx:SmaliParser.SPutWideInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#sPutObjectInstruction.
    def enterSPutObjectInstruction(self, ctx:SmaliParser.SPutObjectInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#sPutObjectInstruction.
    def exitSPutObjectInstruction(self, ctx:SmaliParser.SPutObjectInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#sPutBooleanInstruction.
    def enterSPutBooleanInstruction(self, ctx:SmaliParser.SPutBooleanInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#sPutBooleanInstruction.
    def exitSPutBooleanInstruction(self, ctx:SmaliParser.SPutBooleanInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#sPutByteInstruction.
    def enterSPutByteInstruction(self, ctx:SmaliParser.SPutByteInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#sPutByteInstruction.
    def exitSPutByteInstruction(self, ctx:SmaliParser.SPutByteInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#sPutCharInstruction.
    def enterSPutCharInstruction(self, ctx:SmaliParser.SPutCharInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#sPutCharInstruction.
    def exitSPutCharInstruction(self, ctx:SmaliParser.SPutCharInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#sPutShortInstruction.
    def enterSPutShortInstruction(self, ctx:SmaliParser.SPutShortInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#sPutShortInstruction.
    def exitSPutShortInstruction(self, ctx:SmaliParser.SPutShortInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#invokeVirtualInstruction.
    def enterInvokeVirtualInstruction(self, ctx:SmaliParser.InvokeVirtualInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#invokeVirtualInstruction.
    def exitInvokeVirtualInstruction(self, ctx:SmaliParser.InvokeVirtualInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#invokeSuperInstruction.
    def enterInvokeSuperInstruction(self, ctx:SmaliParser.InvokeSuperInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#invokeSuperInstruction.
    def exitInvokeSuperInstruction(self, ctx:SmaliParser.InvokeSuperInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#invokeDirectInstruction.
    def enterInvokeDirectInstruction(self, ctx:SmaliParser.InvokeDirectInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#invokeDirectInstruction.
    def exitInvokeDirectInstruction(self, ctx:SmaliParser.InvokeDirectInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#invokeStaticInstruction.
    def enterInvokeStaticInstruction(self, ctx:SmaliParser.InvokeStaticInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#invokeStaticInstruction.
    def exitInvokeStaticInstruction(self, ctx:SmaliParser.InvokeStaticInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#invokeInterfaceInstruction.
    def enterInvokeInterfaceInstruction(self, ctx:SmaliParser.InvokeInterfaceInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#invokeInterfaceInstruction.
    def exitInvokeInterfaceInstruction(self, ctx:SmaliParser.InvokeInterfaceInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#invokeVirtualRangeInstruction.
    def enterInvokeVirtualRangeInstruction(self, ctx:SmaliParser.InvokeVirtualRangeInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#invokeVirtualRangeInstruction.
    def exitInvokeVirtualRangeInstruction(self, ctx:SmaliParser.InvokeVirtualRangeInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#invokeSuperRangeInstruction.
    def enterInvokeSuperRangeInstruction(self, ctx:SmaliParser.InvokeSuperRangeInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#invokeSuperRangeInstruction.
    def exitInvokeSuperRangeInstruction(self, ctx:SmaliParser.InvokeSuperRangeInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#invokeDirectRangeInstruction.
    def enterInvokeDirectRangeInstruction(self, ctx:SmaliParser.InvokeDirectRangeInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#invokeDirectRangeInstruction.
    def exitInvokeDirectRangeInstruction(self, ctx:SmaliParser.InvokeDirectRangeInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#invokeStaticRangeInstruction.
    def enterInvokeStaticRangeInstruction(self, ctx:SmaliParser.InvokeStaticRangeInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#invokeStaticRangeInstruction.
    def exitInvokeStaticRangeInstruction(self, ctx:SmaliParser.InvokeStaticRangeInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#invokeInterfaceRangeInstruction.
    def enterInvokeInterfaceRangeInstruction(self, ctx:SmaliParser.InvokeInterfaceRangeInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#invokeInterfaceRangeInstruction.
    def exitInvokeInterfaceRangeInstruction(self, ctx:SmaliParser.InvokeInterfaceRangeInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#intToLongInstruction.
    def enterIntToLongInstruction(self, ctx:SmaliParser.IntToLongInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#intToLongInstruction.
    def exitIntToLongInstruction(self, ctx:SmaliParser.IntToLongInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#intToFloatInstruction.
    def enterIntToFloatInstruction(self, ctx:SmaliParser.IntToFloatInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#intToFloatInstruction.
    def exitIntToFloatInstruction(self, ctx:SmaliParser.IntToFloatInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#intToDoubleInstruction.
    def enterIntToDoubleInstruction(self, ctx:SmaliParser.IntToDoubleInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#intToDoubleInstruction.
    def exitIntToDoubleInstruction(self, ctx:SmaliParser.IntToDoubleInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#longToIntInstruction.
    def enterLongToIntInstruction(self, ctx:SmaliParser.LongToIntInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#longToIntInstruction.
    def exitLongToIntInstruction(self, ctx:SmaliParser.LongToIntInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#longToFloatInstruction.
    def enterLongToFloatInstruction(self, ctx:SmaliParser.LongToFloatInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#longToFloatInstruction.
    def exitLongToFloatInstruction(self, ctx:SmaliParser.LongToFloatInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#longToDoubleInstruction.
    def enterLongToDoubleInstruction(self, ctx:SmaliParser.LongToDoubleInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#longToDoubleInstruction.
    def exitLongToDoubleInstruction(self, ctx:SmaliParser.LongToDoubleInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#floatToIntInstruction.
    def enterFloatToIntInstruction(self, ctx:SmaliParser.FloatToIntInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#floatToIntInstruction.
    def exitFloatToIntInstruction(self, ctx:SmaliParser.FloatToIntInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#floatToLongInstruction.
    def enterFloatToLongInstruction(self, ctx:SmaliParser.FloatToLongInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#floatToLongInstruction.
    def exitFloatToLongInstruction(self, ctx:SmaliParser.FloatToLongInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#floatToDoubleInstruction.
    def enterFloatToDoubleInstruction(self, ctx:SmaliParser.FloatToDoubleInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#floatToDoubleInstruction.
    def exitFloatToDoubleInstruction(self, ctx:SmaliParser.FloatToDoubleInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#doubleToIntInstruction.
    def enterDoubleToIntInstruction(self, ctx:SmaliParser.DoubleToIntInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#doubleToIntInstruction.
    def exitDoubleToIntInstruction(self, ctx:SmaliParser.DoubleToIntInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#doubleToLongInstruction.
    def enterDoubleToLongInstruction(self, ctx:SmaliParser.DoubleToLongInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#doubleToLongInstruction.
    def exitDoubleToLongInstruction(self, ctx:SmaliParser.DoubleToLongInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#doubleToFloatInstruction.
    def enterDoubleToFloatInstruction(self, ctx:SmaliParser.DoubleToFloatInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#doubleToFloatInstruction.
    def exitDoubleToFloatInstruction(self, ctx:SmaliParser.DoubleToFloatInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#intToByteInstruction.
    def enterIntToByteInstruction(self, ctx:SmaliParser.IntToByteInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#intToByteInstruction.
    def exitIntToByteInstruction(self, ctx:SmaliParser.IntToByteInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#intToCharInstruction.
    def enterIntToCharInstruction(self, ctx:SmaliParser.IntToCharInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#intToCharInstruction.
    def exitIntToCharInstruction(self, ctx:SmaliParser.IntToCharInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#intToShortInstruction.
    def enterIntToShortInstruction(self, ctx:SmaliParser.IntToShortInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#intToShortInstruction.
    def exitIntToShortInstruction(self, ctx:SmaliParser.IntToShortInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#ifLabel.
    def enterIfLabel(self, ctx:SmaliParser.IfLabelContext):
        pass

    # Exit a parse tree produced by SmaliParser#ifLabel.
    def exitIfLabel(self, ctx:SmaliParser.IfLabelContext):
        pass


    # Enter a parse tree produced by SmaliParser#ifEqzInstruction.
    def enterIfEqzInstruction(self, ctx:SmaliParser.IfEqzInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#ifEqzInstruction.
    def exitIfEqzInstruction(self, ctx:SmaliParser.IfEqzInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#ifNezInstruction.
    def enterIfNezInstruction(self, ctx:SmaliParser.IfNezInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#ifNezInstruction.
    def exitIfNezInstruction(self, ctx:SmaliParser.IfNezInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#ifLtzInstruction.
    def enterIfLtzInstruction(self, ctx:SmaliParser.IfLtzInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#ifLtzInstruction.
    def exitIfLtzInstruction(self, ctx:SmaliParser.IfLtzInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#ifGezInstruction.
    def enterIfGezInstruction(self, ctx:SmaliParser.IfGezInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#ifGezInstruction.
    def exitIfGezInstruction(self, ctx:SmaliParser.IfGezInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#ifGtzInstruction.
    def enterIfGtzInstruction(self, ctx:SmaliParser.IfGtzInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#ifGtzInstruction.
    def exitIfGtzInstruction(self, ctx:SmaliParser.IfGtzInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#ifLezInstruction.
    def enterIfLezInstruction(self, ctx:SmaliParser.IfLezInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#ifLezInstruction.
    def exitIfLezInstruction(self, ctx:SmaliParser.IfLezInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#negIntInstruction.
    def enterNegIntInstruction(self, ctx:SmaliParser.NegIntInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#negIntInstruction.
    def exitNegIntInstruction(self, ctx:SmaliParser.NegIntInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#notIntInstruction.
    def enterNotIntInstruction(self, ctx:SmaliParser.NotIntInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#notIntInstruction.
    def exitNotIntInstruction(self, ctx:SmaliParser.NotIntInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#negLongInstruction.
    def enterNegLongInstruction(self, ctx:SmaliParser.NegLongInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#negLongInstruction.
    def exitNegLongInstruction(self, ctx:SmaliParser.NegLongInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#notLongInstruction.
    def enterNotLongInstruction(self, ctx:SmaliParser.NotLongInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#notLongInstruction.
    def exitNotLongInstruction(self, ctx:SmaliParser.NotLongInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#negFloatInstruction.
    def enterNegFloatInstruction(self, ctx:SmaliParser.NegFloatInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#negFloatInstruction.
    def exitNegFloatInstruction(self, ctx:SmaliParser.NegFloatInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#negDoubleInstruction.
    def enterNegDoubleInstruction(self, ctx:SmaliParser.NegDoubleInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#negDoubleInstruction.
    def exitNegDoubleInstruction(self, ctx:SmaliParser.NegDoubleInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#ifEqInstruction.
    def enterIfEqInstruction(self, ctx:SmaliParser.IfEqInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#ifEqInstruction.
    def exitIfEqInstruction(self, ctx:SmaliParser.IfEqInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#ifNeInstruction.
    def enterIfNeInstruction(self, ctx:SmaliParser.IfNeInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#ifNeInstruction.
    def exitIfNeInstruction(self, ctx:SmaliParser.IfNeInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#ifLtInstruction.
    def enterIfLtInstruction(self, ctx:SmaliParser.IfLtInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#ifLtInstruction.
    def exitIfLtInstruction(self, ctx:SmaliParser.IfLtInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#ifGeInstruction.
    def enterIfGeInstruction(self, ctx:SmaliParser.IfGeInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#ifGeInstruction.
    def exitIfGeInstruction(self, ctx:SmaliParser.IfGeInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#ifGtInstruction.
    def enterIfGtInstruction(self, ctx:SmaliParser.IfGtInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#ifGtInstruction.
    def exitIfGtInstruction(self, ctx:SmaliParser.IfGtInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#ifLeInstruction.
    def enterIfLeInstruction(self, ctx:SmaliParser.IfLeInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#ifLeInstruction.
    def exitIfLeInstruction(self, ctx:SmaliParser.IfLeInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#addInt2addrInstruction.
    def enterAddInt2addrInstruction(self, ctx:SmaliParser.AddInt2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#addInt2addrInstruction.
    def exitAddInt2addrInstruction(self, ctx:SmaliParser.AddInt2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#subInt2addrInstruction.
    def enterSubInt2addrInstruction(self, ctx:SmaliParser.SubInt2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#subInt2addrInstruction.
    def exitSubInt2addrInstruction(self, ctx:SmaliParser.SubInt2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#mulInt2addrInstruction.
    def enterMulInt2addrInstruction(self, ctx:SmaliParser.MulInt2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#mulInt2addrInstruction.
    def exitMulInt2addrInstruction(self, ctx:SmaliParser.MulInt2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#divInt2addrInstruction.
    def enterDivInt2addrInstruction(self, ctx:SmaliParser.DivInt2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#divInt2addrInstruction.
    def exitDivInt2addrInstruction(self, ctx:SmaliParser.DivInt2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#remInt2addrInstruction.
    def enterRemInt2addrInstruction(self, ctx:SmaliParser.RemInt2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#remInt2addrInstruction.
    def exitRemInt2addrInstruction(self, ctx:SmaliParser.RemInt2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#andInt2addrInstruction.
    def enterAndInt2addrInstruction(self, ctx:SmaliParser.AndInt2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#andInt2addrInstruction.
    def exitAndInt2addrInstruction(self, ctx:SmaliParser.AndInt2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#orInt2addrInstruction.
    def enterOrInt2addrInstruction(self, ctx:SmaliParser.OrInt2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#orInt2addrInstruction.
    def exitOrInt2addrInstruction(self, ctx:SmaliParser.OrInt2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#xorInt2addrInstruction.
    def enterXorInt2addrInstruction(self, ctx:SmaliParser.XorInt2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#xorInt2addrInstruction.
    def exitXorInt2addrInstruction(self, ctx:SmaliParser.XorInt2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#shlInt2addrInstruction.
    def enterShlInt2addrInstruction(self, ctx:SmaliParser.ShlInt2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#shlInt2addrInstruction.
    def exitShlInt2addrInstruction(self, ctx:SmaliParser.ShlInt2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#shrInt2addrInstruction.
    def enterShrInt2addrInstruction(self, ctx:SmaliParser.ShrInt2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#shrInt2addrInstruction.
    def exitShrInt2addrInstruction(self, ctx:SmaliParser.ShrInt2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#ushrInt2addrInstruction.
    def enterUshrInt2addrInstruction(self, ctx:SmaliParser.UshrInt2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#ushrInt2addrInstruction.
    def exitUshrInt2addrInstruction(self, ctx:SmaliParser.UshrInt2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#addLong2addrInstruction.
    def enterAddLong2addrInstruction(self, ctx:SmaliParser.AddLong2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#addLong2addrInstruction.
    def exitAddLong2addrInstruction(self, ctx:SmaliParser.AddLong2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#subLong2addrInstruction.
    def enterSubLong2addrInstruction(self, ctx:SmaliParser.SubLong2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#subLong2addrInstruction.
    def exitSubLong2addrInstruction(self, ctx:SmaliParser.SubLong2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#mulLong2addrInstruction.
    def enterMulLong2addrInstruction(self, ctx:SmaliParser.MulLong2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#mulLong2addrInstruction.
    def exitMulLong2addrInstruction(self, ctx:SmaliParser.MulLong2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#divLong2addrInstruction.
    def enterDivLong2addrInstruction(self, ctx:SmaliParser.DivLong2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#divLong2addrInstruction.
    def exitDivLong2addrInstruction(self, ctx:SmaliParser.DivLong2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#remLong2addrInstruction.
    def enterRemLong2addrInstruction(self, ctx:SmaliParser.RemLong2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#remLong2addrInstruction.
    def exitRemLong2addrInstruction(self, ctx:SmaliParser.RemLong2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#andLong2addrInstruction.
    def enterAndLong2addrInstruction(self, ctx:SmaliParser.AndLong2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#andLong2addrInstruction.
    def exitAndLong2addrInstruction(self, ctx:SmaliParser.AndLong2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#orLong2addrInstruction.
    def enterOrLong2addrInstruction(self, ctx:SmaliParser.OrLong2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#orLong2addrInstruction.
    def exitOrLong2addrInstruction(self, ctx:SmaliParser.OrLong2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#xorLong2addrInstruction.
    def enterXorLong2addrInstruction(self, ctx:SmaliParser.XorLong2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#xorLong2addrInstruction.
    def exitXorLong2addrInstruction(self, ctx:SmaliParser.XorLong2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#shlLong2addrInstruction.
    def enterShlLong2addrInstruction(self, ctx:SmaliParser.ShlLong2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#shlLong2addrInstruction.
    def exitShlLong2addrInstruction(self, ctx:SmaliParser.ShlLong2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#shrLong2addrInstruction.
    def enterShrLong2addrInstruction(self, ctx:SmaliParser.ShrLong2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#shrLong2addrInstruction.
    def exitShrLong2addrInstruction(self, ctx:SmaliParser.ShrLong2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#ushrLong2addrInstruction.
    def enterUshrLong2addrInstruction(self, ctx:SmaliParser.UshrLong2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#ushrLong2addrInstruction.
    def exitUshrLong2addrInstruction(self, ctx:SmaliParser.UshrLong2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#addFloat2addrInstruction.
    def enterAddFloat2addrInstruction(self, ctx:SmaliParser.AddFloat2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#addFloat2addrInstruction.
    def exitAddFloat2addrInstruction(self, ctx:SmaliParser.AddFloat2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#subFloat2addrInstruction.
    def enterSubFloat2addrInstruction(self, ctx:SmaliParser.SubFloat2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#subFloat2addrInstruction.
    def exitSubFloat2addrInstruction(self, ctx:SmaliParser.SubFloat2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#mulFloat2addrInstruction.
    def enterMulFloat2addrInstruction(self, ctx:SmaliParser.MulFloat2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#mulFloat2addrInstruction.
    def exitMulFloat2addrInstruction(self, ctx:SmaliParser.MulFloat2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#divFloat2addrInstruction.
    def enterDivFloat2addrInstruction(self, ctx:SmaliParser.DivFloat2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#divFloat2addrInstruction.
    def exitDivFloat2addrInstruction(self, ctx:SmaliParser.DivFloat2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#remFloat2addrInstruction.
    def enterRemFloat2addrInstruction(self, ctx:SmaliParser.RemFloat2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#remFloat2addrInstruction.
    def exitRemFloat2addrInstruction(self, ctx:SmaliParser.RemFloat2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#addDouble2addrInstruction.
    def enterAddDouble2addrInstruction(self, ctx:SmaliParser.AddDouble2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#addDouble2addrInstruction.
    def exitAddDouble2addrInstruction(self, ctx:SmaliParser.AddDouble2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#subDouble2addrInstruction.
    def enterSubDouble2addrInstruction(self, ctx:SmaliParser.SubDouble2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#subDouble2addrInstruction.
    def exitSubDouble2addrInstruction(self, ctx:SmaliParser.SubDouble2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#mulDouble2addrInstruction.
    def enterMulDouble2addrInstruction(self, ctx:SmaliParser.MulDouble2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#mulDouble2addrInstruction.
    def exitMulDouble2addrInstruction(self, ctx:SmaliParser.MulDouble2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#divDouble2addrInstruction.
    def enterDivDouble2addrInstruction(self, ctx:SmaliParser.DivDouble2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#divDouble2addrInstruction.
    def exitDivDouble2addrInstruction(self, ctx:SmaliParser.DivDouble2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#remDouble2addrInstruction.
    def enterRemDouble2addrInstruction(self, ctx:SmaliParser.RemDouble2addrInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#remDouble2addrInstruction.
    def exitRemDouble2addrInstruction(self, ctx:SmaliParser.RemDouble2addrInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#cmplFloatInstruction.
    def enterCmplFloatInstruction(self, ctx:SmaliParser.CmplFloatInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#cmplFloatInstruction.
    def exitCmplFloatInstruction(self, ctx:SmaliParser.CmplFloatInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#cmpgFloatInstruction.
    def enterCmpgFloatInstruction(self, ctx:SmaliParser.CmpgFloatInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#cmpgFloatInstruction.
    def exitCmpgFloatInstruction(self, ctx:SmaliParser.CmpgFloatInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#cmplDoubleInstruction.
    def enterCmplDoubleInstruction(self, ctx:SmaliParser.CmplDoubleInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#cmplDoubleInstruction.
    def exitCmplDoubleInstruction(self, ctx:SmaliParser.CmplDoubleInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#cmpgDoubleInstruction.
    def enterCmpgDoubleInstruction(self, ctx:SmaliParser.CmpgDoubleInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#cmpgDoubleInstruction.
    def exitCmpgDoubleInstruction(self, ctx:SmaliParser.CmpgDoubleInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#cmpLongInstruction.
    def enterCmpLongInstruction(self, ctx:SmaliParser.CmpLongInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#cmpLongInstruction.
    def exitCmpLongInstruction(self, ctx:SmaliParser.CmpLongInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#field.
    def enterField(self, ctx:SmaliParser.FieldContext):
        pass

    # Exit a parse tree produced by SmaliParser#field.
    def exitField(self, ctx:SmaliParser.FieldContext):
        pass


    # Enter a parse tree produced by SmaliParser#arrayRegister.
    def enterArrayRegister(self, ctx:SmaliParser.ArrayRegisterContext):
        pass

    # Exit a parse tree produced by SmaliParser#arrayRegister.
    def exitArrayRegister(self, ctx:SmaliParser.ArrayRegisterContext):
        pass


    # Enter a parse tree produced by SmaliParser#indexRegister.
    def enterIndexRegister(self, ctx:SmaliParser.IndexRegisterContext):
        pass

    # Exit a parse tree produced by SmaliParser#indexRegister.
    def exitIndexRegister(self, ctx:SmaliParser.IndexRegisterContext):
        pass


    # Enter a parse tree produced by SmaliParser#instanceRegister.
    def enterInstanceRegister(self, ctx:SmaliParser.InstanceRegisterContext):
        pass

    # Exit a parse tree produced by SmaliParser#instanceRegister.
    def exitInstanceRegister(self, ctx:SmaliParser.InstanceRegisterContext):
        pass


    # Enter a parse tree produced by SmaliParser#sourceRegister.
    def enterSourceRegister(self, ctx:SmaliParser.SourceRegisterContext):
        pass

    # Exit a parse tree produced by SmaliParser#sourceRegister.
    def exitSourceRegister(self, ctx:SmaliParser.SourceRegisterContext):
        pass


    # Enter a parse tree produced by SmaliParser#targetRegister.
    def enterTargetRegister(self, ctx:SmaliParser.TargetRegisterContext):
        pass

    # Exit a parse tree produced by SmaliParser#targetRegister.
    def exitTargetRegister(self, ctx:SmaliParser.TargetRegisterContext):
        pass


    # Enter a parse tree produced by SmaliParser#instanceField.
    def enterInstanceField(self, ctx:SmaliParser.InstanceFieldContext):
        pass

    # Exit a parse tree produced by SmaliParser#instanceField.
    def exitInstanceField(self, ctx:SmaliParser.InstanceFieldContext):
        pass


    # Enter a parse tree produced by SmaliParser#agetInstruction.
    def enterAgetInstruction(self, ctx:SmaliParser.AgetInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#agetInstruction.
    def exitAgetInstruction(self, ctx:SmaliParser.AgetInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#agetWideInstruction.
    def enterAgetWideInstruction(self, ctx:SmaliParser.AgetWideInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#agetWideInstruction.
    def exitAgetWideInstruction(self, ctx:SmaliParser.AgetWideInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#agetObjectInstruction.
    def enterAgetObjectInstruction(self, ctx:SmaliParser.AgetObjectInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#agetObjectInstruction.
    def exitAgetObjectInstruction(self, ctx:SmaliParser.AgetObjectInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#agetBooleanInstruction.
    def enterAgetBooleanInstruction(self, ctx:SmaliParser.AgetBooleanInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#agetBooleanInstruction.
    def exitAgetBooleanInstruction(self, ctx:SmaliParser.AgetBooleanInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#agetByteInstruction.
    def enterAgetByteInstruction(self, ctx:SmaliParser.AgetByteInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#agetByteInstruction.
    def exitAgetByteInstruction(self, ctx:SmaliParser.AgetByteInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#agetCharInstruction.
    def enterAgetCharInstruction(self, ctx:SmaliParser.AgetCharInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#agetCharInstruction.
    def exitAgetCharInstruction(self, ctx:SmaliParser.AgetCharInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#agetShortInstruction.
    def enterAgetShortInstruction(self, ctx:SmaliParser.AgetShortInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#agetShortInstruction.
    def exitAgetShortInstruction(self, ctx:SmaliParser.AgetShortInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#aputInstruction.
    def enterAputInstruction(self, ctx:SmaliParser.AputInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#aputInstruction.
    def exitAputInstruction(self, ctx:SmaliParser.AputInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#aputWideInstruction.
    def enterAputWideInstruction(self, ctx:SmaliParser.AputWideInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#aputWideInstruction.
    def exitAputWideInstruction(self, ctx:SmaliParser.AputWideInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#aputObjectInstruction.
    def enterAputObjectInstruction(self, ctx:SmaliParser.AputObjectInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#aputObjectInstruction.
    def exitAputObjectInstruction(self, ctx:SmaliParser.AputObjectInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#aputBooleanInstruction.
    def enterAputBooleanInstruction(self, ctx:SmaliParser.AputBooleanInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#aputBooleanInstruction.
    def exitAputBooleanInstruction(self, ctx:SmaliParser.AputBooleanInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#aputByteInstruction.
    def enterAputByteInstruction(self, ctx:SmaliParser.AputByteInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#aputByteInstruction.
    def exitAputByteInstruction(self, ctx:SmaliParser.AputByteInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#aputCharInstruction.
    def enterAputCharInstruction(self, ctx:SmaliParser.AputCharInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#aputCharInstruction.
    def exitAputCharInstruction(self, ctx:SmaliParser.AputCharInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#aputShortInstruction.
    def enterAputShortInstruction(self, ctx:SmaliParser.AputShortInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#aputShortInstruction.
    def exitAputShortInstruction(self, ctx:SmaliParser.AputShortInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#igetInstruction.
    def enterIgetInstruction(self, ctx:SmaliParser.IgetInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#igetInstruction.
    def exitIgetInstruction(self, ctx:SmaliParser.IgetInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#igetWideInstruction.
    def enterIgetWideInstruction(self, ctx:SmaliParser.IgetWideInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#igetWideInstruction.
    def exitIgetWideInstruction(self, ctx:SmaliParser.IgetWideInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#igetObjectInstruction.
    def enterIgetObjectInstruction(self, ctx:SmaliParser.IgetObjectInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#igetObjectInstruction.
    def exitIgetObjectInstruction(self, ctx:SmaliParser.IgetObjectInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#igetBooleanInstruction.
    def enterIgetBooleanInstruction(self, ctx:SmaliParser.IgetBooleanInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#igetBooleanInstruction.
    def exitIgetBooleanInstruction(self, ctx:SmaliParser.IgetBooleanInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#igetByteInstruction.
    def enterIgetByteInstruction(self, ctx:SmaliParser.IgetByteInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#igetByteInstruction.
    def exitIgetByteInstruction(self, ctx:SmaliParser.IgetByteInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#igetCharInstruction.
    def enterIgetCharInstruction(self, ctx:SmaliParser.IgetCharInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#igetCharInstruction.
    def exitIgetCharInstruction(self, ctx:SmaliParser.IgetCharInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#igetShortInstruction.
    def enterIgetShortInstruction(self, ctx:SmaliParser.IgetShortInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#igetShortInstruction.
    def exitIgetShortInstruction(self, ctx:SmaliParser.IgetShortInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#iputInstruction.
    def enterIputInstruction(self, ctx:SmaliParser.IputInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#iputInstruction.
    def exitIputInstruction(self, ctx:SmaliParser.IputInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#iputWideInstruction.
    def enterIputWideInstruction(self, ctx:SmaliParser.IputWideInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#iputWideInstruction.
    def exitIputWideInstruction(self, ctx:SmaliParser.IputWideInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#iputObjectInstruction.
    def enterIputObjectInstruction(self, ctx:SmaliParser.IputObjectInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#iputObjectInstruction.
    def exitIputObjectInstruction(self, ctx:SmaliParser.IputObjectInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#iputBooleanInstruction.
    def enterIputBooleanInstruction(self, ctx:SmaliParser.IputBooleanInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#iputBooleanInstruction.
    def exitIputBooleanInstruction(self, ctx:SmaliParser.IputBooleanInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#iputByteInstruction.
    def enterIputByteInstruction(self, ctx:SmaliParser.IputByteInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#iputByteInstruction.
    def exitIputByteInstruction(self, ctx:SmaliParser.IputByteInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#iputCharInstruction.
    def enterIputCharInstruction(self, ctx:SmaliParser.IputCharInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#iputCharInstruction.
    def exitIputCharInstruction(self, ctx:SmaliParser.IputCharInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#iputShortInstruction.
    def enterIputShortInstruction(self, ctx:SmaliParser.IputShortInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#iputShortInstruction.
    def exitIputShortInstruction(self, ctx:SmaliParser.IputShortInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#addIntInstruction.
    def enterAddIntInstruction(self, ctx:SmaliParser.AddIntInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#addIntInstruction.
    def exitAddIntInstruction(self, ctx:SmaliParser.AddIntInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#subIntInstruction.
    def enterSubIntInstruction(self, ctx:SmaliParser.SubIntInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#subIntInstruction.
    def exitSubIntInstruction(self, ctx:SmaliParser.SubIntInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#mulIntInstruction.
    def enterMulIntInstruction(self, ctx:SmaliParser.MulIntInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#mulIntInstruction.
    def exitMulIntInstruction(self, ctx:SmaliParser.MulIntInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#divIntInstruction.
    def enterDivIntInstruction(self, ctx:SmaliParser.DivIntInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#divIntInstruction.
    def exitDivIntInstruction(self, ctx:SmaliParser.DivIntInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#remIntInstruction.
    def enterRemIntInstruction(self, ctx:SmaliParser.RemIntInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#remIntInstruction.
    def exitRemIntInstruction(self, ctx:SmaliParser.RemIntInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#andIntInstruction.
    def enterAndIntInstruction(self, ctx:SmaliParser.AndIntInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#andIntInstruction.
    def exitAndIntInstruction(self, ctx:SmaliParser.AndIntInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#orIntInstruction.
    def enterOrIntInstruction(self, ctx:SmaliParser.OrIntInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#orIntInstruction.
    def exitOrIntInstruction(self, ctx:SmaliParser.OrIntInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#xorIntInstruction.
    def enterXorIntInstruction(self, ctx:SmaliParser.XorIntInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#xorIntInstruction.
    def exitXorIntInstruction(self, ctx:SmaliParser.XorIntInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#shlIntInstruction.
    def enterShlIntInstruction(self, ctx:SmaliParser.ShlIntInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#shlIntInstruction.
    def exitShlIntInstruction(self, ctx:SmaliParser.ShlIntInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#shrIntInstruction.
    def enterShrIntInstruction(self, ctx:SmaliParser.ShrIntInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#shrIntInstruction.
    def exitShrIntInstruction(self, ctx:SmaliParser.ShrIntInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#ushrIntInstruction.
    def enterUshrIntInstruction(self, ctx:SmaliParser.UshrIntInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#ushrIntInstruction.
    def exitUshrIntInstruction(self, ctx:SmaliParser.UshrIntInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#rsubIntInstruction.
    def enterRsubIntInstruction(self, ctx:SmaliParser.RsubIntInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#rsubIntInstruction.
    def exitRsubIntInstruction(self, ctx:SmaliParser.RsubIntInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#addLongInstruction.
    def enterAddLongInstruction(self, ctx:SmaliParser.AddLongInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#addLongInstruction.
    def exitAddLongInstruction(self, ctx:SmaliParser.AddLongInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#subLongInstruction.
    def enterSubLongInstruction(self, ctx:SmaliParser.SubLongInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#subLongInstruction.
    def exitSubLongInstruction(self, ctx:SmaliParser.SubLongInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#mulLongInstruction.
    def enterMulLongInstruction(self, ctx:SmaliParser.MulLongInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#mulLongInstruction.
    def exitMulLongInstruction(self, ctx:SmaliParser.MulLongInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#divLongInstruction.
    def enterDivLongInstruction(self, ctx:SmaliParser.DivLongInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#divLongInstruction.
    def exitDivLongInstruction(self, ctx:SmaliParser.DivLongInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#remLongInstruction.
    def enterRemLongInstruction(self, ctx:SmaliParser.RemLongInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#remLongInstruction.
    def exitRemLongInstruction(self, ctx:SmaliParser.RemLongInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#andLongInstruction.
    def enterAndLongInstruction(self, ctx:SmaliParser.AndLongInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#andLongInstruction.
    def exitAndLongInstruction(self, ctx:SmaliParser.AndLongInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#orLongInstruction.
    def enterOrLongInstruction(self, ctx:SmaliParser.OrLongInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#orLongInstruction.
    def exitOrLongInstruction(self, ctx:SmaliParser.OrLongInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#xorLongInstruction.
    def enterXorLongInstruction(self, ctx:SmaliParser.XorLongInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#xorLongInstruction.
    def exitXorLongInstruction(self, ctx:SmaliParser.XorLongInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#shlLongInstruction.
    def enterShlLongInstruction(self, ctx:SmaliParser.ShlLongInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#shlLongInstruction.
    def exitShlLongInstruction(self, ctx:SmaliParser.ShlLongInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#shrLongInstruction.
    def enterShrLongInstruction(self, ctx:SmaliParser.ShrLongInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#shrLongInstruction.
    def exitShrLongInstruction(self, ctx:SmaliParser.ShrLongInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#ushrLongInstruction.
    def enterUshrLongInstruction(self, ctx:SmaliParser.UshrLongInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#ushrLongInstruction.
    def exitUshrLongInstruction(self, ctx:SmaliParser.UshrLongInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#addFloatInstruction.
    def enterAddFloatInstruction(self, ctx:SmaliParser.AddFloatInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#addFloatInstruction.
    def exitAddFloatInstruction(self, ctx:SmaliParser.AddFloatInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#subFloatInstruction.
    def enterSubFloatInstruction(self, ctx:SmaliParser.SubFloatInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#subFloatInstruction.
    def exitSubFloatInstruction(self, ctx:SmaliParser.SubFloatInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#mulFloatInstruction.
    def enterMulFloatInstruction(self, ctx:SmaliParser.MulFloatInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#mulFloatInstruction.
    def exitMulFloatInstruction(self, ctx:SmaliParser.MulFloatInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#divFloatInstruction.
    def enterDivFloatInstruction(self, ctx:SmaliParser.DivFloatInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#divFloatInstruction.
    def exitDivFloatInstruction(self, ctx:SmaliParser.DivFloatInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#remFloatInstruction.
    def enterRemFloatInstruction(self, ctx:SmaliParser.RemFloatInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#remFloatInstruction.
    def exitRemFloatInstruction(self, ctx:SmaliParser.RemFloatInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#addDoubleInstruction.
    def enterAddDoubleInstruction(self, ctx:SmaliParser.AddDoubleInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#addDoubleInstruction.
    def exitAddDoubleInstruction(self, ctx:SmaliParser.AddDoubleInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#subDoubleInstruction.
    def enterSubDoubleInstruction(self, ctx:SmaliParser.SubDoubleInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#subDoubleInstruction.
    def exitSubDoubleInstruction(self, ctx:SmaliParser.SubDoubleInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#mulDoubleInstruction.
    def enterMulDoubleInstruction(self, ctx:SmaliParser.MulDoubleInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#mulDoubleInstruction.
    def exitMulDoubleInstruction(self, ctx:SmaliParser.MulDoubleInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#divDoubleInstruction.
    def enterDivDoubleInstruction(self, ctx:SmaliParser.DivDoubleInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#divDoubleInstruction.
    def exitDivDoubleInstruction(self, ctx:SmaliParser.DivDoubleInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#remDoubleInstruction.
    def enterRemDoubleInstruction(self, ctx:SmaliParser.RemDoubleInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#remDoubleInstruction.
    def exitRemDoubleInstruction(self, ctx:SmaliParser.RemDoubleInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#addIntLit16Instruction.
    def enterAddIntLit16Instruction(self, ctx:SmaliParser.AddIntLit16InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#addIntLit16Instruction.
    def exitAddIntLit16Instruction(self, ctx:SmaliParser.AddIntLit16InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#mulIntLit16Instruction.
    def enterMulIntLit16Instruction(self, ctx:SmaliParser.MulIntLit16InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#mulIntLit16Instruction.
    def exitMulIntLit16Instruction(self, ctx:SmaliParser.MulIntLit16InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#divIntLit16Instruction.
    def enterDivIntLit16Instruction(self, ctx:SmaliParser.DivIntLit16InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#divIntLit16Instruction.
    def exitDivIntLit16Instruction(self, ctx:SmaliParser.DivIntLit16InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#remIntLit16Instruction.
    def enterRemIntLit16Instruction(self, ctx:SmaliParser.RemIntLit16InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#remIntLit16Instruction.
    def exitRemIntLit16Instruction(self, ctx:SmaliParser.RemIntLit16InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#andIntLit16Instruction.
    def enterAndIntLit16Instruction(self, ctx:SmaliParser.AndIntLit16InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#andIntLit16Instruction.
    def exitAndIntLit16Instruction(self, ctx:SmaliParser.AndIntLit16InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#orIntLit16Instruction.
    def enterOrIntLit16Instruction(self, ctx:SmaliParser.OrIntLit16InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#orIntLit16Instruction.
    def exitOrIntLit16Instruction(self, ctx:SmaliParser.OrIntLit16InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#xorIntLit16Instruction.
    def enterXorIntLit16Instruction(self, ctx:SmaliParser.XorIntLit16InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#xorIntLit16Instruction.
    def exitXorIntLit16Instruction(self, ctx:SmaliParser.XorIntLit16InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#addIntLit8Instruction.
    def enterAddIntLit8Instruction(self, ctx:SmaliParser.AddIntLit8InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#addIntLit8Instruction.
    def exitAddIntLit8Instruction(self, ctx:SmaliParser.AddIntLit8InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#rsubIntLit8Instruction.
    def enterRsubIntLit8Instruction(self, ctx:SmaliParser.RsubIntLit8InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#rsubIntLit8Instruction.
    def exitRsubIntLit8Instruction(self, ctx:SmaliParser.RsubIntLit8InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#mulIntLit8Instruction.
    def enterMulIntLit8Instruction(self, ctx:SmaliParser.MulIntLit8InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#mulIntLit8Instruction.
    def exitMulIntLit8Instruction(self, ctx:SmaliParser.MulIntLit8InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#divIntLit8Instruction.
    def enterDivIntLit8Instruction(self, ctx:SmaliParser.DivIntLit8InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#divIntLit8Instruction.
    def exitDivIntLit8Instruction(self, ctx:SmaliParser.DivIntLit8InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#remIntLit8Instruction.
    def enterRemIntLit8Instruction(self, ctx:SmaliParser.RemIntLit8InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#remIntLit8Instruction.
    def exitRemIntLit8Instruction(self, ctx:SmaliParser.RemIntLit8InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#andIntLit8Instruction.
    def enterAndIntLit8Instruction(self, ctx:SmaliParser.AndIntLit8InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#andIntLit8Instruction.
    def exitAndIntLit8Instruction(self, ctx:SmaliParser.AndIntLit8InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#orIntLit8Instruction.
    def enterOrIntLit8Instruction(self, ctx:SmaliParser.OrIntLit8InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#orIntLit8Instruction.
    def exitOrIntLit8Instruction(self, ctx:SmaliParser.OrIntLit8InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#xorIntLit8Instruction.
    def enterXorIntLit8Instruction(self, ctx:SmaliParser.XorIntLit8InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#xorIntLit8Instruction.
    def exitXorIntLit8Instruction(self, ctx:SmaliParser.XorIntLit8InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#shlIntLit8Instruction.
    def enterShlIntLit8Instruction(self, ctx:SmaliParser.ShlIntLit8InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#shlIntLit8Instruction.
    def exitShlIntLit8Instruction(self, ctx:SmaliParser.ShlIntLit8InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#shrIntLit8Instruction.
    def enterShrIntLit8Instruction(self, ctx:SmaliParser.ShrIntLit8InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#shrIntLit8Instruction.
    def exitShrIntLit8Instruction(self, ctx:SmaliParser.ShrIntLit8InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#ushrIntLit8Instruction.
    def enterUshrIntLit8Instruction(self, ctx:SmaliParser.UshrIntLit8InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#ushrIntLit8Instruction.
    def exitUshrIntLit8Instruction(self, ctx:SmaliParser.UshrIntLit8InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#newInstanceType.
    def enterNewInstanceType(self, ctx:SmaliParser.NewInstanceTypeContext):
        pass

    # Exit a parse tree produced by SmaliParser#newInstanceType.
    def exitNewInstanceType(self, ctx:SmaliParser.NewInstanceTypeContext):
        pass


    # Enter a parse tree produced by SmaliParser#newInstanceInstruction.
    def enterNewInstanceInstruction(self, ctx:SmaliParser.NewInstanceInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#newInstanceInstruction.
    def exitNewInstanceInstruction(self, ctx:SmaliParser.NewInstanceInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#checkCastType.
    def enterCheckCastType(self, ctx:SmaliParser.CheckCastTypeContext):
        pass

    # Exit a parse tree produced by SmaliParser#checkCastType.
    def exitCheckCastType(self, ctx:SmaliParser.CheckCastTypeContext):
        pass


    # Enter a parse tree produced by SmaliParser#checkCastInstruction.
    def enterCheckCastInstruction(self, ctx:SmaliParser.CheckCastInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#checkCastInstruction.
    def exitCheckCastInstruction(self, ctx:SmaliParser.CheckCastInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#arrayLengthInstruction.
    def enterArrayLengthInstruction(self, ctx:SmaliParser.ArrayLengthInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#arrayLengthInstruction.
    def exitArrayLengthInstruction(self, ctx:SmaliParser.ArrayLengthInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#arrayElementType.
    def enterArrayElementType(self, ctx:SmaliParser.ArrayElementTypeContext):
        pass

    # Exit a parse tree produced by SmaliParser#arrayElementType.
    def exitArrayElementType(self, ctx:SmaliParser.ArrayElementTypeContext):
        pass


    # Enter a parse tree produced by SmaliParser#arrayElementRegisterRange.
    def enterArrayElementRegisterRange(self, ctx:SmaliParser.ArrayElementRegisterRangeContext):
        pass

    # Exit a parse tree produced by SmaliParser#arrayElementRegisterRange.
    def exitArrayElementRegisterRange(self, ctx:SmaliParser.ArrayElementRegisterRangeContext):
        pass


    # Enter a parse tree produced by SmaliParser#arrayElementRegisters.
    def enterArrayElementRegisters(self, ctx:SmaliParser.ArrayElementRegistersContext):
        pass

    # Exit a parse tree produced by SmaliParser#arrayElementRegisters.
    def exitArrayElementRegisters(self, ctx:SmaliParser.ArrayElementRegistersContext):
        pass


    # Enter a parse tree produced by SmaliParser#filledNewArrayRangeInstruction.
    def enterFilledNewArrayRangeInstruction(self, ctx:SmaliParser.FilledNewArrayRangeInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#filledNewArrayRangeInstruction.
    def exitFilledNewArrayRangeInstruction(self, ctx:SmaliParser.FilledNewArrayRangeInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#filledNewArrayInstruction.
    def enterFilledNewArrayInstruction(self, ctx:SmaliParser.FilledNewArrayInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#filledNewArrayInstruction.
    def exitFilledNewArrayInstruction(self, ctx:SmaliParser.FilledNewArrayInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#filledArrayDataLabel.
    def enterFilledArrayDataLabel(self, ctx:SmaliParser.FilledArrayDataLabelContext):
        pass

    # Exit a parse tree produced by SmaliParser#filledArrayDataLabel.
    def exitFilledArrayDataLabel(self, ctx:SmaliParser.FilledArrayDataLabelContext):
        pass


    # Enter a parse tree produced by SmaliParser#fillArrayDataInstruction.
    def enterFillArrayDataInstruction(self, ctx:SmaliParser.FillArrayDataInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#fillArrayDataInstruction.
    def exitFillArrayDataInstruction(self, ctx:SmaliParser.FillArrayDataInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#checkInstanceType.
    def enterCheckInstanceType(self, ctx:SmaliParser.CheckInstanceTypeContext):
        pass

    # Exit a parse tree produced by SmaliParser#checkInstanceType.
    def exitCheckInstanceType(self, ctx:SmaliParser.CheckInstanceTypeContext):
        pass


    # Enter a parse tree produced by SmaliParser#instanceOfInstruction.
    def enterInstanceOfInstruction(self, ctx:SmaliParser.InstanceOfInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#instanceOfInstruction.
    def exitInstanceOfInstruction(self, ctx:SmaliParser.InstanceOfInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#arraySizeRegister.
    def enterArraySizeRegister(self, ctx:SmaliParser.ArraySizeRegisterContext):
        pass

    # Exit a parse tree produced by SmaliParser#arraySizeRegister.
    def exitArraySizeRegister(self, ctx:SmaliParser.ArraySizeRegisterContext):
        pass


    # Enter a parse tree produced by SmaliParser#newArrayInstruction.
    def enterNewArrayInstruction(self, ctx:SmaliParser.NewArrayInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#newArrayInstruction.
    def exitNewArrayInstruction(self, ctx:SmaliParser.NewArrayInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#packedSwitchRegister.
    def enterPackedSwitchRegister(self, ctx:SmaliParser.PackedSwitchRegisterContext):
        pass

    # Exit a parse tree produced by SmaliParser#packedSwitchRegister.
    def exitPackedSwitchRegister(self, ctx:SmaliParser.PackedSwitchRegisterContext):
        pass


    # Enter a parse tree produced by SmaliParser#packedSwitchLabel.
    def enterPackedSwitchLabel(self, ctx:SmaliParser.PackedSwitchLabelContext):
        pass

    # Exit a parse tree produced by SmaliParser#packedSwitchLabel.
    def exitPackedSwitchLabel(self, ctx:SmaliParser.PackedSwitchLabelContext):
        pass


    # Enter a parse tree produced by SmaliParser#sparseSwitchRegister.
    def enterSparseSwitchRegister(self, ctx:SmaliParser.SparseSwitchRegisterContext):
        pass

    # Exit a parse tree produced by SmaliParser#sparseSwitchRegister.
    def exitSparseSwitchRegister(self, ctx:SmaliParser.SparseSwitchRegisterContext):
        pass


    # Enter a parse tree produced by SmaliParser#sparseSwitchLabel.
    def enterSparseSwitchLabel(self, ctx:SmaliParser.SparseSwitchLabelContext):
        pass

    # Exit a parse tree produced by SmaliParser#sparseSwitchLabel.
    def exitSparseSwitchLabel(self, ctx:SmaliParser.SparseSwitchLabelContext):
        pass


    # Enter a parse tree produced by SmaliParser#packedSwitchInstruction.
    def enterPackedSwitchInstruction(self, ctx:SmaliParser.PackedSwitchInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#packedSwitchInstruction.
    def exitPackedSwitchInstruction(self, ctx:SmaliParser.PackedSwitchInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#sparseSwitchInstruction.
    def enterSparseSwitchInstruction(self, ctx:SmaliParser.SparseSwitchInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#sparseSwitchInstruction.
    def exitSparseSwitchInstruction(self, ctx:SmaliParser.SparseSwitchInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#invokePolymorphicInstruction.
    def enterInvokePolymorphicInstruction(self, ctx:SmaliParser.InvokePolymorphicInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#invokePolymorphicInstruction.
    def exitInvokePolymorphicInstruction(self, ctx:SmaliParser.InvokePolymorphicInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#invokePolymorphicRangeInstruction.
    def enterInvokePolymorphicRangeInstruction(self, ctx:SmaliParser.InvokePolymorphicRangeInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#invokePolymorphicRangeInstruction.
    def exitInvokePolymorphicRangeInstruction(self, ctx:SmaliParser.InvokePolymorphicRangeInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#invokeCustomInstruction.
    def enterInvokeCustomInstruction(self, ctx:SmaliParser.InvokeCustomInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#invokeCustomInstruction.
    def exitInvokeCustomInstruction(self, ctx:SmaliParser.InvokeCustomInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#invokeCustomRangeInstruction.
    def enterInvokeCustomRangeInstruction(self, ctx:SmaliParser.InvokeCustomRangeInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#invokeCustomRangeInstruction.
    def exitInvokeCustomRangeInstruction(self, ctx:SmaliParser.InvokeCustomRangeInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#invokeConstMethodHandleInstruction.
    def enterInvokeConstMethodHandleInstruction(self, ctx:SmaliParser.InvokeConstMethodHandleInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#invokeConstMethodHandleInstruction.
    def exitInvokeConstMethodHandleInstruction(self, ctx:SmaliParser.InvokeConstMethodHandleInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#invokeConstMethodTypeInstruction.
    def enterInvokeConstMethodTypeInstruction(self, ctx:SmaliParser.InvokeConstMethodTypeInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#invokeConstMethodTypeInstruction.
    def exitInvokeConstMethodTypeInstruction(self, ctx:SmaliParser.InvokeConstMethodTypeInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#binaryInstruction.
    def enterBinaryInstruction(self, ctx:SmaliParser.BinaryInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#binaryInstruction.
    def exitBinaryInstruction(self, ctx:SmaliParser.BinaryInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#ternaryInstruction.
    def enterTernaryInstruction(self, ctx:SmaliParser.TernaryInstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#ternaryInstruction.
    def exitTernaryInstruction(self, ctx:SmaliParser.TernaryInstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#instruction.
    def enterInstruction(self, ctx:SmaliParser.InstructionContext):
        pass

    # Exit a parse tree produced by SmaliParser#instruction.
    def exitInstruction(self, ctx:SmaliParser.InstructionContext):
        pass


    # Enter a parse tree produced by SmaliParser#methodInvocationTarget.
    def enterMethodInvocationTarget(self, ctx:SmaliParser.MethodInvocationTargetContext):
        pass

    # Exit a parse tree produced by SmaliParser#methodInvocationTarget.
    def exitMethodInvocationTarget(self, ctx:SmaliParser.MethodInvocationTargetContext):
        pass


    # Enter a parse tree produced by SmaliParser#fieldInvocationTarget.
    def enterFieldInvocationTarget(self, ctx:SmaliParser.FieldInvocationTargetContext):
        pass

    # Exit a parse tree produced by SmaliParser#fieldInvocationTarget.
    def exitFieldInvocationTarget(self, ctx:SmaliParser.FieldInvocationTargetContext):
        pass


    # Enter a parse tree produced by SmaliParser#fieldName.
    def enterFieldName(self, ctx:SmaliParser.FieldNameContext):
        pass

    # Exit a parse tree produced by SmaliParser#fieldName.
    def exitFieldName(self, ctx:SmaliParser.FieldNameContext):
        pass


    # Enter a parse tree produced by SmaliParser#fieldType.
    def enterFieldType(self, ctx:SmaliParser.FieldTypeContext):
        pass

    # Exit a parse tree produced by SmaliParser#fieldType.
    def exitFieldType(self, ctx:SmaliParser.FieldTypeContext):
        pass


    # Enter a parse tree produced by SmaliParser#fieldNameAndType.
    def enterFieldNameAndType(self, ctx:SmaliParser.FieldNameAndTypeContext):
        pass

    # Exit a parse tree produced by SmaliParser#fieldNameAndType.
    def exitFieldNameAndType(self, ctx:SmaliParser.FieldNameAndTypeContext):
        pass


    # Enter a parse tree produced by SmaliParser#fieldDirective.
    def enterFieldDirective(self, ctx:SmaliParser.FieldDirectiveContext):
        pass

    # Exit a parse tree produced by SmaliParser#fieldDirective.
    def exitFieldDirective(self, ctx:SmaliParser.FieldDirectiveContext):
        pass


    # Enter a parse tree produced by SmaliParser#endFieldDirective.
    def enterEndFieldDirective(self, ctx:SmaliParser.EndFieldDirectiveContext):
        pass

    # Exit a parse tree produced by SmaliParser#endFieldDirective.
    def exitEndFieldDirective(self, ctx:SmaliParser.EndFieldDirectiveContext):
        pass


    # Enter a parse tree produced by SmaliParser#className.
    def enterClassName(self, ctx:SmaliParser.ClassNameContext):
        pass

    # Exit a parse tree produced by SmaliParser#className.
    def exitClassName(self, ctx:SmaliParser.ClassNameContext):
        pass


    # Enter a parse tree produced by SmaliParser#classDirective.
    def enterClassDirective(self, ctx:SmaliParser.ClassDirectiveContext):
        pass

    # Exit a parse tree produced by SmaliParser#classDirective.
    def exitClassDirective(self, ctx:SmaliParser.ClassDirectiveContext):
        pass


    # Enter a parse tree produced by SmaliParser#superName.
    def enterSuperName(self, ctx:SmaliParser.SuperNameContext):
        pass

    # Exit a parse tree produced by SmaliParser#superName.
    def exitSuperName(self, ctx:SmaliParser.SuperNameContext):
        pass


    # Enter a parse tree produced by SmaliParser#superDirective.
    def enterSuperDirective(self, ctx:SmaliParser.SuperDirectiveContext):
        pass

    # Exit a parse tree produced by SmaliParser#superDirective.
    def exitSuperDirective(self, ctx:SmaliParser.SuperDirectiveContext):
        pass


    # Enter a parse tree produced by SmaliParser#sourceName.
    def enterSourceName(self, ctx:SmaliParser.SourceNameContext):
        pass

    # Exit a parse tree produced by SmaliParser#sourceName.
    def exitSourceName(self, ctx:SmaliParser.SourceNameContext):
        pass


    # Enter a parse tree produced by SmaliParser#sourceDirective.
    def enterSourceDirective(self, ctx:SmaliParser.SourceDirectiveContext):
        pass

    # Exit a parse tree produced by SmaliParser#sourceDirective.
    def exitSourceDirective(self, ctx:SmaliParser.SourceDirectiveContext):
        pass


    # Enter a parse tree produced by SmaliParser#methodIdentifier.
    def enterMethodIdentifier(self, ctx:SmaliParser.MethodIdentifierContext):
        pass

    # Exit a parse tree produced by SmaliParser#methodIdentifier.
    def exitMethodIdentifier(self, ctx:SmaliParser.MethodIdentifierContext):
        pass


    # Enter a parse tree produced by SmaliParser#methodReturnType.
    def enterMethodReturnType(self, ctx:SmaliParser.MethodReturnTypeContext):
        pass

    # Exit a parse tree produced by SmaliParser#methodReturnType.
    def exitMethodReturnType(self, ctx:SmaliParser.MethodReturnTypeContext):
        pass


    # Enter a parse tree produced by SmaliParser#methodParameterType.
    def enterMethodParameterType(self, ctx:SmaliParser.MethodParameterTypeContext):
        pass

    # Exit a parse tree produced by SmaliParser#methodParameterType.
    def exitMethodParameterType(self, ctx:SmaliParser.MethodParameterTypeContext):
        pass


    # Enter a parse tree produced by SmaliParser#methodArguments.
    def enterMethodArguments(self, ctx:SmaliParser.MethodArgumentsContext):
        pass

    # Exit a parse tree produced by SmaliParser#methodArguments.
    def exitMethodArguments(self, ctx:SmaliParser.MethodArgumentsContext):
        pass


    # Enter a parse tree produced by SmaliParser#methodSignature.
    def enterMethodSignature(self, ctx:SmaliParser.MethodSignatureContext):
        pass

    # Exit a parse tree produced by SmaliParser#methodSignature.
    def exitMethodSignature(self, ctx:SmaliParser.MethodSignatureContext):
        pass


    # Enter a parse tree produced by SmaliParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:SmaliParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by SmaliParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:SmaliParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by SmaliParser#annotationScope.
    def enterAnnotationScope(self, ctx:SmaliParser.AnnotationScopeContext):
        pass

    # Exit a parse tree produced by SmaliParser#annotationScope.
    def exitAnnotationScope(self, ctx:SmaliParser.AnnotationScopeContext):
        pass


    # Enter a parse tree produced by SmaliParser#annotationType.
    def enterAnnotationType(self, ctx:SmaliParser.AnnotationTypeContext):
        pass

    # Exit a parse tree produced by SmaliParser#annotationType.
    def exitAnnotationType(self, ctx:SmaliParser.AnnotationTypeContext):
        pass


    # Enter a parse tree produced by SmaliParser#annotationFieldValue.
    def enterAnnotationFieldValue(self, ctx:SmaliParser.AnnotationFieldValueContext):
        pass

    # Exit a parse tree produced by SmaliParser#annotationFieldValue.
    def exitAnnotationFieldValue(self, ctx:SmaliParser.AnnotationFieldValueContext):
        pass


    # Enter a parse tree produced by SmaliParser#annotationValueScoped.
    def enterAnnotationValueScoped(self, ctx:SmaliParser.AnnotationValueScopedContext):
        pass

    # Exit a parse tree produced by SmaliParser#annotationValueScoped.
    def exitAnnotationValueScoped(self, ctx:SmaliParser.AnnotationValueScopedContext):
        pass


    # Enter a parse tree produced by SmaliParser#annotationField.
    def enterAnnotationField(self, ctx:SmaliParser.AnnotationFieldContext):
        pass

    # Exit a parse tree produced by SmaliParser#annotationField.
    def exitAnnotationField(self, ctx:SmaliParser.AnnotationFieldContext):
        pass


    # Enter a parse tree produced by SmaliParser#annotationDirective.
    def enterAnnotationDirective(self, ctx:SmaliParser.AnnotationDirectiveContext):
        pass

    # Exit a parse tree produced by SmaliParser#annotationDirective.
    def exitAnnotationDirective(self, ctx:SmaliParser.AnnotationDirectiveContext):
        pass


    # Enter a parse tree produced by SmaliParser#locaDirectiveVariableName.
    def enterLocaDirectiveVariableName(self, ctx:SmaliParser.LocaDirectiveVariableNameContext):
        pass

    # Exit a parse tree produced by SmaliParser#locaDirectiveVariableName.
    def exitLocaDirectiveVariableName(self, ctx:SmaliParser.LocaDirectiveVariableNameContext):
        pass


    # Enter a parse tree produced by SmaliParser#localDirectiveType.
    def enterLocalDirectiveType(self, ctx:SmaliParser.LocalDirectiveTypeContext):
        pass

    # Exit a parse tree produced by SmaliParser#localDirectiveType.
    def exitLocalDirectiveType(self, ctx:SmaliParser.LocalDirectiveTypeContext):
        pass


    # Enter a parse tree produced by SmaliParser#localDirectiveGenericHint.
    def enterLocalDirectiveGenericHint(self, ctx:SmaliParser.LocalDirectiveGenericHintContext):
        pass

    # Exit a parse tree produced by SmaliParser#localDirectiveGenericHint.
    def exitLocalDirectiveGenericHint(self, ctx:SmaliParser.LocalDirectiveGenericHintContext):
        pass


    # Enter a parse tree produced by SmaliParser#localDirectiveRegister.
    def enterLocalDirectiveRegister(self, ctx:SmaliParser.LocalDirectiveRegisterContext):
        pass

    # Exit a parse tree produced by SmaliParser#localDirectiveRegister.
    def exitLocalDirectiveRegister(self, ctx:SmaliParser.LocalDirectiveRegisterContext):
        pass


    # Enter a parse tree produced by SmaliParser#localDirective.
    def enterLocalDirective(self, ctx:SmaliParser.LocalDirectiveContext):
        pass

    # Exit a parse tree produced by SmaliParser#localDirective.
    def exitLocalDirective(self, ctx:SmaliParser.LocalDirectiveContext):
        pass


    # Enter a parse tree produced by SmaliParser#localEndDirective.
    def enterLocalEndDirective(self, ctx:SmaliParser.LocalEndDirectiveContext):
        pass

    # Exit a parse tree produced by SmaliParser#localEndDirective.
    def exitLocalEndDirective(self, ctx:SmaliParser.LocalEndDirectiveContext):
        pass


    # Enter a parse tree produced by SmaliParser#localRestartDirective.
    def enterLocalRestartDirective(self, ctx:SmaliParser.LocalRestartDirectiveContext):
        pass

    # Exit a parse tree produced by SmaliParser#localRestartDirective.
    def exitLocalRestartDirective(self, ctx:SmaliParser.LocalRestartDirectiveContext):
        pass


    # Enter a parse tree produced by SmaliParser#lineLabel.
    def enterLineLabel(self, ctx:SmaliParser.LineLabelContext):
        pass

    # Exit a parse tree produced by SmaliParser#lineLabel.
    def exitLineLabel(self, ctx:SmaliParser.LineLabelContext):
        pass


    # Enter a parse tree produced by SmaliParser#methodBodyStatement.
    def enterMethodBodyStatement(self, ctx:SmaliParser.MethodBodyStatementContext):
        pass

    # Exit a parse tree produced by SmaliParser#methodBodyStatement.
    def exitMethodBodyStatement(self, ctx:SmaliParser.MethodBodyStatementContext):
        pass


    # Enter a parse tree produced by SmaliParser#methodBody.
    def enterMethodBody(self, ctx:SmaliParser.MethodBodyContext):
        pass

    # Exit a parse tree produced by SmaliParser#methodBody.
    def exitMethodBody(self, ctx:SmaliParser.MethodBodyContext):
        pass


    # Enter a parse tree produced by SmaliParser#packedSwitchIdent.
    def enterPackedSwitchIdent(self, ctx:SmaliParser.PackedSwitchIdentContext):
        pass

    # Exit a parse tree produced by SmaliParser#packedSwitchIdent.
    def exitPackedSwitchIdent(self, ctx:SmaliParser.PackedSwitchIdentContext):
        pass


    # Enter a parse tree produced by SmaliParser#packedSwitchDirectiveLabel.
    def enterPackedSwitchDirectiveLabel(self, ctx:SmaliParser.PackedSwitchDirectiveLabelContext):
        pass

    # Exit a parse tree produced by SmaliParser#packedSwitchDirectiveLabel.
    def exitPackedSwitchDirectiveLabel(self, ctx:SmaliParser.PackedSwitchDirectiveLabelContext):
        pass


    # Enter a parse tree produced by SmaliParser#packedSwitchDirectiveLabels.
    def enterPackedSwitchDirectiveLabels(self, ctx:SmaliParser.PackedSwitchDirectiveLabelsContext):
        pass

    # Exit a parse tree produced by SmaliParser#packedSwitchDirectiveLabels.
    def exitPackedSwitchDirectiveLabels(self, ctx:SmaliParser.PackedSwitchDirectiveLabelsContext):
        pass


    # Enter a parse tree produced by SmaliParser#packedSwitchDirective.
    def enterPackedSwitchDirective(self, ctx:SmaliParser.PackedSwitchDirectiveContext):
        pass

    # Exit a parse tree produced by SmaliParser#packedSwitchDirective.
    def exitPackedSwitchDirective(self, ctx:SmaliParser.PackedSwitchDirectiveContext):
        pass


    # Enter a parse tree produced by SmaliParser#methodDirective.
    def enterMethodDirective(self, ctx:SmaliParser.MethodDirectiveContext):
        pass

    # Exit a parse tree produced by SmaliParser#methodDirective.
    def exitMethodDirective(self, ctx:SmaliParser.MethodDirectiveContext):
        pass


    # Enter a parse tree produced by SmaliParser#registersDirective.
    def enterRegistersDirective(self, ctx:SmaliParser.RegistersDirectiveContext):
        pass

    # Exit a parse tree produced by SmaliParser#registersDirective.
    def exitRegistersDirective(self, ctx:SmaliParser.RegistersDirectiveContext):
        pass


    # Enter a parse tree produced by SmaliParser#localsDirective.
    def enterLocalsDirective(self, ctx:SmaliParser.LocalsDirectiveContext):
        pass

    # Exit a parse tree produced by SmaliParser#localsDirective.
    def exitLocalsDirective(self, ctx:SmaliParser.LocalsDirectiveContext):
        pass


    # Enter a parse tree produced by SmaliParser#simpleParamDirective.
    def enterSimpleParamDirective(self, ctx:SmaliParser.SimpleParamDirectiveContext):
        pass

    # Exit a parse tree produced by SmaliParser#simpleParamDirective.
    def exitSimpleParamDirective(self, ctx:SmaliParser.SimpleParamDirectiveContext):
        pass


    # Enter a parse tree produced by SmaliParser#extendedParamDirective.
    def enterExtendedParamDirective(self, ctx:SmaliParser.ExtendedParamDirectiveContext):
        pass

    # Exit a parse tree produced by SmaliParser#extendedParamDirective.
    def exitExtendedParamDirective(self, ctx:SmaliParser.ExtendedParamDirectiveContext):
        pass


    # Enter a parse tree produced by SmaliParser#paramDirective.
    def enterParamDirective(self, ctx:SmaliParser.ParamDirectiveContext):
        pass

    # Exit a parse tree produced by SmaliParser#paramDirective.
    def exitParamDirective(self, ctx:SmaliParser.ParamDirectiveContext):
        pass


    # Enter a parse tree produced by SmaliParser#lineDirective.
    def enterLineDirective(self, ctx:SmaliParser.LineDirectiveContext):
        pass

    # Exit a parse tree produced by SmaliParser#lineDirective.
    def exitLineDirective(self, ctx:SmaliParser.LineDirectiveContext):
        pass


    # Enter a parse tree produced by SmaliParser#catchFromLabel.
    def enterCatchFromLabel(self, ctx:SmaliParser.CatchFromLabelContext):
        pass

    # Exit a parse tree produced by SmaliParser#catchFromLabel.
    def exitCatchFromLabel(self, ctx:SmaliParser.CatchFromLabelContext):
        pass


    # Enter a parse tree produced by SmaliParser#catchToLabel.
    def enterCatchToLabel(self, ctx:SmaliParser.CatchToLabelContext):
        pass

    # Exit a parse tree produced by SmaliParser#catchToLabel.
    def exitCatchToLabel(self, ctx:SmaliParser.CatchToLabelContext):
        pass


    # Enter a parse tree produced by SmaliParser#catchGotoLabel.
    def enterCatchGotoLabel(self, ctx:SmaliParser.CatchGotoLabelContext):
        pass

    # Exit a parse tree produced by SmaliParser#catchGotoLabel.
    def exitCatchGotoLabel(self, ctx:SmaliParser.CatchGotoLabelContext):
        pass


    # Enter a parse tree produced by SmaliParser#catchExceptionType.
    def enterCatchExceptionType(self, ctx:SmaliParser.CatchExceptionTypeContext):
        pass

    # Exit a parse tree produced by SmaliParser#catchExceptionType.
    def exitCatchExceptionType(self, ctx:SmaliParser.CatchExceptionTypeContext):
        pass


    # Enter a parse tree produced by SmaliParser#catchDirective.
    def enterCatchDirective(self, ctx:SmaliParser.CatchDirectiveContext):
        pass

    # Exit a parse tree produced by SmaliParser#catchDirective.
    def exitCatchDirective(self, ctx:SmaliParser.CatchDirectiveContext):
        pass


    # Enter a parse tree produced by SmaliParser#catchAllDirective.
    def enterCatchAllDirective(self, ctx:SmaliParser.CatchAllDirectiveContext):
        pass

    # Exit a parse tree produced by SmaliParser#catchAllDirective.
    def exitCatchAllDirective(self, ctx:SmaliParser.CatchAllDirectiveContext):
        pass


    # Enter a parse tree produced by SmaliParser#arrayDataDirective.
    def enterArrayDataDirective(self, ctx:SmaliParser.ArrayDataDirectiveContext):
        pass

    # Exit a parse tree produced by SmaliParser#arrayDataDirective.
    def exitArrayDataDirective(self, ctx:SmaliParser.ArrayDataDirectiveContext):
        pass


    # Enter a parse tree produced by SmaliParser#arrayDataEntry.
    def enterArrayDataEntry(self, ctx:SmaliParser.ArrayDataEntryContext):
        pass

    # Exit a parse tree produced by SmaliParser#arrayDataEntry.
    def exitArrayDataEntry(self, ctx:SmaliParser.ArrayDataEntryContext):
        pass


    # Enter a parse tree produced by SmaliParser#sparseSwitchDirectiveValue.
    def enterSparseSwitchDirectiveValue(self, ctx:SmaliParser.SparseSwitchDirectiveValueContext):
        pass

    # Exit a parse tree produced by SmaliParser#sparseSwitchDirectiveValue.
    def exitSparseSwitchDirectiveValue(self, ctx:SmaliParser.SparseSwitchDirectiveValueContext):
        pass


    # Enter a parse tree produced by SmaliParser#sparseSwitchDirective.
    def enterSparseSwitchDirective(self, ctx:SmaliParser.SparseSwitchDirectiveContext):
        pass

    # Exit a parse tree produced by SmaliParser#sparseSwitchDirective.
    def exitSparseSwitchDirective(self, ctx:SmaliParser.SparseSwitchDirectiveContext):
        pass


    # Enter a parse tree produced by SmaliParser#implementsDirective.
    def enterImplementsDirective(self, ctx:SmaliParser.ImplementsDirectiveContext):
        pass

    # Exit a parse tree produced by SmaliParser#implementsDirective.
    def exitImplementsDirective(self, ctx:SmaliParser.ImplementsDirectiveContext):
        pass


    # Enter a parse tree produced by SmaliParser#statement.
    def enterStatement(self, ctx:SmaliParser.StatementContext):
        pass

    # Exit a parse tree produced by SmaliParser#statement.
    def exitStatement(self, ctx:SmaliParser.StatementContext):
        pass


    # Enter a parse tree produced by SmaliParser#smali_file.
    def enterSmali_file(self, ctx:SmaliParser.Smali_fileContext):
        pass

    # Exit a parse tree produced by SmaliParser#smali_file.
    def exitSmali_file(self, ctx:SmaliParser.Smali_fileContext):
        pass



del SmaliParser