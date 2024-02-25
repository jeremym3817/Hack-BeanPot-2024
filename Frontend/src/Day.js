import React from 'react';
import { Card, CardContent, Grid, Typography } from '@mui/material'

const Day = ({ dayOfWeek, courseName, time, professorName, thisDay }) => {
  for (let i = 0; i < dayOfWeek.length; i++) {
    if (thisDay == dayOfWeek[i]) {
      return (
      <Grid item>
        <Card>
          <CardContent>
            <Typography variant="body2" color="text.secondary">
              {courseName}<br />
              {time}, Professor {professorName}
            </Typography>
          </CardContent>
        </Card>
      </Grid> 
      );
    }
  }  
  return (
    null
  );
}

export default Day;