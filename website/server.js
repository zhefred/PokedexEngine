const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const path = require('path');

const app = express();
const port = 8080;

app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
})

app.get('/pokedex', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'pokedex.html'));
})

app.get('/playnow', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'playnow.html'));
})

app.get('/api/messages', (req, res) => {
    const db = new sqlite3.Database('pokeDb.db');
    db.all('SELECT * FROM messages', [], (err, rows) => {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }
        res.json(rows);
    });
    db.close();
})

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
// const db = new sqlite3.Database('pokeDb.db', (err) => {
//     if (err) {
//         console.error('Error connecting to the database :', err.message);
//     } else {
//         console.log('Connected to the SQLite database.');
//     }
// })