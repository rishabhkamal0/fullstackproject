import React, { useEffect, useState } from "react";
import {
    Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Button,
} from "@mui/material";
import { fetchDocuments } from "../api/documentService";

const DocumentList = () => {
    const [documents, setDocuments] = useState([]);

    useEffect(() => {
        const loadDocuments = async () => {
            try {
                const response = await fetchDocuments();
                setDocuments(response.data);
            } catch (error) {
                console.error("Error fetching documents:", error);
            }
        };
        loadDocuments();
    }, []);

    return (
        <TableContainer component={Paper}>
            <Table>
                <TableHead>
                    <TableRow>
                        <TableCell>Title</TableCell>
                        <TableCell>Size (KB)</TableCell>
                        <TableCell>Uploaded Date</TableCell>
                        <TableCell>Actions</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {documents.map((doc) => (
                        <TableRow key={doc.id}>
                            <TableCell>{doc.title}</TableCell>
                            <TableCell>{doc.size}</TableCell>
                            <TableCell>
                                {new Date(doc.date_uploaded).toLocaleDateString()}
                            </TableCell>
                            <TableCell>
                                <Button variant="outlined" color="primary">
                                    View
                                </Button>
                                <Button variant="outlined" color="error" style={{ marginLeft: "10px" }}>
                                    Delete
                                </Button>
                            </TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    );
};

export default DocumentList;
