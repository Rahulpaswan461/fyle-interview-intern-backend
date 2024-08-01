from core.models.assignments import AssignmentStateEnum, GradeEnum

def test_list_all_assignments(client, h_principal):
    """Test listing all submitted and graded assignments"""
    response = client.get(
        '/principal/assignments',
        headers=h_principal
    )

    assert response.status_code == 200

    data = response.json['data']
    if data:  # Ensure there's data to assert on
        for assignment in data:
            assert assignment['state'] in [AssignmentStateEnum.SUBMITTED.value, AssignmentStateEnum.GRADED.value]
    else:
        assert len(data) == 0  # Handle case where no assignments are returned



def test_grade_assignment_draft_assignment(client, h_principal):
    """
    Failure case: If an assignment is in Draft state, it cannot be graded by the principal.
    """
    # Assume assignment with id 5 is in draft state
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 5,
            'grade': GradeEnum.A.value
        },
        headers=h_principal
    )

    assert response.status_code == 400
    assert response.json['error'] == "Assignment is in draft state and cannot be graded."



def test_grade_assignment(client, h_principal):
    """Test grading an assignment"""
    # Assume assignment with id 4 exists and is in submitted state
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 4,
            'grade': GradeEnum.C.value
        },
        headers=h_principal
    )

    assert response.status_code == 200

    data = response.json['data']
    assert data['state'] == AssignmentStateEnum.GRADED.value
    assert data['grade'] == GradeEnum.C.value

def test_regrade_assignment(client, h_principal):
    """Test re-grading an assignment"""
    # Assume assignment with id 4 exists and was previously graded
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 4,
            'grade': GradeEnum.B.value
        },
        headers=h_principal
    )

    assert response.status_code == 200

    data = response.json['data']
    assert data['state'] == AssignmentStateEnum.GRADED.value
    assert data['grade'] == GradeEnum.B.value
