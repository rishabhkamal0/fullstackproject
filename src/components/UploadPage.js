import React, { useState } from "react";
import { Button, Typography, CircularProgress } from "@mui/material";
import { uploadDocument } from "../api/documentService";
import '../styles/components/uploadPage.scss';


const UploadPage = () => {
    const [file, setFile] = useState(null);
    const [uploading, setUploading] = useState(false);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleUpload = async () => {
        if (file) {
            setUploading(true);
            try {
                await uploadDocument(file);
                alert("File uploaded successfully!");
            } catch (error) {
                console.error(error);
                alert("File upload failed.");
            } finally {
                setUploading(false);
            }
        }
    };

    return (
        <div className="upload-page">
            <Typography variant="h4" gutterBottom>Upload Your Document</Typography>
            <input
                type="file"
                onChange={handleFileChange}
                accept=".pdf,.csv,.ppt"
                style={{ margin: "20px 0" }}
            />
            {uploading ? (
                <CircularProgress />
            ) : (
                <Button variant="contained" color="primary" onClick={handleUpload}>
                    Upload
                </Button>
            )}
        </div>
    );
};

export default UploadPage;
