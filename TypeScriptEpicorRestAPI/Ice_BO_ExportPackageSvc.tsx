import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.BO.ExportPackageSvc
// Description: This object is used to create and export an export package.
An export package contains a list of records that need to be exported and then
loaded to a customer's database. Examples of such records include BAQ, zDataset, etc.
// Version: v1



//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => application/json
   */  
export function getServiceDocument(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<JSON>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as JSON)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: Returns metadata document => content
   */  
export function get_metadata(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ExportPackage item
   Description: Calls GetByID to retrieve the ExportPackage item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExportPackage
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExportPackageRow
   */  
export function get_ExportPackages_PackageID(PackageID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ExportPackageRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_ExportPackageRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPBAQReport item
   Description: Calls GetByID to retrieve the EPBAQReport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPBAQReport1
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param BAQRptID Desc: BAQRptID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPBAQReportRow
   */  
export function get_ExportPackages_PackageID_EPBAQReports_PackageID_BAQRptID(PackageID:string, BAQRptID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPBAQReportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPBAQReports(" + PackageID + "," + BAQRptID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPBAQReportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPBpDirectiveGroup item
   Description: Calls GetByID to retrieve the EPBpDirectiveGroup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPBpDirectiveGroup1
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param DirectiveGroup Desc: DirectiveGroup   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPBpDirectiveGroupRow
   */  
export function get_ExportPackages_PackageID_EPBpDirectiveGroups_PackageID_DirectiveGroup(PackageID:string, DirectiveGroup:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPBpDirectiveGroupRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPBpDirectiveGroups(" + PackageID + "," + DirectiveGroup + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPBpDirectiveGroupRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPChgLogGA item
   Description: Calls GetByID to retrieve the EPChgLogGA item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPChgLogGA1
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AlertNum Desc: AlertNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPChgLogGARow
   */  
export function get_ExportPackages_PackageID_EPChgLogGAs_PackageID_Company_AlertNum(PackageID:string, Company:string, AlertNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPChgLogGARow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPChgLogGAs(" + PackageID + "," + Company + "," + AlertNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPChgLogGARow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPDashBdDef item
   Description: Calls GetByID to retrieve the EPDashBdDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPDashBdDef1
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProductID Desc: ProductID   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPDashBdDefRow
   */  
export function get_ExportPackages_PackageID_EPDashBdDefs_PackageID_Company_ProductID_DefinitionID(PackageID:string, Company:string, ProductID:string, DefinitionID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPDashBdDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPDashBdDefs(" + PackageID + "," + Company + "," + ProductID + "," + DefinitionID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPDashBdDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPEfxLibrary item
   Description: Calls GetByID to retrieve the EPEfxLibrary item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPEfxLibrary1
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param LibraryID Desc: LibraryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPEfxLibraryRow
   */  
export function get_ExportPackages_PackageID_EPEfxLibraries_PackageID_LibraryID(PackageID:string, LibraryID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPEfxLibraryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPEfxLibraries(" + PackageID + "," + LibraryID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPEfxLibraryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPExport item
   Description: Calls GetByID to retrieve the EPExport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPExport1
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Approved Desc: Approved   Required: True
      @param UserID Desc: UserID   Required: True   Allow empty value : True
      @param ExportID Desc: ExportID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPExportsRow
   */  
export function get_ExportPackages_PackageID_EPExports_PackageID_Company_Approved_UserID_ExportID(PackageID:string, Company:string, Approved:string, UserID:string, ExportID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPExportsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPExports(" + PackageID + "," + Company + "," + Approved + "," + UserID + "," + ExportID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPExportsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPFileContent item
   Description: Calls GetByID to retrieve the EPFileContent item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPFileContent1
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param SourcePath Desc: SourcePath   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPFileContentsRow
   */  
export function get_ExportPackages_PackageID_EPFileContents_PackageID_SourcePath(PackageID:string, SourcePath:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPFileContentsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPFileContents(" + PackageID + "," + SourcePath + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPFileContentsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPHistory item
   Description: Calls GetByID to retrieve the EPHistory item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPHistory1
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param ActionNum Desc: ActionNum   Required: True
      @param ActionDate Desc: ActionDate   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPHistoryRow
   */  
export function get_ExportPackages_PackageID_EPHistories_PackageID_ActionNum_ActionDate(PackageID:string, ActionNum:string, ActionDate:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPHistoryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPHistories(" + PackageID + "," + ActionNum + "," + ActionDate + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPHistoryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPMenu item
   Description: Calls GetByID to retrieve the EPMenu item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPMenu1
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param MenuID Desc: MenuID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPMenuRow
   */  
export function get_ExportPackages_PackageID_EPMenus_PackageID_MenuID(PackageID:string, MenuID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPMenuRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPMenus(" + PackageID + "," + MenuID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPMenuRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPQuickSearch item
   Description: Calls GetByID to retrieve the EPQuickSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPQuickSearch1
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param QuickSearchID Desc: QuickSearchID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPQuickSearchRow
   */  
export function get_ExportPackages_PackageID_EPQuickSearches_PackageID_Company_GlbCompany_QuickSearchID(PackageID:string, Company:string, GlbCompany:string, QuickSearchID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPQuickSearchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPQuickSearches(" + PackageID + "," + Company + "," + GlbCompany + "," + QuickSearchID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPQuickSearchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPReport item
   Description: Calls GetByID to retrieve the EPReport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPReport1
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPReportRow
   */  
export function get_ExportPackages_PackageID_EPReports_PackageID_ReportID(PackageID:string, ReportID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPReportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPReports(" + PackageID + "," + ReportID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPReportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPReportStyle item
   Description: Calls GetByID to retrieve the EPReportStyle item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPReportStyle1
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param StyleNum Desc: StyleNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPReportStyleRow
   */  
export function get_ExportPackages_PackageID_EPReportStyles_PackageID_ReportID_StyleNum(PackageID:string, ReportID:string, StyleNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPReportStyleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPReportStyles(" + PackageID + "," + ReportID + "," + StyleNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPReportStyleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPRptDataDef item
   Description: Calls GetByID to retrieve the EPRptDataDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPRptDataDef1
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPRptDataDefRow
   */  
export function get_ExportPackages_PackageID_EPRptDataDefs_PackageID_RptDefID(PackageID:string, RptDefID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPRptDataDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPRptDataDefs(" + PackageID + "," + RptDefID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPRptDataDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPSecurity item
   Description: Calls GetByID to retrieve the EPSecurity item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPSecurity1
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SecCode Desc: SecCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPSecurityRow
   */  
export function get_ExportPackages_PackageID_EPSecurities_PackageID_Company_SecCode(PackageID:string, Company:string, SecCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPSecurityRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPSecurities(" + PackageID + "," + Company + "," + SecCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPSecurityRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPUDCodeType item
   Description: Calls GetByID to retrieve the EPUDCodeType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPUDCodeType1
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CodeTypeID Desc: CodeTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPUDCodeTypeRow
   */  
export function get_ExportPackages_PackageID_EPUDCodeTypes_PackageID_Company_CodeTypeID(PackageID:string, Company:string, CodeTypeID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPUDCodeTypeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPUDCodeTypes(" + PackageID + "," + Company + "," + CodeTypeID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPUDCodeTypeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPUserDefinedTable item
   Description: Calls GetByID to retrieve the EPUserDefinedTable item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPUserDefinedTable1
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPUserDefinedTableRow
   */  
export function get_ExportPackages_PackageID_EPUserDefinedTables_PackageID_TableName(PackageID:string, TableName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPUserDefinedTableRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPUserDefinedTables(" + PackageID + "," + TableName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPUserDefinedTableRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPXXXDef item
   Description: Calls GetByID to retrieve the EPXXXDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPXXXDef1
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProductID Desc: ProductID   Required: True   Allow empty value : True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPXXXDefRow
   */  
export function get_ExportPackages_PackageID_EPXXXDefs_PackageID_Company_ProductID_TypeCode_Key1_Key2_Key3(PackageID:string, Company:string, ProductID:string, TypeCode:string, Key1:string, Key2:string, Key3:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPXXXDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPXXXDefs(" + PackageID + "," + Company + "," + ProductID + "," + TypeCode + "," + Key1 + "," + Key2 + "," + Key3 + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPXXXDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPzBODef item
   Description: Calls GetByID to retrieve the EPzBODef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPzBODef1
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param ClassName Desc: ClassName   Required: True   Allow empty value : True
      @param ObjectNS Desc: ObjectNS   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPzBODefRow
   */  
export function get_ExportPackages_PackageID_EPzBODefs_PackageID_ClassName_ObjectNS(PackageID:string, ClassName:string, ObjectNS:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPzBODefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPzBODefs(" + PackageID + "," + ClassName + "," + ObjectNS + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPzBODefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPzData item
   Description: Calls GetByID to retrieve the EPzData item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPzData1
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPzDataRow
   */  
export function get_ExportPackages_PackageID_EPzDatas_PackageID_DataTableID(PackageID:string, DataTableID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPzDataRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPzDatas(" + PackageID + "," + DataTableID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPzDataRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPBAQReport item
   Description: Calls GetByID to retrieve the EPBAQReport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPBAQReport
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param BAQRptID Desc: BAQRptID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPBAQReportRow
   */  
export function get_EPBAQReports_PackageID_BAQRptID(PackageID:string, BAQRptID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPBAQReportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPBAQReports(" + PackageID + "," + BAQRptID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPBAQReportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPBpDirectiveGroup item
   Description: Calls GetByID to retrieve the EPBpDirectiveGroup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPBpDirectiveGroup
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param DirectiveGroup Desc: DirectiveGroup   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPBpDirectiveGroupRow
   */  
export function get_EPBpDirectiveGroups_PackageID_DirectiveGroup(PackageID:string, DirectiveGroup:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPBpDirectiveGroupRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPBpDirectiveGroups(" + PackageID + "," + DirectiveGroup + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPBpDirectiveGroupRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPChgLogGA item
   Description: Calls GetByID to retrieve the EPChgLogGA item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPChgLogGA
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AlertNum Desc: AlertNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPChgLogGARow
   */  
export function get_EPChgLogGAs_PackageID_Company_AlertNum(PackageID:string, Company:string, AlertNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPChgLogGARow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPChgLogGAs(" + PackageID + "," + Company + "," + AlertNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPChgLogGARow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPDashBdDef item
   Description: Calls GetByID to retrieve the EPDashBdDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPDashBdDef
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProductID Desc: ProductID   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPDashBdDefRow
   */  
export function get_EPDashBdDefs_PackageID_Company_ProductID_DefinitionID(PackageID:string, Company:string, ProductID:string, DefinitionID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPDashBdDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPDashBdDefs(" + PackageID + "," + Company + "," + ProductID + "," + DefinitionID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPDashBdDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPEfxLibrary item
   Description: Calls GetByID to retrieve the EPEfxLibrary item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPEfxLibrary
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param LibraryID Desc: LibraryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPEfxLibraryRow
   */  
export function get_EPEfxLibraries_PackageID_LibraryID(PackageID:string, LibraryID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPEfxLibraryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPEfxLibraries(" + PackageID + "," + LibraryID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPEfxLibraryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPExport item
   Description: Calls GetByID to retrieve the EPExport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPExport
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Approved Desc: Approved   Required: True
      @param UserID Desc: UserID   Required: True   Allow empty value : True
      @param ExportID Desc: ExportID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPExportsRow
   */  
export function get_EPExports_PackageID_Company_Approved_UserID_ExportID(PackageID:string, Company:string, Approved:string, UserID:string, ExportID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPExportsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPExports(" + PackageID + "," + Company + "," + Approved + "," + UserID + "," + ExportID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPExportsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPFileContent item
   Description: Calls GetByID to retrieve the EPFileContent item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPFileContent
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param SourcePath Desc: SourcePath   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPFileContentsRow
   */  
export function get_EPFileContents_PackageID_SourcePath(PackageID:string, SourcePath:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPFileContentsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPFileContents(" + PackageID + "," + SourcePath + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPFileContentsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPHistory item
   Description: Calls GetByID to retrieve the EPHistory item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPHistory
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param ActionNum Desc: ActionNum   Required: True
      @param ActionDate Desc: ActionDate   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPHistoryRow
   */  
export function get_EPHistories_PackageID_ActionNum_ActionDate(PackageID:string, ActionNum:string, ActionDate:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPHistoryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPHistories(" + PackageID + "," + ActionNum + "," + ActionDate + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPHistoryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPMenu item
   Description: Calls GetByID to retrieve the EPMenu item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPMenu
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param MenuID Desc: MenuID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPMenuRow
   */  
export function get_EPMenus_PackageID_MenuID(PackageID:string, MenuID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPMenuRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPMenus(" + PackageID + "," + MenuID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPMenuRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPQuickSearch item
   Description: Calls GetByID to retrieve the EPQuickSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPQuickSearch
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param QuickSearchID Desc: QuickSearchID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPQuickSearchRow
   */  
export function get_EPQuickSearches_PackageID_Company_GlbCompany_QuickSearchID(PackageID:string, Company:string, GlbCompany:string, QuickSearchID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPQuickSearchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPQuickSearches(" + PackageID + "," + Company + "," + GlbCompany + "," + QuickSearchID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPQuickSearchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPReport item
   Description: Calls GetByID to retrieve the EPReport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPReport
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPReportRow
   */  
export function get_EPReports_PackageID_ReportID(PackageID:string, ReportID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPReportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPReports(" + PackageID + "," + ReportID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPReportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPReportStyle item
   Description: Calls GetByID to retrieve the EPReportStyle item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPReportStyle
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param StyleNum Desc: StyleNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPReportStyleRow
   */  
export function get_EPReportStyles_PackageID_ReportID_StyleNum(PackageID:string, ReportID:string, StyleNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPReportStyleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPReportStyles(" + PackageID + "," + ReportID + "," + StyleNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPReportStyleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPRptDataDef item
   Description: Calls GetByID to retrieve the EPRptDataDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPRptDataDef
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPRptDataDefRow
   */  
export function get_EPRptDataDefs_PackageID_RptDefID(PackageID:string, RptDefID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPRptDataDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPRptDataDefs(" + PackageID + "," + RptDefID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPRptDataDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPSecurity item
   Description: Calls GetByID to retrieve the EPSecurity item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPSecurity
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SecCode Desc: SecCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPSecurityRow
   */  
export function get_EPSecurities_PackageID_Company_SecCode(PackageID:string, Company:string, SecCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPSecurityRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPSecurities(" + PackageID + "," + Company + "," + SecCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPSecurityRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPUDCodeType item
   Description: Calls GetByID to retrieve the EPUDCodeType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPUDCodeType
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CodeTypeID Desc: CodeTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPUDCodeTypeRow
   */  
export function get_EPUDCodeTypes_PackageID_Company_CodeTypeID(PackageID:string, Company:string, CodeTypeID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPUDCodeTypeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPUDCodeTypes(" + PackageID + "," + Company + "," + CodeTypeID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPUDCodeTypeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPUserDefinedTable item
   Description: Calls GetByID to retrieve the EPUserDefinedTable item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPUserDefinedTable
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPUserDefinedTableRow
   */  
export function get_EPUserDefinedTables_PackageID_TableName(PackageID:string, TableName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPUserDefinedTableRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPUserDefinedTables(" + PackageID + "," + TableName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPUserDefinedTableRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPXXXDef item
   Description: Calls GetByID to retrieve the EPXXXDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPXXXDef
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProductID Desc: ProductID   Required: True   Allow empty value : True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPXXXDefRow
   */  
export function get_EPXXXDefs_PackageID_Company_ProductID_TypeCode_Key1_Key2_Key3(PackageID:string, Company:string, ProductID:string, TypeCode:string, Key1:string, Key2:string, Key3:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPXXXDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPXXXDefs(" + PackageID + "," + Company + "," + ProductID + "," + TypeCode + "," + Key1 + "," + Key2 + "," + Key3 + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPXXXDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPzBODef item
   Description: Calls GetByID to retrieve the EPzBODef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPzBODef
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param ClassName Desc: ClassName   Required: True   Allow empty value : True
      @param ObjectNS Desc: ObjectNS   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPzBODefRow
   */  
export function get_EPzBODefs_PackageID_ClassName_ObjectNS(PackageID:string, ClassName:string, ObjectNS:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPzBODefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPzBODefs(" + PackageID + "," + ClassName + "," + ObjectNS + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPzBODefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPzData item
   Description: Calls GetByID to retrieve the EPzData item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPzData
      @param PackageID Desc: PackageID   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPzDataRow
   */  
export function get_EPzDatas_PackageID_DataTableID(PackageID:string, DataTableID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPzDataRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPzDatas(" + PackageID + "," + DataTableID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPzDataRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPExtensionSet item
   Description: Calls GetByID to retrieve the EPExtensionSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPExtensionSet
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPExtensionSetRow
   */  
export function get_EPExtensionSets_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPExtensionSetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPExtensionSets(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPExtensionSetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPSolutionDetail item
   Description: Calls GetByID to retrieve the EPSolutionDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPSolutionDetail
      @param SolutionID Desc: SolutionID   Required: True   Allow empty value : True
      @param ForeignSysRowID Desc: ForeignSysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPSolutionDetailRow
   */  
export function get_EPSolutionDetails_SolutionID_ForeignSysRowID(SolutionID:string, ForeignSysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPSolutionDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPSolutionDetails(" + SolutionID + "," + ForeignSysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPSolutionDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPSolutionDetailDisplay item
   Description: Calls GetByID to retrieve the EPSolutionDetailDisplay item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPSolutionDetailDisplay
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPSolutionDetailDisplayRow
   */  
export function get_EPSolutionDetailDisplays_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPSolutionDetailDisplayRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPSolutionDetailDisplays(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPSolutionDetailDisplayRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPSolutionHeader item
   Description: Calls GetByID to retrieve the EPSolutionHeader item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPSolutionHeader
      @param SolutionID Desc: SolutionID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPSolutionHeaderRow
   */  
export function get_EPSolutionHeaders_SolutionID(SolutionID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPSolutionHeaderRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPSolutionHeaders(" + SolutionID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPSolutionHeaderRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPSolutionPackage item
   Description: Calls GetByID to retrieve the EPSolutionPackage item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPSolutionPackage
      @param SolutionID Desc: SolutionID   Required: True   Allow empty value : True
      @param ForeignSysRowID Desc: ForeignSysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPSolutionPackageRow
   */  
export function get_EPSolutionPackages_SolutionID_ForeignSysRowID(SolutionID:string, ForeignSysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPSolutionPackageRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPSolutionPackages(" + SolutionID + "," + ForeignSysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPSolutionPackageRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPSolutionTracker item
   Description: Calls GetByID to retrieve the EPSolutionTracker item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPSolutionTracker
      @param SolutionID Desc: SolutionID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param LastUpdated Desc: LastUpdated   Required: True   Allow empty value : True
      @param ForeignSysRowID Desc: ForeignSysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPSolutionTrackerRow
   */  
export function get_EPSolutionTrackers_SolutionID_TableName_LastUpdated_ForeignSysRowID(SolutionID:string, TableName:string, LastUpdated:string, ForeignSysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPSolutionTrackerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPSolutionTrackers(" + SolutionID + "," + TableName + "," + LastUpdated + "," + ForeignSysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPSolutionTrackerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPSolutionTrackerDetail item
   Description: Calls GetByID to retrieve the EPSolutionTrackerDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPSolutionTrackerDetail
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPSolutionTrackerDetailRow
   */  
export function get_EPSolutionTrackerDetails_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPSolutionTrackerDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPSolutionTrackerDetails(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPSolutionTrackerDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPSolutionType item
   Description: Calls GetByID to retrieve the EPSolutionType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPSolutionType
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPSolutionTypeRow
   */  
export function get_EPSolutionTypes_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPSolutionTypeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPSolutionTypes(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPSolutionTypeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EPStructuredReport item
   Description: Calls GetByID to retrieve the EPStructuredReport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPStructuredReport
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPStructuredReportRow
   */  
export function get_EPStructuredReports_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_EPStructuredReportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPStructuredReports(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_EPStructuredReportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExportPackageListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExportPackageListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExportPackageListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method GetByID
   Description: This method returns a dataset representing an ExportPackage
   OperationID: GetByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExportPackageListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/GetByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExportPackageListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetList
   Description: This method returns a list of solutions
   OperationID: GetList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/GetList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method HasUnsupportedContentTypes
   Description: Has solution files invalid/unsupported content types.
   OperationID: HasUnsupportedContentTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HasUnsupportedContentTypes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HasUnsupportedContentTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HasUnsupportedContentTypes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/HasUnsupportedContentTypes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewEPFileContents
   Description: This method creates a EPFileContents row
   OperationID: GetNewEPFileContents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEPFileContents_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEPFileContents_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEPFileContents(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/GetNewEPFileContents", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewEPHistory
   Description: This method creates a EPHistory row
   OperationID: GetNewEPHistory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEPHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEPHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEPHistory(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/GetNewEPHistory", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewExportPackage
   Description: This method creates a new Export package
   OperationID: GetNewExportPackage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExportPackage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExportPackage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewExportPackage(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/GetNewExportPackage", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Update
   Description: Update
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RemoveWorkbenchPromoteDetailRows
   Description: Removes deleted rows from the SolutionDetail table
   OperationID: RemoveWorkbenchPromoteDetailRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveWorkbenchPromoteDetailRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveWorkbenchPromoteDetailRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemoveWorkbenchPromoteDetailRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/RemoveWorkbenchPromoteDetailRows", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RemoveWorkbenchTrackerDetailRows
   Description: Selects or Removes the row in the SoltutionTracker table
   OperationID: RemoveWorkbenchTrackerDetailRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveWorkbenchTrackerDetailRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveWorkbenchTrackerDetailRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemoveWorkbenchTrackerDetailRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/RemoveWorkbenchTrackerDetailRows", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PopulateWorkbenchTrackerDetailPanel
   Description: Populates the detail view in the WorkbenchTrackerDetailPanel
   OperationID: PopulateWorkbenchTrackerDetailPanel
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PopulateWorkbenchTrackerDetailPanel_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PopulateWorkbenchTrackerDetailPanel_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PopulateWorkbenchTrackerDetailPanel(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/PopulateWorkbenchTrackerDetailPanel", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteByID
   Description: Deletes the Solution
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PopulateWorkbenchPromoteDetailPanel
   Description: Populates the detail view in the WorkbenchPromoteDetailPanel
   OperationID: PopulateWorkbenchPromoteDetailPanel
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PopulateWorkbenchPromoteDetailPanel_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PopulateWorkbenchPromoteDetailPanel_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PopulateWorkbenchPromoteDetailPanel(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/PopulateWorkbenchPromoteDetailPanel", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsValidBORecByID
   Description: validates the imported row
   OperationID: IsValidBORecByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsValidBORecByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsValidBORecByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsValidBORecByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/IsValidBORecByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBORecByID
   Description: Gets the row to export
   OperationID: GetBORecByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBORecByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBORecByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBORecByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/GetBORecByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateMenuModuleType
   Description: update the Module for the Menu row
   OperationID: UpdateMenuModuleType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateMenuModuleType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateMenuModuleType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateMenuModuleType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/UpdateMenuModuleType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateDBScript
   Description: updates the database script in the SolutionScriptStore
   OperationID: UpdateDBScript
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateDBScript_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateDBScript_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateDBScript(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/UpdateDBScript", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteSolutionDBScripts
   Description: deletes the database script in the SolutionScriptStore for the solution and company
   OperationID: DeleteSolutionDBScripts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteSolutionDBScripts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteSolutionDBScripts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteSolutionDBScripts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/DeleteSolutionDBScripts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetElementBOName
   Description: returns the BO associated with the Solution Element
   OperationID: GetElementBOName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetElementBOName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetElementBOName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetElementBOName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/GetElementBOName", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetExportRow
   Description: Gets the row to export
   OperationID: GetExportRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetExportRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExportRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetExportRow(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/GetExportRow", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MoveTrackedRowsToSolution
   Description: Move Tracked Selected rows to the Solution
   OperationID: MoveTrackedRowsToSolution
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveTrackedRowsToSolution_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveTrackedRowsToSolution_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MoveTrackedRowsToSolution(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/MoveTrackedRowsToSolution", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AddItemToSolution
   Description: Add rows (non-tracked) to the Solution
   OperationID: AddItemToSolution
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddItemToSolution_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddItemToSolution_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddItemToSolution(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/AddItemToSolution", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateSolutionType
   Description: Validates the Solution Type ID
   OperationID: ValidateSolutionType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSolutionType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSolutionType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSolutionType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ValidateSolutionType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInstalledSolution
   Description: Get the previous install of a solution.
   OperationID: GetInstalledSolution
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInstalledSolution_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInstalledSolution_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInstalledSolution(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/GetInstalledSolution", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteSolutionInstall
   Description: Delete the last record of a solution installation.
   OperationID: DeleteSolutionInstall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteSolutionInstall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteSolutionInstall_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteSolutionInstall(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/DeleteSolutionInstall", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RecordSolutionInstall
   Description: Record the fact that we're installing a solution.
   OperationID: RecordSolutionInstall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecordSolutionInstall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecordSolutionInstall_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RecordSolutionInstall(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/RecordSolutionInstall", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInstalledSolutions
   Description: Get the list of installed solutions.
   OperationID: GetInstalledSolutions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInstalledSolutions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInstalledSolutions(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/GetInstalledSolutions", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSolutionHistory
   Description: Get the history of a solution.
   OperationID: GetSolutionHistory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSolutionHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSolutionHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSolutionHistory(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/GetSolutionHistory", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Build
   Description: Build solution package.
   OperationID: Build
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Build_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Build_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Build(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/Build", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBuildSettings
   Description: Gets build settings.
   OperationID: GetBuildSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBuildSettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBuildSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBuildSettings(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/GetBuildSettings", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateBuildSettings
   Description: Validate build settings.
   OperationID: ValidateBuildSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateBuildSettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateBuildSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateBuildSettings(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ValidateBuildSettings", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInstallSettings
   Description: Get install settings.
   OperationID: GetInstallSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInstallSettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInstallSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInstallSettings(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/GetInstallSettings", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateInstallSettings
   Description: Validate install settings.
   OperationID: ValidateInstallSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateInstallSettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateInstallSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateInstallSettings(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ValidateInstallSettings", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Install
   Description: Install solution.
   OperationID: Install
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Install_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Install_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Install(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/Install", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Delete
   Description: Delete solution.
   OperationID: Delete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Delete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Delete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Delete(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/Delete", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExportPackageListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ExportPackageListRow[],
}

export interface Ice_Tablesets_EPBAQReportRow{
      /**  BAQ Report ID, the unique identifier for this report within the company  */  
   "BAQRptID":string,
      /**  Indicating if this record is selected in the export package  */  
   "Selected":boolean,
   "PackageID":string,
      /**  Description  */  
   "Description":string,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_EPBpDirectiveGroupRow{
   "DirectiveGroup":string,
   "DirectiveCount":number,
   "PackageID":string,
   "Selected":boolean,
   "Description":string,
      /**  Country Group / Country Code for CSF  */  
   "CGCCode":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_EPChgLogGARow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The unique Alert Num of the record.  The AlertNum should be greater than or equal to 2000 to avoid conflicts with standard global alerts.  */  
   "AlertNum":number,
   "Selected":boolean,
   "PackageID":string,
      /**  The description of the alert/change log  */  
   "Description":string,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_EPDashBdDefRow{
   "PackageID":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  VN - Vantage, VS - Vista  */  
   "ProductID":string,
   "DefinitionID":string,
   "Selected":boolean,
   "Description":string,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_EPEfxLibraryRow{
   "PackageID":string,
      /**  ID of Epicor Functions Library  */  
   "LibraryID":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_EPExportsRow{
   "PackageID":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**   no = this exports is a work-in-process one
Since 9.0 there should be only approved BAQs.  */  
   "Approved":boolean,
      /**  The userid of the user who created the export.  */  
   "UserID":string,
      /**  The unique export identifier.  */  
   "ExportID":string,
   "Selected":boolean,
      /**  Description  */  
   "Description":string,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_EPExtensionSetRow{
   "ExtensionSetID":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_EPFileContentsRow{
      /**  Export Package ID  */  
   "PackageID":string,
      /**  Source Path  */  
   "SourcePath":string,
      /**  File Content Type  */  
   "FileContentType":number,
      /**  Description  */  
   "Description":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RunSequence  */  
   "RunSequence":number,
      /**  Notes  */  
   "Notes":string,
   "CabFolder":string,
   "Selected":boolean,
   "SourceFilename":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_EPHistoryRow{
      /**  Export Package ID  */  
   "PackageID":string,
      /**  Action Number  */  
   "ActionNum":number,
      /**  User ID  */  
   "UserID":string,
      /**  Action Date  */  
   "ActionDate":string,
      /**  Description  */  
   "Description":string,
   "Selected":boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_EPMenuRow{
   "PackageID":string,
      /**  MM=module, XX=MN,UP,LS,PC, and ZZZZ = number.  */  
   "MenuID":string,
   "Selected":boolean,
   "Description":string,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_EPQuickSearchRow{
      /**  Company Identifier. If blank then this quick search is for all companies.  */  
   "Company":string,
   "GlbCompany":string,
      /**  The unique identifier for this quick search  */  
   "QuickSearchID":string,
      /**  Indicating if this record is selected in the export package  */  
   "Selected":boolean,
   "PackageID":string,
      /**  Description  */  
   "Description":string,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_EPReportRow{
   "PackageID":string,
   "ReportID":string,
   "Selected":boolean,
   "Description":string,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_EPReportStyleRow{
   "CGCCode":string,
   "Description":string,
   "PackageID":string,
   "ReportID":string,
   "Selected":boolean,
   "StyleNum":number,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_EPRptDataDefRow{
   "PackageID":string,
   "RptDefID":string,
   "Selected":boolean,
   "Description":string,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_EPSecurityRow{
   "PackageID":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Security ID for the Program/SubMenu.  Format is either "XXX999-888" or "XXX999-888", where XXX is either SEC or UD (User Defined), 999 is a number to make the code unique, and -888 is a number used to make a subcomponent unique.  Subcomponents are used to allow more restricted access to a piece of a menu item(program).  For example: Costing information in Job Tracker.  */  
   "SecCode":string,
   "Selected":boolean,
   "Description":string,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_EPSolutionDetailDisplayRow{
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_EPSolutionDetailRow{
      /**  SolutionID  */  
   "SolutionID":string,
      /**  ForeignSysRowID  */  
   "ForeignSysRowID":string,
      /**  TableName  */  
   "TableName":string,
      /**  LastUpdatedBy  */  
   "LastUpdatedBy":string,
      /**  LastUpdated  */  
   "LastUpdated":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "Elements":string,
   "PackageID":string,
   "Selected":number,
   "SolutionTypeID":string,
   "InstallationOrder":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_EPSolutionHeaderRow{
      /**  SolutionID  */  
   "SolutionID":string,
      /**  Company  */  
   "Company":string,
      /**  Description  */  
   "Description":string,
      /**  AppVersion  */  
   "AppVersion":string,
      /**  InternalNotes  */  
   "InternalNotes":string,
      /**  Notes  */  
   "Notes":string,
      /**  LastExported  */  
   "LastExported":string,
      /**  CreatedBy  */  
   "CreatedBy":string,
      /**  CreateDate  */  
   "CreateDate":string,
      /**  SolutionTypeID  */  
   "SolutionTypeID":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  BuildIteration  */  
   "BuildIteration":number,
      /**  SolutionReference  */  
   "SolutionReference":string,
      /**  MinAppVersion  */  
   "MinAppVersion":number,
      /**  ImportSameRelease  */  
   "ImportSameRelease":boolean,
   "PackageID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_EPSolutionPackageRow{
      /**  SolutionID  */  
   "SolutionID":string,
      /**  ForeignSysRowID  */  
   "ForeignSysRowID":string,
      /**  TableName  */  
   "TableName":string,
      /**  LastUpdatedBy  */  
   "LastUpdatedBy":string,
      /**  LastUpdated  */  
   "LastUpdated":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_EPSolutionTrackerDetailRow{
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_EPSolutionTrackerRow{
      /**  SolutionID  */  
   "SolutionID":string,
      /**  TableName  */  
   "TableName":string,
      /**  LastUpdated  */  
   "LastUpdated":string,
      /**  ForeignSysRowID  */  
   "ForeignSysRowID":string,
      /**  LastUpdatedBy  */  
   "LastUpdatedBy":string,
      /**  IsSelected  */  
   "IsSelected":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "Available":number,
   "Elements":string,
   "PackageID":string,
   "Selected":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_EPSolutionTypeRow{
   "SolutionID":string,
   "Company":string,
   "SolutionTypeID":string,
   "ElementHeaderID":string,
   "ParentTableName":string,
   "BusinessObject":string,
   "BOMethod":string,
   "ChildTableName":string,
   "ElementDisplayColumnID":number,
   "ParentColumnName":string,
   "DataType":string,
   "ParameterName":string,
   "ParameterOrder":number,
   "ParameterDataType":string,
   "PackageID":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_EPStructuredReportRow{
   "ReportID":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_EPUDCodeTypeRow{
      /**  Company Identifier.  */  
   "Company":string,
   "CodeTypeID":string,
   "PackageID":string,
   "Selected":boolean,
   "Description":string,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_EPUserDefinedTableRow{
      /**  EP Package ID  */  
   "PackageID":string,
      /**  Table Name  */  
   "TableName":string,
      /**  Selection flag  */  
   "Selected":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_EPXXXDefRow{
   "PackageID":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  VN - Vantage, VS - Vista  */  
   "ProductID":string,
      /**  Ex: Customization, Personalization  */  
   "TypeCode":string,
      /**   Generic key component field.
Ex: Customization Name if TypeCode =  "Customization" 
FormName if TypeCode = "Personalization"  */  
   "Key1":string,
      /**   Generic key component field.
Ex: FormName Name if TypeCode =  "Customization" 
UserID if TypeCode = "Personalization"  */  
   "Key2":string,
      /**   Generic key component field.  
Ex: if TypeCode =  "Customization"  this may contain "WIP" or blanks.  */  
   "Key3":string,
   "Selected":boolean,
   "Description":string,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_EPzBODefRow{
   "PackageID":string,
   "ClassName":string,
   "ObjectNS":string,
   "Selected":boolean,
   "Description":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_EPzDataRow{
   "PackageID":string,
   "DataTableID":string,
   "Selected":boolean,
   "Description":string,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ExportPackageListRow{
   "PackageID":string,
   "Description":string,
   "AppVersion":string,
   "CreateDate":string,
   "CreatedBy":string,
   "LastExported":string,
   "Notes":string,
   "InternalNotes":string,
      /**  Solution Type  */  
   "Type":string,
      /**  Country Group / Country Code for CSF  */  
   "CGCCode":string,
   "Company":string,
   "SolutionID":string,
   "SolutionTypeID":string,
   "SolutionVersion":string,
   "SolutionReference":string,
   "BuildIteration":number,
   "ImportSameRelease":boolean,
   "MinAppVersion":number,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ExportPackageRow{
   "PackageID":string,
   "Description":string,
   "AppVersion":string,
   "CreateDate":string,
   "CreatedBy":string,
   "LastExported":string,
   "Notes":string,
   "InternalNotes":string,
      /**  Solution Type  */  
   "Type":string,
      /**  Country Group / Country Code for CSF  */  
   "CGCCode":string,
   "Company":string,
   "SolutionID":string,
   "SolutionTypeID":string,
   "BuildIteration":number,
   "SolutionReference":string,
   "ImportSameRelease":boolean,
   "MinAppVersion":number,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param solutionID
      @param ds
   */  
export interface AddItemToSolution_input{
   solutionID:string,
   ds:any,      //schema had no properties on an object.
}

export interface AddItemToSolution_output{
}

   /** Required : 
      @param settings
   */  
export interface Build_input{
   settings:Ice_Tablesets_SolutionBuildSettingsTableset[],
}

export interface Build_output{
   returnObj:Ice_BO_ExportPackage_SolutionBuildResult[],
}

   /** Required : 
      @param solutionID
   */  
export interface DeleteByID_input{
      /**  the SolutionID  */  
   solutionID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param solutionID
   */  
export interface DeleteSolutionDBScripts_input{
      /**  the SolutionID of the import  */  
   solutionID:string,
}

export interface DeleteSolutionDBScripts_output{
      /**  success or failure of the update  */  
   returnObj:boolean,
}

   /** Required : 
      @param solutionID
   */  
export interface DeleteSolutionInstall_input{
      /**  Solution ID.  */  
   solutionID:string,
}

export interface DeleteSolutionInstall_output{
      /**  Whether a row was found to delete.  */  
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   content:string,
}
}

   /** Required : 
      @param solutionID
      @param allCompanies
   */  
export interface Delete_input{
      /**  The solution identifier.  */  
   solutionID:string,
      /**  if set to `true` [all companies].  */  
   allCompanies:boolean,
}

export interface Delete_output{
   returnObj:Ice_BO_ExportPackage_SolutionResult[],
}

   /** Required : 
      @param xml
   */  
export interface GetBORecByID_input{
   xml:string,
}

export interface GetBORecByID_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param solutionID
   */  
export interface GetBuildSettings_input{
      /**  Solution identifier.  */  
   solutionID:string,
}

export interface GetBuildSettings_output{
   returnObj:Ice_Tablesets_SolutionBuildSettingsTableset[],
}

   /** Required : 
      @param packageID
   */  
export interface GetByID_input{
      /**  The package ID code  */  
   packageID:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_ExportPackageTableset[],
}

   /** Required : 
      @param tableName
   */  
export interface GetElementBOName_input{
   tableName:string,
}

export interface GetElementBOName_output{
   returnObj:string,
}

   /** Required : 
      @param tableName
      @param foreignSysRowId
      @param ns
   */  
export interface GetExportRow_input{
   tableName:string,
   foreignSysRowId:string,
   ns:string,
}

export interface GetExportRow_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param cabData
      @param solutionFile
   */  
export interface GetInstallSettings_input{
      /**  The CAB data.  */  
   cabData:string,
      /**  Solution file name.  */  
   solutionFile:string,
}

export interface GetInstallSettings_output{
   returnObj:Ice_Tablesets_SolutionInstallSettingsTableset[],
}

   /** Required : 
      @param solutionID
   */  
export interface GetInstalledSolution_input{
   solutionID:string,
}

export interface GetInstalledSolution_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   content:string,
}
}

export interface GetInstalledSolutions_output{
   returnObj:Ice_BO_ExportPackage_InstalledSolution[],
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
      /**  The whereClause filter  */  
   whereClause:string,
      /**  Size of a page  */  
   pageSize:number,
      /**  The absolute page  */  
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Ice_Tablesets_ExportPackageListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param packageID
   */  
export interface GetNewEPFileContents_input{
   ds:Ice_Tablesets_ExportPackageTableset[],
      /**  The package ID  */  
   packageID:string,
}

export interface GetNewEPFileContents_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ExportPackageTableset[],
}
}

   /** Required : 
      @param ds
      @param packageID
   */  
export interface GetNewEPHistory_input{
   ds:Ice_Tablesets_ExportPackageTableset[],
      /**  The package ID  */  
   packageID:string,
}

export interface GetNewEPHistory_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ExportPackageTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewExportPackage_input{
   ds:Ice_Tablesets_ExportPackageTableset[],
}

export interface GetNewExportPackage_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ExportPackageTableset[],
}
}

   /** Required : 
      @param solutionID
   */  
export interface GetSolutionHistory_input{
   solutionID:string,
}

export interface GetSolutionHistory_output{
   returnObj:Ice_BO_ExportPackage_SolutionEvent[],
}

   /** Required : 
      @param solutionID
   */  
export interface HasUnsupportedContentTypes_input{
   solutionID:string,
}

export interface HasUnsupportedContentTypes_output{
   returnObj:boolean,
}

export interface Ice_BO_ExportPackage_InstalledSolution{
   CompanyID:string,
   SolutionID:string,
   Description:string,
   FileName:string,
   BuildIteration:number,
   SolutionReference:string,
   ChangedBy:string,
   ChangedOn:string,
}

export interface Ice_BO_ExportPackage_LogRecord{
   UtcDate:string,
   Type:number,
   Message:string,
}

export interface Ice_BO_ExportPackage_SolutionBuildResult{
   Content:string,
   HashContent:string,
   LogRecords:Ice_BO_ExportPackage_LogRecord[],
   HasErrors:boolean,
}

export interface Ice_BO_ExportPackage_SolutionEvent{
   CompanyID:string,
   SolutionID:string,
   Sequence:number,
   Event:string,
   Description:string,
   FileName:string,
   BuildIteration:number,
   SolutionReference:string,
   CreatedBy:string,
   CreatedOn:string,
}

export interface Ice_BO_ExportPackage_SolutionResult{
   LogRecords:Ice_BO_ExportPackage_LogRecord[],
   HasErrors:boolean,
}

export interface Ice_Extensions_ExtensionRow{
   ColumnValues:object
   RowMod:string,
   SysRowID:string,
}

export interface Ice_Extensions_ExtensionTableColumn{
   ColumnName:string,
   ColumnType:string,
}

export interface Ice_Extensions_ExtensionTableData{
   Table:Ice_Extensions_ExtensionRow[],
   SystemCode:string,
   TableName:string,
   Columns:Ice_Extensions_ExtensionTableColumn[],
   PrimaryKeyColumns:string,
   PeerTableSystemCode:string,
   PeerTableName:string,
}

export interface Ice_Tablesets_BAQBuildSettingsRow{
   QueryDescription:string,
   QueryID:string,
   SCPassword:string,
   SCServer:string,
   SCServerUrl:string,
   SCUser:string,
   SCCredentialsAreValid:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BAQInstallSettingsRow{
   ExtDataSourceName:string,
   OverwriteExistingSCWorkflow:boolean,
   QueryDescription:string,
   QueryID:string,
   QueryType:number,
   SCExecPassword:string,
   SCExecUser:string,
   SCPassword:string,
   SCServer:string,
   SCServerUrl:string,
   SCUser:string,
   SCWorkflowPackage:string,
   UseCompanyDefaultSCSettings:boolean,
   SCCredentialsAreValid:boolean,
   CanImportSCWorkflow:boolean,
   SCExecutionCredentialsAreValid:boolean,
   SCExecServer:string,
   SCWorkflowName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPBAQReportRow{
      /**  BAQ Report ID, the unique identifier for this report within the company  */  
   BAQRptID:string,
      /**  Indicating if this record is selected in the export package  */  
   Selected:boolean,
   PackageID:string,
      /**  Description  */  
   Description:string,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPBpDirectiveGroupRow{
   DirectiveGroup:string,
   DirectiveCount:number,
   PackageID:string,
   Selected:boolean,
   Description:string,
      /**  Country Group / Country Code for CSF  */  
   CGCCode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPChgLogGARow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The unique Alert Num of the record.  The AlertNum should be greater than or equal to 2000 to avoid conflicts with standard global alerts.  */  
   AlertNum:number,
   Selected:boolean,
   PackageID:string,
      /**  The description of the alert/change log  */  
   Description:string,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPDashBdDefRow{
   PackageID:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  VN - Vantage, VS - Vista  */  
   ProductID:string,
   DefinitionID:string,
   Selected:boolean,
   Description:string,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPEfxLibraryRow{
   PackageID:string,
      /**  ID of Epicor Functions Library  */  
   LibraryID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPExportsRow{
   PackageID:string,
      /**  Company Identifier.  */  
   Company:string,
      /**   no = this exports is a work-in-process one
Since 9.0 there should be only approved BAQs.  */  
   Approved:boolean,
      /**  The userid of the user who created the export.  */  
   UserID:string,
      /**  The unique export identifier.  */  
   ExportID:string,
   Selected:boolean,
      /**  Description  */  
   Description:string,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPExtensionSetRow{
   ExtensionSetID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPFileContentsRow{
      /**  Export Package ID  */  
   PackageID:string,
      /**  Source Path  */  
   SourcePath:string,
      /**  File Content Type  */  
   FileContentType:number,
      /**  Description  */  
   Description:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RunSequence  */  
   RunSequence:number,
      /**  Notes  */  
   Notes:string,
   CabFolder:string,
   Selected:boolean,
   SourceFilename:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPHistoryRow{
      /**  Export Package ID  */  
   PackageID:string,
      /**  Action Number  */  
   ActionNum:number,
      /**  User ID  */  
   UserID:string,
      /**  Action Date  */  
   ActionDate:string,
      /**  Description  */  
   Description:string,
   Selected:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPMenuRow{
   PackageID:string,
      /**  MM=module, XX=MN,UP,LS,PC, and ZZZZ = number.  */  
   MenuID:string,
   Selected:boolean,
   Description:string,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPQuickSearchRow{
      /**  Company Identifier. If blank then this quick search is for all companies.  */  
   Company:string,
   GlbCompany:string,
      /**  The unique identifier for this quick search  */  
   QuickSearchID:string,
      /**  Indicating if this record is selected in the export package  */  
   Selected:boolean,
   PackageID:string,
      /**  Description  */  
   Description:string,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPReportRow{
   PackageID:string,
   ReportID:string,
   Selected:boolean,
   Description:string,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPReportStyleRow{
   CGCCode:string,
   Description:string,
   PackageID:string,
   ReportID:string,
   Selected:boolean,
   StyleNum:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPRptDataDefRow{
   PackageID:string,
   RptDefID:string,
   Selected:boolean,
   Description:string,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPSecurityRow{
   PackageID:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Security ID for the Program/SubMenu.  Format is either "XXX999-888" or "XXX999-888", where XXX is either SEC or UD (User Defined), 999 is a number to make the code unique, and -888 is a number used to make a subcomponent unique.  Subcomponents are used to allow more restricted access to a piece of a menu item(program).  For example: Costing information in Job Tracker.  */  
   SecCode:string,
   Selected:boolean,
   Description:string,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPSolutionDetailDisplayRow{
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPSolutionDetailRow{
      /**  SolutionID  */  
   SolutionID:string,
      /**  ForeignSysRowID  */  
   ForeignSysRowID:string,
      /**  TableName  */  
   TableName:string,
      /**  LastUpdatedBy  */  
   LastUpdatedBy:string,
      /**  LastUpdated  */  
   LastUpdated:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   Elements:string,
   PackageID:string,
   Selected:number,
   SolutionTypeID:string,
   InstallationOrder:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPSolutionHeaderRow{
      /**  SolutionID  */  
   SolutionID:string,
      /**  Company  */  
   Company:string,
      /**  Description  */  
   Description:string,
      /**  AppVersion  */  
   AppVersion:string,
      /**  InternalNotes  */  
   InternalNotes:string,
      /**  Notes  */  
   Notes:string,
      /**  LastExported  */  
   LastExported:string,
      /**  CreatedBy  */  
   CreatedBy:string,
      /**  CreateDate  */  
   CreateDate:string,
      /**  SolutionTypeID  */  
   SolutionTypeID:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  BuildIteration  */  
   BuildIteration:number,
      /**  SolutionReference  */  
   SolutionReference:string,
      /**  MinAppVersion  */  
   MinAppVersion:number,
      /**  ImportSameRelease  */  
   ImportSameRelease:boolean,
   PackageID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPSolutionPackageRow{
      /**  SolutionID  */  
   SolutionID:string,
      /**  ForeignSysRowID  */  
   ForeignSysRowID:string,
      /**  TableName  */  
   TableName:string,
      /**  LastUpdatedBy  */  
   LastUpdatedBy:string,
      /**  LastUpdated  */  
   LastUpdated:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPSolutionTrackerDetailRow{
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPSolutionTrackerRow{
      /**  SolutionID  */  
   SolutionID:string,
      /**  TableName  */  
   TableName:string,
      /**  LastUpdated  */  
   LastUpdated:string,
      /**  ForeignSysRowID  */  
   ForeignSysRowID:string,
      /**  LastUpdatedBy  */  
   LastUpdatedBy:string,
      /**  IsSelected  */  
   IsSelected:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   Available:number,
   Elements:string,
   PackageID:string,
   Selected:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPSolutionTypeRow{
   SolutionID:string,
   Company:string,
   SolutionTypeID:string,
   ElementHeaderID:string,
   ParentTableName:string,
   BusinessObject:string,
   BOMethod:string,
   ChildTableName:string,
   ElementDisplayColumnID:number,
   ParentColumnName:string,
   DataType:string,
   ParameterName:string,
   ParameterOrder:number,
   ParameterDataType:string,
   PackageID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPStructuredReportRow{
   ReportID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPUDCodeTypeRow{
      /**  Company Identifier.  */  
   Company:string,
   CodeTypeID:string,
   PackageID:string,
   Selected:boolean,
   Description:string,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPUserDefinedTableRow{
      /**  EP Package ID  */  
   PackageID:string,
      /**  Table Name  */  
   TableName:string,
      /**  Selection flag  */  
   Selected:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPXXXDefRow{
   PackageID:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  VN - Vantage, VS - Vista  */  
   ProductID:string,
      /**  Ex: Customization, Personalization  */  
   TypeCode:string,
      /**   Generic key component field.
Ex: Customization Name if TypeCode =  "Customization" 
FormName if TypeCode = "Personalization"  */  
   Key1:string,
      /**   Generic key component field.
Ex: FormName Name if TypeCode =  "Customization" 
UserID if TypeCode = "Personalization"  */  
   Key2:string,
      /**   Generic key component field.  
Ex: if TypeCode =  "Customization"  this may contain "WIP" or blanks.  */  
   Key3:string,
   Selected:boolean,
   Description:string,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPzBODefRow{
   PackageID:string,
   ClassName:string,
   ObjectNS:string,
   Selected:boolean,
   Description:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EPzDataRow{
   PackageID:string,
   DataTableID:string,
   Selected:boolean,
   Description:string,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ExportPackageListRow{
   PackageID:string,
   Description:string,
   AppVersion:string,
   CreateDate:string,
   CreatedBy:string,
   LastExported:string,
   Notes:string,
   InternalNotes:string,
      /**  Solution Type  */  
   Type:string,
      /**  Country Group / Country Code for CSF  */  
   CGCCode:string,
   Company:string,
   SolutionID:string,
   SolutionTypeID:string,
   SolutionVersion:string,
   SolutionReference:string,
   BuildIteration:number,
   ImportSameRelease:boolean,
   MinAppVersion:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ExportPackageListTableset{
   ExportPackageList:Ice_Tablesets_ExportPackageListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_ExportPackageRow{
   PackageID:string,
   Description:string,
   AppVersion:string,
   CreateDate:string,
   CreatedBy:string,
   LastExported:string,
   Notes:string,
   InternalNotes:string,
      /**  Solution Type  */  
   Type:string,
      /**  Country Group / Country Code for CSF  */  
   CGCCode:string,
   Company:string,
   SolutionID:string,
   SolutionTypeID:string,
   BuildIteration:number,
   SolutionReference:string,
   ImportSameRelease:boolean,
   MinAppVersion:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ExportPackageTableset{
   ExportPackage:Ice_Tablesets_ExportPackageRow[],
   EPBAQReport:Ice_Tablesets_EPBAQReportRow[],
   EPBpDirectiveGroup:Ice_Tablesets_EPBpDirectiveGroupRow[],
   EPChgLogGA:Ice_Tablesets_EPChgLogGARow[],
   EPDashBdDef:Ice_Tablesets_EPDashBdDefRow[],
   EPEfxLibrary:Ice_Tablesets_EPEfxLibraryRow[],
   EPExports:Ice_Tablesets_EPExportsRow[],
   EPFileContents:Ice_Tablesets_EPFileContentsRow[],
   EPHistory:Ice_Tablesets_EPHistoryRow[],
   EPMenu:Ice_Tablesets_EPMenuRow[],
   EPQuickSearch:Ice_Tablesets_EPQuickSearchRow[],
   EPReport:Ice_Tablesets_EPReportRow[],
   EPReportStyle:Ice_Tablesets_EPReportStyleRow[],
   EPRptDataDef:Ice_Tablesets_EPRptDataDefRow[],
   EPSecurity:Ice_Tablesets_EPSecurityRow[],
   EPUDCodeType:Ice_Tablesets_EPUDCodeTypeRow[],
   EPUserDefinedTable:Ice_Tablesets_EPUserDefinedTableRow[],
   EPXXXDef:Ice_Tablesets_EPXXXDefRow[],
   EPzBODef:Ice_Tablesets_EPzBODefRow[],
   EPzData:Ice_Tablesets_EPzDataRow[],
   EPExtensionSet:Ice_Tablesets_EPExtensionSetRow[],
   EPSolutionDetail:Ice_Tablesets_EPSolutionDetailRow[],
   EPSolutionDetailDisplay:Ice_Tablesets_EPSolutionDetailDisplayRow[],
   EPSolutionHeader:Ice_Tablesets_EPSolutionHeaderRow[],
   EPSolutionPackage:Ice_Tablesets_EPSolutionPackageRow[],
   EPSolutionTracker:Ice_Tablesets_EPSolutionTrackerRow[],
   EPSolutionTrackerDetail:Ice_Tablesets_EPSolutionTrackerDetailRow[],
   EPSolutionType:Ice_Tablesets_EPSolutionTypeRow[],
   EPStructuredReport:Ice_Tablesets_EPStructuredReportRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_MainBuildSettingsRow{
      /**  Library type.  */  
   LibraryType:number,
      /**  Solution identifier.  */  
   SolutionID:string,
   SysRowID:string,
   Output:string,
   PromptForCABName:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_MainInstallSettingsRow{
      /**  Solution identifier.  */  
   SolutionID:string,
      /**  Solution description.  */  
   Description:string,
      /**  Source version.  */  
   SourceVersion:string,
      /**  Destination version.  */  
   DestinationVersion:string,
      /**  Solution file.  */  
   SolutionFile:string,
      /**  Installation notes.  */  
   InstallNotes:string,
      /**  Build iteration.  */  
   BuildIteration:number,
      /**  Solution reference.  */  
   SolutionReference:string,
      /**  Minimum application version.  */  
   MinAppVersion:number,
      /**  Import the same release.  */  
   ImportSameRelease:boolean,
      /**  Library type.  */  
   LibraryType:number,
      /**  Source CAB schema.  */  
   SourceCabSchema:string,
      /**  Source company.  */  
   SourceCompany:string,
      /**  Includes files for deployment.  */  
   IncludesFilesForDeployment:boolean,
      /**  Validation hash.  */  
   ValidationHash:string,
      /**  Auto overwrite duplicate file.  */  
   AutoOverwriteDuplicateFile:boolean,
      /**  Auto overwrite duplicate data.  */  
   AutoOverwriteDuplicateData:boolean,
      /**  Delete previous install.  */  
   DeletePreviousInstall:boolean,
      /**  Override directives.  */  
   OverrideDirectives:boolean,
      /**  Only target current company.  */  
   OnlyTargetCurrentCompany:boolean,
   SysRowID:string,
   Output:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_PromptInstallSettingsRow{
      /**  Predefined server paths.  */  
   TargetBasePath:number,
      /**  Relative path for selected Target Base Path.  */  
   RelativePath:string,
   SysRowID:string,
      /**  File name with extension or a folder name.  */  
   SolutionItem:string,
      /**  Source item type (file or directory).  */  
   ItemType:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ReportStyleBuildSettingsRow{
      /**  Export image option.  */  
   ExportImage:boolean,
      /**  Export RDL file option.  */  
   ExportRDL:boolean,
      /**  Report identifier.  */  
   ReportID:string,
      /**  Style description.  */  
   StyleDescription:string,
      /**  Style identifier.  */  
   StyleNum:number,
   SysRowID:string,
      /**  Export certificate option.  */  
   ExportCertificate:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ReportStyleInstallSettingsRow{
      /**  Report ID  */  
   ReportID:string,
      /**  Report Style Number  */  
   StyleNum:number,
      /**  Report Style Description  */  
   StyleDescription:string,
      /**  Certificate ID  */  
   CertificateID:string,
      /**  Overwrite Certificate  */  
   OverwriteCertificate:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_SolutionBuildSettingsTableset{
   BAQBuildSettings:Ice_Tablesets_BAQBuildSettingsRow[],
   MainBuildSettings:Ice_Tablesets_MainBuildSettingsRow[],
   ReportStyleBuildSettings:Ice_Tablesets_ReportStyleBuildSettingsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_SolutionInstallSettingsTableset{
   BAQInstallSettings:Ice_Tablesets_BAQInstallSettingsRow[],
   MainInstallSettings:Ice_Tablesets_MainInstallSettingsRow[],
   PromptInstallSettings:Ice_Tablesets_PromptInstallSettingsRow[],
   ReportStyleInstallSettings:Ice_Tablesets_ReportStyleInstallSettingsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param cabData
      @param settings
   */  
export interface Install_input{
      /**  The CAB data.  */  
   cabData:string,
   settings:Ice_Tablesets_SolutionInstallSettingsTableset[],
}

export interface Install_output{
   returnObj:Ice_BO_ExportPackage_SolutionResult[],
}

   /** Required : 
      @param xml
   */  
export interface IsValidBORecByID_input{
   xml:string,
}

export interface IsValidBORecByID_output{
   returnObj:boolean,
}

   /** Required : 
      @param solutionID
   */  
export interface MoveTrackedRowsToSolution_input{
   solutionID:string,
}

export interface MoveTrackedRowsToSolution_output{
}

   /** Required : 
      @param elementType
      @param solutionID
   */  
export interface PopulateWorkbenchPromoteDetailPanel_input{
   elementType:string,
   solutionID:string,
}

export interface PopulateWorkbenchPromoteDetailPanel_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param elementType
      @param solutionID
   */  
export interface PopulateWorkbenchTrackerDetailPanel_input{
   elementType:string,
   solutionID:string,
}

export interface PopulateWorkbenchTrackerDetailPanel_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param solutionID
      @param description
      @param fileName
      @param content
      @param buildIteration
      @param solutionReference
   */  
export interface RecordSolutionInstall_input{
   solutionID:string,
   description:string,
   fileName:string,
   content:string,
   buildIteration:number,
   solutionReference:string,
}

export interface RecordSolutionInstall_output{
}

   /** Required : 
      @param foreignSysRowIDs
      @param solutionID
   */  
export interface RemoveWorkbenchPromoteDetailRows_input{
      /**  the foreignsysrowid(s) of the row to delete  */  
   foreignSysRowIDs:string,
      /**  the users solutionID  */  
   solutionID:string,
}

export interface RemoveWorkbenchPromoteDetailRows_output{
}

   /** Required : 
      @param foreignSysRowIDs
      @param solutionID
      @param delete
      @param IsSelected
   */  
export interface RemoveWorkbenchTrackerDetailRows_input{
   foreignSysRowIDs:string,
   solutionID:string,
   delete:boolean,
   IsSelected:boolean,
}

export interface RemoveWorkbenchTrackerDetailRows_output{
}

   /** Required : 
      @param solutionID
      @param scriptName
      @param scriptContent
      @param runSequence
      @param notes
   */  
export interface UpdateDBScript_input{
      /**  the SolutionID of the import  */  
   solutionID:string,
      /**  the file name of the script being imported  */  
   scriptName:string,
      /**  the script content  */  
   scriptContent:string,
      /**  the sequence to run the script in the DatabaseScriptRunner  */  
   runSequence:number,
      /**  the user notes for this script  */  
   notes:string,
}

export interface UpdateDBScript_output{
      /**  success or failure of the update  */  
   returnObj:boolean,
}

   /** Required : 
      @param importID
      @param importModuleType
   */  
export interface UpdateMenuModuleType_input{
      /**  the MenuID  */  
   importID:string,
      /**  the Menu Module  */  
   importModuleType:string,
}

export interface UpdateMenuModuleType_output{
      /**  success  */  
   returnObj:boolean,
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_ExportPackageTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ExportPackageTableset[],
}
}

   /** Required : 
      @param settings
   */  
export interface ValidateBuildSettings_input{
   settings:Ice_Tablesets_SolutionBuildSettingsTableset[],
}

export interface ValidateBuildSettings_output{
   returnObj:Ice_Tablesets_SolutionBuildSettingsTableset[],
}

   /** Required : 
      @param settings
   */  
export interface ValidateInstallSettings_input{
   settings:Ice_Tablesets_SolutionInstallSettingsTableset[],
}

export interface ValidateInstallSettings_output{
   returnObj:Ice_Tablesets_SolutionInstallSettingsTableset[],
}

   /** Required : 
      @param solutionTypeID
   */  
export interface ValidateSolutionType_input{
      /**  The Solution Type ID  */  
   solutionTypeID:string,
}

export interface ValidateSolutionType_output{
      /**  false if the Solution Type ID is not valid in the database  */  
   returnObj:boolean,
}

