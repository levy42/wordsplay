/**
 * Created by vitaliy on 14.06.16.
 */

function create_game() {
    value = document.getElementById("timeSelect").value;
    if (value == '') {
        value = 60
    }
    window.location = '/game/action?action=create&move_time=' + value;
}