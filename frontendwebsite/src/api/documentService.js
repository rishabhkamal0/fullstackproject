import axios from 'axios';

const API_URL = "http://localhost:8000/api";

export const uploadDocument = (file) => {
    const formData = new FormData();
    formData.append('file', file);
    return axios.post(`${API_URL}/documents/upload`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
    });
};

export const fetchDocuments = () => {
    return axios.get(`${API_URL}/documents`);
};

export const queryDocuments = (query) => {
    return axios.post(`${API_URL}/query`, { query });
};
