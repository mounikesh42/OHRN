import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.css']
})
export class NavigationComponent {
  constructor(private http: HttpClient, private router: Router) { }

  ngOnInit() {
    const userData = localStorage.getItem('user');
    if (userData) {
      this.user = JSON.parse(userData);
    }
  }
  user: any; // Declare the 'user' property

  getUserFromLocalStorage() {
    const user = localStorage.getItem('user');
    if (user) {
      const gg= JSON.parse(user)
      console.log(gg.email)
      // If user data exists in localStorage, parse and return it
      return JSON.parse(user);
    }
    return null;
  }

  logout() {
    console.log('yess came')
    localStorage.removeItem('user');


    this.router.navigate(['/jobs']);

  }


  
}
