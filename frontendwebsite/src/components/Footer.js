import React from "react";
import { Typography, Box } from "@mui/material";

const Footer = () => {
    return (
        <Box
            component="footer"
            sx={{
                backgroundColor: "#f5f5f5",
                padding: "10px 20px",
                textAlign: "center",
                marginTop: "20px",
            }}
        >
            <Typography variant="body2" color="textSecondary">
                © 2024 DocuQuery. All rights reserved.
            </Typography>
        </Box>
    );
};

export default Footer;
