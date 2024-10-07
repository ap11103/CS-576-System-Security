.data
.global READ_SZ
READ_SZ:
    .short 400
	
.text
.global	stack_pivot
stack_pivot:
    mov -0x18(%rbp), %rsp
    ret
