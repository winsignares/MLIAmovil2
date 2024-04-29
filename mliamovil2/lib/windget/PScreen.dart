import 'package:flutter/material.dart';

class HabitsForm extends StatefulWidget {
  @override
  _HabitsFormState createState() => _HabitsFormState();
}

class _HabitsFormState extends State<HabitsForm> {
  final TextEditingController cigarettesController = TextEditingController();
  final TextEditingController durationController = TextEditingController();
  final TextEditingController lungCancerController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Registrar Hábitos de Fumado'),
      ),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            TextField(
              controller: cigarettesController,
              keyboardType: TextInputType.number,
              decoration: InputDecoration(
                labelText: 'Cigarrillos por día',
              ),
            ),
            SizedBox(height: 16.0),
            TextField(
              controller: durationController,
              keyboardType: TextInputType.number,
              decoration: InputDecoration(
                labelText: 'Duración del hábito (años)',
              ),
            ),
            SizedBox(height: 16.0),
            TextField(
              controller: lungCancerController,
              decoration: InputDecoration(
                labelText: 'Cáncer de Pulmón (si/no)',
              ),
            ),
            SizedBox(height: 16.0),
            ElevatedButton(
              onPressed: () {
                // Aquí puedes enviar o guardar los datos ingresados
                String cigarettes = cigarettesController.text;
                String duration = durationController.text;
                String lungCancer = lungCancerController.text;

                print('Cigarrillos por día: $cigarettes');
                print('Duración del hábito: $duration');
                print('Cáncer de Pulmón: $lungCancer');
              },
              child: Text('Guardar'),
            ),
          ],
        ),
      ),
    );
  }
}
