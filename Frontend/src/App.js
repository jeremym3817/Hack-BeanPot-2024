import React, {useState} from 'react';
import {Card, CardActions, CardContent, CardMedia, Grid, Typography} from '@mui/material'
import Layout from './Layout.js';
import ClassList from './ClassList.js';
import HoverClassList from './HoverClassList.js';
import './App.css';

function App() {
  const [listOfCourses, setListOfCourses] = useState([ 
    { id: 0, courseName: "CS 2500", difficultly: "6.5/10", minYear: "1st", maxClassSize: 150,
    dayOfWeek: ["Monday, ", "Wednesday, ", "Thursday"], time: "8:00 - 9:05", professorName: "Vesely", selected: false },
    { id: 1, courseName: "CS 1800", difficultly: "4.3/10", minYear: "1st", maxClassSize: 300,
    dayOfWeek: ["Tuesday, ", "Friday"], time: "3:15 - 5:05", professorName: "Higger", selected: false },
    { id: 2, courseName: "ENG 1111", difficultly: "6.5/10", minYear: "1st", maxClassSize: 150, 
    dayOfWeek: ["Tuesday, ", "Friday"], time: "8:00 - 9:05", professorName: "Marino", selected: true },
    { id: 3, courseName: "THTR 2345", difficultly: "6.5/10", minYear: "1st", maxClassSize: 150,
    dayOfWeek: ["Monday", "Wednesday", "Thursday"], time: "9:15 - 10:20", professorName: "Dennis", selected: true }
  ]);

  const toggleSelectedCourse = (courseId) => {
    setListOfCourses(prevCourses => 
      prevCourses.map(course => 
        course.id === courseId ? { ...course, selected: !course.selected } : course
      )
    );
  };

  const DropdownMenu = () => {
    const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  
    const handleMouseEnter = () => {
      setIsDropdownOpen(true);
    };
  
    const handleMouseLeave = () => {
      setIsDropdownOpen(false);
    };

    for (let i = 0; i < listOfCourses.length; i++) {
      return (
        <div class="dropdown-container">
          <div class="text" onMouseEnter={handleMouseEnter} onMouseLeave={handleMouseLeave}>
          {listOfCourses.filter((course) => !course.selected).map((course) => (
            <ClassList
              key={course.id}
              course={course}
              toggleSelectedCourse={toggleSelectedCourse}
            />
          ))}
          </div>
          {isDropdownOpen && (
            HoverClassList()
          )}
        </div>
      );
    }
  };
  
    return (
      <div class = "App">
        <h1 class = "header">
          Class Recommendations
        </h1>
        <h2 class = "header">
          Helping you pick you classes based on peer reviews!
        </h2>
        <div class = "Middle">
          <div class = "ClassList">
            <div class = "Class-Name">
              <DropdownMenu />
            </div>
          </div>
          <div class = "Calender-Title">
            Your Schedule So Far
            <div class = "Calender">
              
              <Layout 

              />
            </div>
          </div>
        </div>
      </div>
    );
}

/*
{listOfCourses.filter((course) => !course.selected).map((course) => (
                <Layout
                  key={course.id}
                  course={course}
                  toggleSelectedCourse={toggleSelectedCourse}
                />
))}
*/

export default App;
