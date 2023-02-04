using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class scenechanger : MonoBehaviour
{
    public void playGame()
    { SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex + 1); }

    public void Back()
    { SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex - 1); }

    public void Interview()
    { SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex +2); }

    public void InterBack()
    { SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex - 2); }

    public void Classroom()
    { SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex + 3 ); }

    public void ClassroomBack()
    { SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex - 3); }

    public void Date()
    { SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex + 4); }

    public void DateBack()
    { SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex - 4); }

    public void jkBack()
    { SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex - 5); }

    public void kBack()
    { SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex - 6); }

    public void dep()
    { SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex + 9); }

    public void depback()
    { SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex - 9); }

    public void sim()
    { SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex + 10); }


}
