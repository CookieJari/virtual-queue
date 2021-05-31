import React from 'react'
import { Container, Grid, List, ListItem, ListItemText, Button } from '@material-ui/core'

const Confirmation = ({ prevStep, nextStep, values }) => {
  console.log(values);
  const { email, profile_picture, username, first_name, last_name, password, preferred_name, secondary_email, longitude, latitude,  is_active, is_staff, is_worker } = values
  const Continue = e => {
    e.preventDefault();
    nextStep();
  }

  const Previous = e => {
    e.preventDefault();
    prevStep();
  }

  return (
    <Container  component="main" maxWidth="xl">
      <div>
        <List>
          <ListItem>
            <ListItemText primary="Email" secondary={email}/>
          </ListItem>
          <ListItem>
            <ListItemText primary="Profile Picture" secondary={profile_picture}/>
          </ListItem>
          <ListItem>
            <ListItemText primary="Username" secondary={username}/>
          </ListItem>
          <ListItem>
            <ListItemText primary="First Name" secondary={first_name}/>
          </ListItem>
          <ListItem>
            <ListItemText primary="Last Name" secondary={last_name}/>
          </ListItem>
          <ListItem>
            <ListItemText primary="Preferred Name" secondary={preferred_name}/>
          </ListItem>
          <ListItem>
            <ListItemText primary="Secondary Email" secondary={secondary_email}/>
          </ListItem>
        </List>

        <br />
        <Grid container spacing={2}>
          <Grid item xs={12} sm={6}>
            <div className="formField">
              <button
                className="formFieldButton"
                onClick={ Previous }
                type="submit"
               >
                Previous
              </button>
            </div>
          </Grid>
          <Grid item xs={12} sm={6}>
            <div className="formField">
              <button
                className="formFieldButton"
                onClick={ Continue }
                type="submit"
               >
                Confirm & Continue
              </button>
            </div>
          </Grid>
        </Grid>
      </div>
    </Container>
  )
}

export default Confirmation