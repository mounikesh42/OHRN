import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { environment } from 'src/environments/environment';
@Component({
  selector: 'app-job-list',
  templateUrl: './job-list.component.html',
  styleUrls: ['./job-list.component.css']
})
export class JobListComponent implements OnInit {
  private apiUrl = environment.apiUrl;
  jobs!: any[];
  searchQuery!: string;

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.fetchJobs();
  }

  fetchJobs(): void {
    let params = new HttpParams();
    if (this.searchQuery) {
      params = params.set('search', this.searchQuery);
    }

    this.http.get<any>(`${this.apiUrl}/api/jobs`, { params }).subscribe(
      (response) => {
        this.jobs = response.results;
      },
      (error) => {
        console.error('Error fetching jobs:', error);
      }
    );
  }

  onSearch(query: string): void {
    this.searchQuery = query;
    this.fetchJobs();
  }
}
