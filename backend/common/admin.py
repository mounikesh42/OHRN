from django.contrib import admin


class AuditModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.created_by = request.user
        obj.modified_by = request.user
        super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            if not instance.id:
                instance.created_by = request.user
            instance.modified_by = request.user
            instance.save()
        formset.save_m2m()