import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { CssBaseline } from "@mui/material";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import UploadPage from "./components/UploadPage";
import DocumentList from "./components/DocumentList";
import SearchPage from "./components/SearchPage";
import "./styles/global.scss"; // Import global styles

const App = () => {
    return (
        <Router>
            <CssBaseline />
            <Navbar />
            <main style={{ minHeight: "80vh", padding: "20px" }}>
                <Routes>
                    <Route path="/" element={<DocumentList />} />
                    <Route path="/upload" element={<UploadPage />} />
                    <Route path="/search" element={<SearchPage />} />
                </Routes>
            </main>
            <Footer />
        </Router>
    );
};

export default App;
