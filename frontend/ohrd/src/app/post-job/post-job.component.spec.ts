import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PostJobComponent } from './post-job.component';

describe('PostJobComponent', () => {
  let component: PostJobComponent;
  let fixture: ComponentFixture<PostJobComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PostJobComponent]
    });
    fixture = TestBed.createComponent(PostJobComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
