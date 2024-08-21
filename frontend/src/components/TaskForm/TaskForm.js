import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './TaskForm.css';

const TaskForm = ({ task, onSave }) => {
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [completed, setCompleted] = useState(false);

    useEffect(() => {
        if (task) {
            setTitle(task.title);
            setDescription(task.description);
            setCompleted(task.completed);
        }
    }, [task]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            if (task) {
                await axios.put(`http://localhost:8888/tasks/${task.id}`, {
                    title,
                    description,
                    completed,
                });
            } else {
                await axios.post('http://localhost:8888/tasks', {
                    title,
                    description,
                    completed,
                });
            }
            onSave();
            setTitle(''); 
            setDescription('');
            setCompleted(false);
        } catch (error) {
            console.error('Error saving task:', error);
        }
    };

    return (
        <div className="task-form-container">
            <form className="task-form" onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    placeholder="Title"
                    required
                />
                <textarea
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    placeholder="Description"
                    required
                />
                <label>
                    Completed:
                    <input
                        type="checkbox"
                        checked={completed}
                        onChange={(e) => setCompleted(e.target.checked)}
                    />
                </label>
                <button type="submit">Save</button>
            </form>
        </div>
    );
};

export default TaskForm;
