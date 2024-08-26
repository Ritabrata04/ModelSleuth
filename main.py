import argparse
from analyzer import analyze_models

def main():
    parser = argparse.ArgumentParser(description="Analyze models in specified Python files.")
    parser.add_argument('files', type=str, nargs='+', help="Python files to analyze.")
    parser.add_argument('--output', type=str, help="Output file to save the model information.", default=None)
    
    args = parser.parse_args()
    
    models = analyze_models(args.files)
    
    if args.output:
        with open(args.output, 'w') as f:
            for model in models:
                f.write(f"Model {model['class_name']} (inherits from {model['base_class']}) found in {model['file']}\n")
                f.write("Methods: " + ", ".join(model['methods']) + "\n\n")
        print(f"Model information saved to {args.output}")
    else:
        for model in models:
            print(f"Model {model['class_name']} (inherits from {model['base_class']}) found in {model['file']}")
            print("Methods:", ", ".join(model['methods']))
            print()

if __name__ == "__main__":
    main()
