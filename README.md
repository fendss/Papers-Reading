# Academic Literature Repository

A sophisticated web-based academic literature management system with advanced PDF reading capabilities, built for researchers and scholars.

## Features

### Core Functionality
- **Professional Interface Design**: Modern, responsive academic-grade interface with gradient backgrounds and glass-morphism effects
- **Intelligent Directory Management**: Automatic categorization of papers into academic domains
- **Advanced PDF Reader**: Full-featured PDF.js integration with text selection and rendering

### Advanced PDF Reading Experience
- **Text Selection & Highlighting**: Select text directly from PDFs with visual feedback
- **Smart Highlighting System**: Toggle highlighting mode with visual indicators
- **Bookmark Management**: Add contextual bookmarks and annotations
- **Persistent Storage**: All annotations are saved locally using browser storage
- **Annotation Panel**: Dedicated sidebar for managing bookmarks and highlights
- **Keyboard Shortcuts**: Full keyboard navigation support (Ctrl+H for highlighting, Ctrl+B for bookmarks, etc.)

### Document Management
- **Download Functionality**: Direct download of any paper from the interface
- **External Tool Integration**: Quick access to Adobe Acrobat, Zotero, and Mendeley
- **Multi-format Support**: Optimized for PDF documents with text layer extraction

### Responsive Design
- **Mobile-First Approach**: Fully responsive layout adapting to all screen sizes
- **Touch-Friendly Controls**: Optimized for tablet and mobile devices
- **Cross-Browser Compatibility**: Works seamlessly across modern browsers

## Directory Structure

```
Papers/
├── AutoML/           # Automated Machine Learning papers
├── Benchmark/        # Performance benchmarking studies
├── LLM4CO/          # Large Language Models for Combinatorial Optimization
├── AI4Science/       # AI for Scientific Discovery (formerly SOH forecasting)
├── Surveys/         # Comprehensive literature surveys
├── Security/        # AI security and safety research
├── Embodied/        # Embodied intelligence papers
├── index.html       # Main application interface
└── README.md        # This documentation
```

## Quick Start

### Local Development
1. **Clone or download** the repository to your local machine
2. **Navigate** to the project directory
3. **Start a local server** using Python:
   ```bash
   python -m http.server 8080
   ```
4. **Open your browser** and navigate to `http://localhost:8080`

### Alternative Server Options
- **Node.js**: `npx serve .`
- **PHP**: `php -S localhost:8080`
- **Live Server** (VS Code extension)

## Usage Guide

### Browsing Papers
1. **Expand categories** by clicking on category headers
2. **Select papers** by clicking on individual paper titles
3. **Download papers** using the download button next to each paper or in the reader

### PDF Reading Features
- **Zoom Controls**: Use +/- buttons or Ctrl+Plus/Ctrl+Minus
- **Page Navigation**: Arrow keys or Previous/Next buttons
- **Text Highlighting**: Enable highlight mode and select text
- **Bookmarks**: Add contextual bookmarks with custom notes
- **Annotations**: View all annotations in the dedicated panel

### Keyboard Shortcuts
- `Ctrl/Cmd + H`: Toggle highlighting mode
- `Ctrl/Cmd + B`: Toggle bookmark panel
- `Ctrl/Cmd + D`: Download current paper
- `Ctrl/Cmd + Plus`: Zoom in
- `Ctrl/Cmd + Minus`: Zoom out
- `Arrow Left/Right`: Navigate pages

### External Tools
Access professional PDF tools directly from the sidebar:
- **Adobe Acrobat**: Full PDF editing suite
- **Zotero**: Reference management
- **Mendeley**: Academic social network

## Technical Architecture

### Frontend Stack
- **HTML5**: Semantic markup with accessibility features
- **CSS3**: Modern styling with CSS Grid, Flexbox, and CSS variables
- **JavaScript ES6+**: Modern JavaScript with async/await
- **PDF.js**: Mozilla's PDF rendering engine
- **Font Awesome**: Professional iconography

### Key Technologies
- **PDF.js 3.11.174**: Latest stable PDF rendering
- **Local Storage API**: Persistent annotation storage
- **Responsive Design**: Mobile-first CSS approach
- **Progressive Enhancement**: Graceful degradation for older browsers

### GitHub Pages Deployment
This project is configured for GitHub Pages hosting:
1. **Ensure repository is public**
2. **Enable GitHub Pages** (Settings → Pages → Deploy from branch)
3. **Access your site** at: `https://[your-username].github.io/[repository-name]`
4. **Automatic deployment** via GitHub Actions on push to main branch

### Performance Optimizations
- **Lazy Loading**: Papers load on-demand
- **Efficient Rendering**: Optimized PDF page rendering
- **Memory Management**: Proper cleanup of PDF resources
- **Caching**: Browser caching for frequently accessed papers

## Customization

### Adding New Categories
1. Create a new folder in the root directory
2. Add PDF files to the folder
3. Update the `categories` object in `index.html`:
   ```javascript
   'NewCategory': { icon: 'fas fa-icon-name', description: 'Category description' }
   ```

### Styling Customization
- Modify CSS variables in the `<style>` section
- Adjust color schemes, fonts, and spacing
- Customize responsive breakpoints

### Feature Extensions
- Add new keyboard shortcuts in the keydown event listener
- Implement additional annotation types
- Integrate with external APIs or databases

## Browser Support

### Recommended Browsers
- **Chrome 90+**: Full feature support
- **Firefox 88+**: Excellent PDF.js compatibility
- **Safari 14+**: Good support with minor limitations
- **Edge 90+**: Full compatibility

### Mobile Support
- **iOS Safari**: Full touch support
- **Android Chrome**: Complete feature set
- **Mobile Firefox**: Good compatibility

## Troubleshooting

### Common Issues

#### PDF Not Loading
- **Check server**: Ensure local server is running
- **File paths**: Verify PDF files exist in correct directories
- **Browser cache**: Clear cache and hard refresh

#### Annotations Not Saving
- **Local storage**: Check browser local storage permissions
- **Quota exceeded**: Clear old annotations if storage is full
- **Private browsing**: Annotations don't persist in private mode

#### Performance Issues
- **Large PDFs**: Consider optimizing PDF file sizes
- **Memory usage**: Close unused browser tabs
- **Zoom levels**: Reset zoom to 100% for complex documents

### Debug Mode
Enable console logging by adding to browser console:
```javascript
localStorage.setItem('debugMode', 'true');
```

## Contributing

### Development Guidelines
1. **Code Style**: Follow modern JavaScript conventions
2. **Testing**: Test on multiple browsers and devices
3. **Documentation**: Update README for new features
4. **Performance**: Profile before and after changes

### Feature Requests
- Open issues for new feature suggestions
- Provide detailed use cases and examples
- Consider accessibility implications

## License

This project is open source and available under the MIT License. Feel free to use, modify, and distribute according to your needs.

## Acknowledgments

- **PDF.js Team**: Mozilla for the excellent PDF rendering engine
- **Font Awesome**: Professional icon set
- **Academic Community**: For inspiring this scholarly tool

## Support

For technical support or feature requests:
1. Check the troubleshooting section
2. Review browser console for errors
3. Test in a different browser
4. Ensure all PDF files are properly formatted

---

*Built with ❤️ for the academic research community*
