import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { NgForm } from '@angular/forms';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  constructor(private http: HttpClient, private router: Router) { }



  onSubmit(loginForm: NgForm) {
    const email = loginForm.value.username;
    const password = loginForm.value.password;

    const loginData = { email, password };
    console.log(loginData)
    this.http.post<any>('http://localhost:8000/api/auth/login/', loginData).subscribe(
      response => {
        // Save the token and user details
        const token = response.key;
        const user = response.detail;
        // console.log(user.first_name)
        // Save the token and user details in local storage
        localStorage.setItem('token', token);
        localStorage.setItem('user', JSON.stringify(user));
  
        // Redirect to the desired page (e.g., home page)
        this.router.navigate(['/jobs']);
      },
      error => {
        // Handle error response
        console.error('Login failed:', error);
      }
    );
  }
  
}
