import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { NgForm } from '@angular/forms';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient, private router: Router) { }



  onSubmit(loginForm: NgForm) {
    const email = loginForm.value.username;
    const password = loginForm.value.password;
  
    const loginData = { email, password };
    console.log(loginData)
    this.http.post<any>(`${this.apiUrl}/api/auth/login/`, loginData).subscribe(
      response => {
        // Check if the user is verified
        const user = response.detail;
        if (!user.verified) {
          // User is not verified, show an alert
          alert('You have not been verified yet. Please contact admin to verify ');
          return;
        }
  
        // User is verified, proceed with saving token and user details
        const token = response.key;
        // Save the token and user details in local storage
        localStorage.setItem('token', token);
        localStorage.setItem('user', JSON.stringify(user));
  
        // Redirect to the desired page (e.g., home page)
        this.router.navigate(['']);
      },
      error => {
        alert(error.error.non_field_errors)
        // Handle error response
        console.error('Login failed:', error);
      }
    );
  }
  
  
}
