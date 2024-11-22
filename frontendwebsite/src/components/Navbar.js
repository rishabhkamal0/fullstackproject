import React from "react";
import { AppBar, Toolbar, Typography, Button, Box } from "@mui/material";
import { Link } from "react-router-dom";

const Navbar = () => {
    return (
        <AppBar position="sticky" color="primary">
            <Toolbar>
                <Typography variant="h6" sx={{ flexGrow: 1 }}>
                    <Link to="/" style={{ textDecoration: "none", color: "#fff" }}>
                        DocuQuery
                    </Link>
                </Typography>
                <Box>
                    <Button color="inherit" component={Link} to="/upload">
                        Upload
                    </Button>
                    <Button color="inherit" component={Link} to="/search">
                        Search
                    </Button>
                </Box>
            </Toolbar>
        </AppBar>
    );
};

export default Navbar;
