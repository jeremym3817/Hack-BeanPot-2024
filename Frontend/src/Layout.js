import React, {useState} from 'react';
import {Card, CardContent, Grid, Typography} from '@mui/material'
import Day from './Day.js';
import './Layout.css';


// {course, toggleSelectedCourse}
const Layout = (  ) => {

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

  /*
    const aCourse = { id: id.course, courseName: courseName.course, difficultly: difficultly.course, 
    minYear: minYear.course, maxClassSize: maxClassSize.course, dayOfWeek: dayOfWeek.course, 
    time: time.course, professorName: professorName.course };
  */

  return (
    <div className="Class-Cards">
      <span>
        <Grid container spacing={1} 
        className = "container">
        <Grid item>
            <Card>
              <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                  Sunday
                </Typography>
              </CardContent>
            </Card>
            {listOfCourses.map((day, index) => (
              <Day
                key={index}
                dayOfWeek={day.dayOfWeek}
                courseName={day.courseName}
                time={day.time}
                professorName={day.professorName}
                thisDay="Sunday"
              />
            ))}
          </Grid>
          <Grid item>
            <Card>
              <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                  Monday
                </Typography>
              </CardContent>
            </Card>
            {listOfCourses.map((day, index) => (
              <Day
                key={index}
                dayOfWeek={day.dayOfWeek}
                courseName={day.courseName}
                time={day.time}
                professorName={day.professorName}
                thisDay="Monday"
              />
            ))}
          </Grid>
          <Grid item>
            <Card>
              <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                  Tuesday
                </Typography>
              </CardContent>
            </Card>
            {listOfCourses.map((day, index) => (
              <Day
                key={index}
                dayOfWeek={day.dayOfWeek}
                courseName={day.courseName}
                time={day.time}
                professorName={day.professorName}
                thisDay="Tuesday"
              />
            ))}
          </Grid>
          <Grid item>
            <Card>
              <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                  Wednesday
                </Typography>
              </CardContent>
            </Card>
            {listOfCourses.map((day, index) => (
              <Day
                key={index}
                dayOfWeek={day.dayOfWeek}
                courseName={day.courseName}
                time={day.time}
                professorName={day.professorName}
                thisDay="Wednesday"
              />
            ))}
          </Grid>
          <Grid item>
            <Card>
              <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                  Thursday
                </Typography>
              </CardContent>
            </Card>
            {listOfCourses.map((day, index) => (
              <Day
                key={index}
                dayOfWeek={day.dayOfWeek}
                courseName={day.courseName}
                time={day.time}
                professorName={day.professorName}
                thisDay="Thursday"
              />
            ))}
          </Grid>
          <Grid item>
            <Card>
              <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                  Friday
                </Typography>
              </CardContent>
            </Card>
            {listOfCourses.map((day, index) => (
              <Day
                key={index}
                dayOfWeek={day.dayOfWeek}
                courseName={day.courseName}
                time={day.time}
                professorName={day.professorName}
                thisDay="Friday"
              />
            ))}
          </Grid>
          <Grid item>
            <Card>
              <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                  Saturday
                </Typography>
              </CardContent>
            </Card>
            {listOfCourses.map((day, index) => (
              <Day
                key={index}
                dayOfWeek={day.dayOfWeek}
                courseName={day.courseName}
                time={day.time}
                professorName={day.professorName}
                thisDay="Saturday"
              />
            ))}
          </Grid>
        </Grid>
        {/* Add more days as needed */}
      </span>
    </div>
  );
}

export default Layout;