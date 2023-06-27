import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-post-job',
  templateUrl: './post-job.component.html',
  styleUrls: ['./post-job.component.css']
})
export class PostJobComponent {

  jobData = {
    company_name: '',
    job_description: '',
    job_type: '',
    skills: '',
    reference_name: '',
    email: ''
  };


  constructor(private http: HttpClient, private router: Router) { }
  onSubmit() {
    const token = localStorage.getItem('token');
    const headers = new HttpHeaders().set('Authorization', `Token ${token}`);

    this.http.post('http://localhost:8000/api/jobs/', this.jobData, { headers }).subscribe(
      (response) => {
        console.log('Job created successfully', response);
        this.router.navigate(['/jobs']);


        // Handle the success response here
      },
      (error) => {
        console.error('Error creating job', error);
        // Handle the error response here
      }
    );
  }

}
