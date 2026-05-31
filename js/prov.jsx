import { Children, useContext, useState } from "react";

export const ThemeContext=useContext()
const ThemeProvider=({Children})=>{
    const[theme,setTheme]=useState("light")
    const toggleTheme=setTheme(theme==="light" ? "dark":"light")
    return(
        <ThemeContext.Provider value={{theme,setTheme,toggleTheme}}>
            {Children}

        </ThemeContext.Provider>
    )
}
export default ThemeProvider