def RMB(dollar):
    RMB = dollar*6.28
    return ('%.2f美元=%.2f元'%(dollar,dollar*6.28))
dollar = float(input('输入美元'))
RMB(dollar)
print(RMB(dollar))
