import streamlit as st
from streamlit_option_menu import option_menu

st.header("100 Days `C Programming` Tasks By Venkatesh ")

with st.sidebar:
    selected = option_menu(menu_title="100 Days Task", 
    options=["Positive or Negative", "Odd or Even","Sum of First N Natural"], menu_icon="cast",icons=["book", "book", "book"], default_index=0)
    

if selected == "Positive or Negative":
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

elif selected == "Odd or Even":

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
elif selected == "Sum of First N Natural":
    st.subheader("3. Sum of First N Natural numbers :")

    st.write("you can use the formula:")

    st.latex(r'Sum = \frac{N \times (N + 1)}{2}')

    st.code("""
   #include <stdio.h>

    int main() {
    int N;
    long long sum;

    
    printf("Enter the value of N: ");
    scanf("%d", &N);

    
    sum = (long long)N * (N + 1) / 2;

    
    printf("The sum of the first %d natural numbers is: %lld\n", N, sum);

    return 0;
    }

    """, language="c")

    st.subheader("Keypoints :")
 
    st.write(' `long long` is used to store large numbers. ')


st.balloons()
