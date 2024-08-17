import streamlit as st
from streamlit_option_menu import option_menu

st.header("100 Days `C Programming` Tasks By Venkatesh ")

with st.sidebar:
    selected = option_menu("100 Days Task", ["Task-1 & 2", "Task-3 & 4"], icons=["book", "book"], menu_icon="cast", default_index=0)

if selected == "Task-1 & 2":
    st.subheader("1. Positive or Negative number:")
    st.code("""
           #include <stdio.h>

        int main() {
        int num;
        printf("Enter a number: ");
        scanf("%d", &num); 
        if (num > 0)
          printf("%d is positive.\n", num);
        else if (num < 0)
          printf("%d is negative.\n", num);
        else
          printf("The number is zero.\n");

        return 0;
    }

    """, language="c")

    st.subheader("2. Odd or Even number:")

    st.code("""
   #include <stdio.h>

    int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    if (num % 2 == 0)
        printf("%d is even.\n", num);
    else
        printf("%d is odd.\n", num);

    return 0;
    }
    """, language="c")
