/*
* @Author: liujinjia
* @Date:   2017-02-24 16:01:06
* @Last Modified by:   liujinjia
* @Last Modified time: 2017-02-24 16:56:27
*/

#include <stdio.h>
#include <limits.h>
#include <float.h>

int main() {
    printf("int 存储git大小 ： %lu \n", sizeof(int));
    printf("float 存储最大字节数 ： %lu \n", sizeof(float));
    printf("float 最小值 ：%E \n", FLT_MIN);
    printf("float 最大值 ：%E \n", FLT_MAX);
    printf("精度值 ：%d \n", FLT_DIG);
    return 0;
}