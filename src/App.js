import logo from './logo.svg';
import React, {useState} from 'react'
import './App.css';

import {AgGridReact} from 'ag-grid-react'

class ClassDate {
  constructor(name, time, day) {
    this.name = name;
    this.time = time;
    this.day = day;
  }
  render() {
    return <div>
      this.name + " " + this.time
    </div>;
  }

  
}

const DropdownMenu = () => {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  const handleMouseEnter = () => {
    setIsDropdownOpen(true);
  };

  const handleMouseLeave = () => {
    setIsDropdownOpen(false);
  };

  return (
    <div className="dropdown-container">
      <div className="text" onMouseEnter={handleMouseEnter} onMouseLeave={handleMouseLeave}>
        CS 2500 
      </div>
      {isDropdownOpen && (
        <div className="dropdown-content" onMouseEnter={handleMouseEnter} onMouseLeave={handleMouseLeave}>
          {/* Dropdown content */}
          <p>Difficultly: 6.5/10</p>
          <p>Year Taken: 1st-3rd Years</p>
          <p>Class Size: 150-170</p>
          <p>Class Times: 8:00-9:05, 9:15-10:20, 10:30-11:35</p>
          <p>Professors: Ferd, Arjun</p>
        </div>
      )}
    </div>
  );
};

function App() {


  function classDay() {
    return this.name + " " + this.time;
  }


  const eng = new ClassDate("ENG 1111", "8:00 - 9:05", "Sunday");
  const addClasses = () => {
    return (
      <div class = "Cal-Class-Name">
        ENG 1111  8:00 - 9:05
      </div>
    );
  }

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
          <div class = "Class">
            <div class = "Class-Name">
              <DropdownMenu />
            </div>
            <div class = "Class-Periods">
              3 periods availible
            </div>
          </div>
        </div>
        <div class = "Calender-Title">
          Your Schedule So Far
          <div class = "Calender">
            <div class = "Times">
              <div class = "Time">6 am</div>
              <div class = "Time">7 am</div>
              <div class = "Time">8 am</div>
              <div class = "Time">9 am</div>
              <div class = "Time">10 am</div>
              <div class = "Time">11 am</div>
              <div class = "Time">12 am</div>
              <div class = "Time">1 pm</div>
              <div class = "Time">2 pm</div>
              <div class = "Time">3 pm</div>
              <div class = "Time">4 pm</div>
              <div class = "Time">5 pm</div>
              <div class = "Time">6 pm</div>
            </div>
            <div class = "Dates">
              <div class = "Date">
                Sunday
              </div>
              <div class = "Date">
                Monday
                <div class = "Class-Block">
                  {addClasses()}
                </div>
                <div class = "Class-Block">
                  {addClasses()}
                </div>
              </div>
              <div class = "Date">
                Tuesday
              </div>
              <div class = "Date">
                Wednesday
                <div class = "Class-Block">
                  {addClasses()}
                </div>
              </div>
              <div class = "Date">
                Thursday
                <div class = "Class-Block">
                  {addClasses()}
                </div>
              </div>
              <div class = "Date">
                Friday
              </div>
              <div class = "Date">
                Saturday
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
