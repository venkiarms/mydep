import streamlit as st
import streamlit_option_menu as option_menu


with st.sidebar:
    selected = option_menu("Main Menu", ["Home", "About"], icons=["house", "book"], menu_icon="cast", default_index=0)

    if selected == "Task-1 & 2":
        st.subheader("Positive or Negative number:")
        st.code("""

           #include <stdio.h>
int main()
{
    int num = 23;
      
    //Conditions to check if the number is negative/positive or zero
    if (num > 0)
         printf("The number is positive");
    else if (num < 0)
        printf("The number is negative");
    else
        printf("Zero");
    
    return 0;
}

        """, language="c")


        st.subheader("Odd or Even number:")

        st.code("""
           #include <stdio.h>
int main()
{
    int num = 23;
      
    //Conditions to check if the number is odd/even
    if (num % 2 == 0)
         printf("The number is even");
    else
        printf("The number is odd");
    
    return 0;
}
                """,language="c")

 

