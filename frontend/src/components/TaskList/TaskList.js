import React, { useState, useEffect } from 'react';
import axios from 'axios';
import TaskForm from '../TaskForm/TaskForm';
import Switch from 'react-switch';
import './TaskList.css'; 

const TaskList = () => {
    const [tasks, setTasks] = useState([]);
    const [editTask, setEditTask] = useState(null);

    useEffect(() => {
        fetchTasks();
    }, []);

    const fetchTasks = async () => {
        try {
            const response = await axios.get('http://localhost:8888/tasks');
            setTasks(response.data || []);
        } catch (error) {
            console.error('Error fetching tasks:', error);
        }
    };

    const handleDelete = async (id) => {
        try {
            await axios.delete(`http://localhost:8888/tasks/${id}`);
            setTasks(tasks.filter(task => task.id !== id));
        } catch (error) {
            console.error('Error deleting task:', error);
        }
    };

    const handleEdit = (task) => {
        setEditTask(task);
    };

    const handleSave = () => {
        setEditTask(null);
        fetchTasks();
    };

    const handleToggle = async (id) => {
        const task = tasks.find(task => task.id === id);
        if (task) {
            try {
                await axios.put(`http://localhost:8888/tasks/${id}`, {
                    ...task,
                    completed: !task.completed
                });
                setTasks(tasks.map(t => t.id === id ? { ...t, completed: !t.completed } : t));
            } catch (error) {
                console.error('Error toggling task:', error);
            }
        }
    };

    return (
        <div>
            <h1>Task List</h1>
            <TaskForm task={editTask} onSave={handleSave} />
            <div className="task-list">
                {tasks.map((task) => (
                    <div
                        key={task.id}
                        className={`task-card ${task.completed ? "completed" : "not-completed"}`}
                    >
                        <h3>{task.title}</h3>
                        <p>{task.description}</p>
                        <label>
                            Completed:
                            <Switch
                                onChange={() => handleToggle(task.id)}
                                checked={task.completed}
                                className="react-switch"
                            />
                        </label>
                        <div className="buttons">
                            <button onClick={() => handleEdit(task)}>Edit</button>
                            <button onClick={() => handleDelete(task.id)}>Delete</button>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default TaskList;
