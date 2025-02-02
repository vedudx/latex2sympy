
from latex2sympy2 import latex2sympyStr
import traceback


def main():
    testList = [
        # r"x^1",
        # r"x^2",
        # r"x^3",
        # r"x^4",
        # r"x^{-1}",
        # r"x^{-2}",
        # r"e^1",
        # r"e^2",
        # r"e^3",
        # r"e^4",
        # r"e^{-1}",
        # r"e^{-2}",

        "---",
        
        #Derivatives tests
        r"\frac{\partial f(x,y)}{\partial x} ",
        r"\frac{df(x)}{dx} ",
        r"\frac{\partial}{\partial x} f(x,y) ",
        r"\frac{d}{dx} f(x)",
        r"\frac{\partial}{\partial x} \frac{1}{xy} ",
        r"\frac{d}{dx}  \frac{1}{xy}",

        # Functions tests
        r"f(x)",
        r"f(x+1)",
        r"f(x^2)",
        r"\sqrt{\frac{1}{x}}",
        r"\sum_{n = 0}^{\infty} \frac{1}{n!}",
        r"\prod^c_{a = b} x^{a!}",
        r"\log{e^{2*x!}}"

        # Integer * Symbol tests
        r"2x2y",
        r"2x2",
        r"2 4 2y",
        r"24 y",
        r"2 4 y",
        r"2 4 y",
        # Matrices
        r"\begin{matrix}1&2\\3&4\end{matrix}",
        r"\begin{bmatrix}1&2\\3&4\end{bmatrix}",
        r"\begin{pmatrix}1&2\\3&4\end{pmatrix}",
        # r"\begin{matrix}x&x^2\\\sqrt{x}&x\end{matrix}",
        r"\begin{matrix}\sqrt{x}\\\sin(\theta)\end{matrix}",

        "\\begin{pmatrix}1\\\\2\\\\3\\end{pmatrix}",
        "\\left{\\begin{pmatrix}1\\\\2\\\\3\\end{pmatrix}\\right}",
        "\\left\\{\\begin{pmatrix}1\\\\2\\\\3\\end{pmatrix}\\right\\}",
        r"\begin{pmatrix}1\\2\\3\end{pmatrix},\begin{pmatrix}4\\3\\1\end{pmatrix}",
        r"\begin{pmatrix}1\\2\\3\end{pmatrix},\begin{pmatrix}4\\3\\1\end{pmatrix}",

    ]


    for tex in testList:
        if tex == '---':
            print("\n")
        else:
            try:
                math = latex2sympyStr(tex)
            except Exception as err:
                # Print stack trace 
                print(traceback.format_exc())
                print(tex, f"--> Error: {err}")
            else:
                print(tex, "-->", math)

main()