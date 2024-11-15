const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const PORT = 3000;

mongoose.connect('mongodb://localhost:27017/todoapp', { useNewUrlParser: true, useUnifiedTopology: true });

const taskSchema = new mongoose.Schema({
    text: String,
    done: { type: Boolean, default: false }
});

const Task = mongoose.model('Task', taskSchema);

app.use(cors());
app.use(bodyParser.json());
app.use(express.static('public'));

app.get('/tasks', async (req, res) => {
    const tasks = await Task.find();
    res.json(tasks);
});

app.post('/tasks', async (req, res) => {
    const task = new Task(req.body);
    await task.save();
    res.status(201).send(task);
});

app.patch('/tasks/:id/toggle', async (req, res) => {
    const task = await Task.findById(req.params.id);
    task.done = !task.done;
    await task.save();
    res.send(task);
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
