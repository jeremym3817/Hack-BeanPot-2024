import React, {useState} from 'react';
import { Card, CardContent, Grid, Typography } from '@mui/material'
import './ClassList.css'

const ClassList = ( {course, toggleSelectedCourse} ) => {
  const {id, courseName , difficultly, minYear, maxClassSize, dayOfWeek, time, professorName } = course;

  return (
    <div class = "container" onClick={() => {
      toggleSelectedCourse(id)
    }}>
      <Grid item>
        <Card>
          <CardContent>
            <Typography gutterBottom variant="h5" component="div">
              <div class="Class-Info">
                <p class = "Name-text">Course Name: {courseName}</p>
                <p class = "text">Difficultly: {difficultly}</p>
                <p class = "text">Minimum Year: {minYear}</p>
                <p class = "text">Max Class Size: {maxClassSize}</p>
                <p class = "text">Lecture Days: {dayOfWeek}</p>
                <p class = "text">Class Time: {time}</p>
                <p class = "text">Professor: {professorName}</p>
              </div>
            </Typography>
          </CardContent>
        </Card>
      </Grid>
    </div>
  );
}

export default ClassList;