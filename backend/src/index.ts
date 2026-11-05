import express from 'express';
import type { Express } from "express";

const app: Express = express();

const PORT: number = Number(process.env.APPLICATION_PORT) | 3000;


app.listen(PORT, () => {
    console.log(`Application is running on port: ${PORT}`)
})