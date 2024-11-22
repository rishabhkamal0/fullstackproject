import React, { useState } from "react";
import { TextField, Button, Typography } from "@mui/material";
import { queryDocuments } from "../api/documentService";

const SearchPage = () => {
    const [query, setQuery] = useState("");
    const [results, setResults] = useState([]);

    const handleSearch = async () => {
        try {
            const response = await queryDocuments(query);
            setResults(response.data);
        } catch (error) {
            console.error("Search error:", error);
        }
    };

    return (
        <div>
            <Typography variant="h4">Search Documents</Typography>
            <TextField
                label="Enter your query"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                fullWidth
                margin="normal"
            />
            <Button variant="contained" color="primary" onClick={handleSearch}>
                Search
            </Button>
            <div>
                {results.map((result, index) => (
                    <Typography key={index}>{result.snippet}</Typography>
                ))}
            </div>
        </div>
    );
};

export default SearchPage;
