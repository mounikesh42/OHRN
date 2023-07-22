import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent {
  private apiUrl = environment.apiUrl;


  registrationData: any = {
    first_name: '',
    last_name: '',
    email: '',
    password: '',
    confirm_password: '',
    phone_number: ''
  };

  constructor(private http: HttpClient, private router: Router) { }

  onSubmit() {
    const apiUrl = `${this.apiUrl}/api/auth/register/`;
    this.http.post(apiUrl, this.registrationData).subscribe(
      (response) => {
        console.log('Registration successful:', response);
        this.router.navigate(['/login']);

        // Perform any additional actions upon successful registration
      },
      (error) => {
        console.error('Registration failed:', error);
        // Handle any errors that occur during registration
      }
    );
  }
}
