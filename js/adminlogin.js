export const adminLogin=(req,res)=>{
    try{
        const{username,password}=req.body
        if(username !==process.env.Admin_username || password !==process.env.password)
        {
            return res.status(401).json({success:"false",message:"invalid username"})

        }
        const token=jwt.sign({username:process.env.username},
            {processenvJWT_SECRET},
            {expiresIn:"1d"}
            
        )
        return res.json({success:"true",message:"login successfull"},
            token
        )

    }
    catch(error)
    {
        console.log(error.message)
        return res.status(500).json({success:"false",message:"server error"})

    }
}