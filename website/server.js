const { name } = require('ejs');
const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const path = require('path');

const app = express();
const port = 8080;

const dbPath = path.join(__dirname, 'pokeDb.sqlite');
const db = new sqlite3.Database(dbPath, (err) => {
    if (err) {
        console.error('Error connecting to the database : ', err.message);
    } else {
        console.log('Connected to the SQLite database')
    }
});

app.set('view engine', 'ejs');
app.set('views', './views');
app.use('/static', express.static(path.join(__dirname, 'static')));
app.use('/public', express.static(path.join(__dirname, 'public')));


app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.get('/pokedex', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'pokedex.html'));
});

app.get('/pokemon', (req, res) => {
    const pokemon_nbr = req.query.pokemon_nbr;
    res.sendFile(path.join(__dirname, 'public', 'poke_data.html'))
})

app.get('/playnow', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'playnow.html'));
});

app.get('/api/pokedex', (req, res) => {
    const request_type = req.query.req_type;
    const infos = req.query.info;

    if(request_type == "pkdx") {
        if(infos){    
            db.all('SELECT * FROM pokedex WHERE pokedex_nbr = ?', [infos], (err,rows) => {
                if (err) {
                    return res.status(500).json({ error: err.message });
                }

                if (rows.length > 0) {
                    res.json(rows);
                } else {
                    res.status(404).json({ error: "Pokemon not found" });
                }
            });
        } else {
            db.all('SELECT * FROM pokedex', [], (err, rows) => {
                if (err) {
                    return res.status(500).json({ error: err.message });
                }
                res.json(rows);
            });
        }
    } else if (request_type == "type") {
        db.all('SELECT * FROM types WHERE id = ?', [infos], (err,rows) => {
            if (err) {
                return res.status(500).json({ error: err.message });
            }
            res.json(rows);
        });
    }
});

app.get('/static/images/', (req, res) => {
    res.sendStatus(202);
})

app.use((req, res) => {
    res.status(404).sendFile(path.join(__dirname, 'public', '404.html'));
});


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