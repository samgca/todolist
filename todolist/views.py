from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NoteForm
from .models import Note


@login_required()
def create_note(request):
    if request.method == "POST":
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            note_form.save()
            return redirect('list_notes')
    else:
        note_form = NoteForm()
    return render(request, 'todolist/edit_note.html', {'note_form': note_form})


def list_notes(request):
    if request.user.is_authenticated():
        notes = Note.objects.all()
    else:
        notes = Note.objects.filter(status=False)
    return render(request, 'todolist/index.html', {'notes': notes})


@login_required()
def update_note(request, slug):
    note = get_object_or_404(Note, id=slug)
    if request.method == "POST":
        note_form = NoteForm(request.POST, instance=note)
        if note_form.is_valid():
            note_form.save()
            return redirect('list_notes')
    else:
        note_form = NoteForm(instance=note)
    return render(request, 'todolist/edit_note.html', {'note_form': note_form})


@login_required()
def delete_note(request, slug):
    note = get_object_or_404(Note, id=slug)
    note.delete()
    return redirect('list_notes')
