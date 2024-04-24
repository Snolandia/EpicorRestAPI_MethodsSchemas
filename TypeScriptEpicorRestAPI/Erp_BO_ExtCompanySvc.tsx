import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ExtCompanySvc
// Description: ExtCompany object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/$metadata", {
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
   Summary: Calls GetRows for the service
   Description: Get ExtCompanies items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtCompanies
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtCompanyRow
   */  
export function get_ExtCompanies(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanies", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtCompanies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtCompanyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtCompanyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExtCompanies(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanies", {
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
   Summary: Calls GetByID to retrieve the ExtCompany item
   Description: Calls GetByID to retrieve the ExtCompany item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtCompany
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtCompanyRow
   */  
export function get_ExtCompanies_Company_ExtSystemID_ExtCompanyID(Company:string, ExtSystemID:string, ExtCompanyID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ExtCompanyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ExtCompanyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ExtCompany for the service
   Description: Calls UpdateExt to update ExtCompany. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtCompany
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtCompanyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ExtCompanies_Company_ExtSystemID_ExtCompanyID(Company:string, ExtSystemID:string, ExtCompanyID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete ExtCompany item
   Description: Call UpdateExt to delete ExtCompany item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtCompany
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ExtCompanies_Company_ExtSystemID_ExtCompanyID(Company:string, ExtSystemID:string, ExtCompanyID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")", {
          method: 'delete',
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
   Summary: Calls GetByID for the service
   Description: Get ExtCompanyECCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ExtCompanyECCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtCompanyECCRow
   */  
export function get_ExtCompanies_Company_ExtSystemID_ExtCompanyID_ExtCompanyECCs(Company:string, ExtSystemID:string, ExtCompanyID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyECCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")/ExtCompanyECCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyECCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ExtCompanyECC item
   Description: Calls GetByID to retrieve the ExtCompanyECC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtCompanyECC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param ECCID Desc: ECCID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtCompanyECCRow
   */  
export function get_ExtCompanies_Company_ExtSystemID_ExtCompanyID_ExtCompanyECCs_Company_ExtCompanyID_ExtSystemID_ECCID(Company:string, ExtSystemID:string, ExtCompanyID:string, ECCID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ExtCompanyECCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")/ExtCompanyECCs(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ExtCompanyECCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ExtPlants items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ExtPlants1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtPlantRow
   */  
export function get_ExtCompanies_Company_ExtSystemID_ExtCompanyID_ExtPlants(Company:string, ExtSystemID:string, ExtCompanyID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPlantRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")/ExtPlants", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPlantRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ExtPlant item
   Description: Calls GetByID to retrieve the ExtPlant item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtPlant1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param TransferMethod Desc: TransferMethod   Required: True   Allow empty value : True
      @param ExtPlantID Desc: ExtPlantID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtPlantRow
   */  
export function get_ExtCompanies_Company_ExtSystemID_ExtCompanyID_ExtPlants_Company_ExtSystemID_TransferMethod_ExtCompanyID_ExtPlantID(Company:string, ExtSystemID:string, ExtCompanyID:string, TransferMethod:string, ExtPlantID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ExtPlantRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")/ExtPlants(" + Company + "," + ExtSystemID + "," + TransferMethod + "," + ExtCompanyID + "," + ExtPlantID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ExtPlantRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get EntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EntityGLCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   */  
export function get_ExtCompanies_Company_ExtSystemID_ExtCompanyID_EntityGLCs(Company:string, ExtSystemID:string, ExtCompanyID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")/EntityGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   */  
export function get_ExtCompanies_Company_ExtSystemID_ExtCompanyID_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, ExtSystemID:string, ExtCompanyID:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ExtCompanyAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ExtCompanyAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtCompanyAttchRow
   */  
export function get_ExtCompanies_Company_ExtSystemID_ExtCompanyID_ExtCompanyAttches(Company:string, ExtSystemID:string, ExtCompanyID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")/ExtCompanyAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ExtCompanyAttch item
   Description: Calls GetByID to retrieve the ExtCompanyAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtCompanyAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtCompanyAttchRow
   */  
export function get_ExtCompanies_Company_ExtSystemID_ExtCompanyID_ExtCompanyAttches_Company_ExtSystemID_ExtCompanyID_DrawingSeq(Company:string, ExtSystemID:string, ExtCompanyID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ExtCompanyAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")/ExtCompanyAttches(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ExtCompanyAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ExtCompanyECCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtCompanyECCs
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtCompanyECCRow
   */  
export function get_ExtCompanyECCs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyECCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyECCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyECCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtCompanyECCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtCompanyECCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtCompanyECCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExtCompanyECCs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyECCs", {
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
   Summary: Calls GetByID to retrieve the ExtCompanyECC item
   Description: Calls GetByID to retrieve the ExtCompanyECC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtCompanyECC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ECCID Desc: ECCID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtCompanyECCRow
   */  
export function get_ExtCompanyECCs_Company_ExtCompanyID_ExtSystemID_ECCID(Company:string, ExtCompanyID:string, ExtSystemID:string, ECCID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ExtCompanyECCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyECCs(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ExtCompanyECCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ExtCompanyECC for the service
   Description: Calls UpdateExt to update ExtCompanyECC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtCompanyECC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ECCID Desc: ECCID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtCompanyECCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ExtCompanyECCs_Company_ExtCompanyID_ExtSystemID_ECCID(Company:string, ExtCompanyID:string, ExtSystemID:string, ECCID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyECCs(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete ExtCompanyECC item
   Description: Call UpdateExt to delete ExtCompanyECC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtCompanyECC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ECCID Desc: ECCID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ExtCompanyECCs_Company_ExtCompanyID_ExtSystemID_ECCID(Company:string, ExtCompanyID:string, ExtSystemID:string, ECCID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyECCs(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + ")", {
          method: 'delete',
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
   Summary: Calls GetByID for the service
   Description: Get ECCDocTypes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECCDocTypes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ECCID Desc: ECCID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECCDocTypeRow
   */  
export function get_ExtCompanyECCs_Company_ExtCompanyID_ExtSystemID_ECCID_ECCDocTypes(Company:string, ExtCompanyID:string, ExtSystemID:string, ECCID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECCDocTypeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyECCs(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + ")/ECCDocTypes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECCDocTypeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ECCDocType item
   Description: Calls GetByID to retrieve the ECCDocType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECCDocType1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ECCID Desc: ECCID   Required: True
      @param DocTypeID Desc: DocTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECCDocTypeRow
   */  
export function get_ExtCompanyECCs_Company_ExtCompanyID_ExtSystemID_ECCID_ECCDocTypes_Company_ExtCompanyID_ExtSystemID_ECCID_DocTypeID(Company:string, ExtCompanyID:string, ExtSystemID:string, ECCID:string, DocTypeID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECCDocTypeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyECCs(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + ")/ECCDocTypes(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + "," + DocTypeID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECCDocTypeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ECCReportDefaultStyles items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECCReportDefaultStyles1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ECCID Desc: ECCID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECCReportDefaultStyleRow
   */  
export function get_ExtCompanyECCs_Company_ExtCompanyID_ExtSystemID_ECCID_ECCReportDefaultStyles(Company:string, ExtCompanyID:string, ExtSystemID:string, ECCID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECCReportDefaultStyleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyECCs(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + ")/ECCReportDefaultStyles", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECCReportDefaultStyleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ECCReportDefaultStyle item
   Description: Calls GetByID to retrieve the ECCReportDefaultStyle item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECCReportDefaultStyle1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ECCID Desc: ECCID   Required: True
      @param AutoProgram Desc: AutoProgram   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECCReportDefaultStyleRow
   */  
export function get_ExtCompanyECCs_Company_ExtCompanyID_ExtSystemID_ECCID_ECCReportDefaultStyles_Company_ExtCompanyID_ExtSystemID_ECCID_AutoProgram(Company:string, ExtCompanyID:string, ExtSystemID:string, ECCID:string, AutoProgram:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECCReportDefaultStyleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyECCs(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + ")/ECCReportDefaultStyles(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + "," + AutoProgram + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECCReportDefaultStyleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ECCDocTypes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECCDocTypes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECCDocTypeRow
   */  
export function get_ECCDocTypes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECCDocTypeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ECCDocTypes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECCDocTypeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECCDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECCDocTypeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECCDocTypeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECCDocTypes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ECCDocTypes", {
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
   Summary: Calls GetByID to retrieve the ECCDocType item
   Description: Calls GetByID to retrieve the ECCDocType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECCDocType
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ECCID Desc: ECCID   Required: True
      @param DocTypeID Desc: DocTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECCDocTypeRow
   */  
export function get_ECCDocTypes_Company_ExtCompanyID_ExtSystemID_ECCID_DocTypeID(Company:string, ExtCompanyID:string, ExtSystemID:string, ECCID:string, DocTypeID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECCDocTypeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ECCDocTypes(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + "," + DocTypeID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECCDocTypeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ECCDocType for the service
   Description: Calls UpdateExt to update ECCDocType. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECCDocType
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ECCID Desc: ECCID   Required: True
      @param DocTypeID Desc: DocTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECCDocTypeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ECCDocTypes_Company_ExtCompanyID_ExtSystemID_ECCID_DocTypeID(Company:string, ExtCompanyID:string, ExtSystemID:string, ECCID:string, DocTypeID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ECCDocTypes(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + "," + DocTypeID + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete ECCDocType item
   Description: Call UpdateExt to delete ECCDocType item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECCDocType
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ECCID Desc: ECCID   Required: True
      @param DocTypeID Desc: DocTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ECCDocTypes_Company_ExtCompanyID_ExtSystemID_ECCID_DocTypeID(Company:string, ExtCompanyID:string, ExtSystemID:string, ECCID:string, DocTypeID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ECCDocTypes(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + "," + DocTypeID + ")", {
          method: 'delete',
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
   Summary: Calls GetRows for the service
   Description: Get ECCReportDefaultStyles items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECCReportDefaultStyles
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECCReportDefaultStyleRow
   */  
export function get_ECCReportDefaultStyles(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECCReportDefaultStyleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ECCReportDefaultStyles", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECCReportDefaultStyleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECCReportDefaultStyles
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECCReportDefaultStyleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECCReportDefaultStyleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECCReportDefaultStyles(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ECCReportDefaultStyles", {
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
   Summary: Calls GetByID to retrieve the ECCReportDefaultStyle item
   Description: Calls GetByID to retrieve the ECCReportDefaultStyle item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECCReportDefaultStyle
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ECCID Desc: ECCID   Required: True
      @param AutoProgram Desc: AutoProgram   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECCReportDefaultStyleRow
   */  
export function get_ECCReportDefaultStyles_Company_ExtCompanyID_ExtSystemID_ECCID_AutoProgram(Company:string, ExtCompanyID:string, ExtSystemID:string, ECCID:string, AutoProgram:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECCReportDefaultStyleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ECCReportDefaultStyles(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + "," + AutoProgram + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECCReportDefaultStyleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ECCReportDefaultStyle for the service
   Description: Calls UpdateExt to update ECCReportDefaultStyle. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECCReportDefaultStyle
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ECCID Desc: ECCID   Required: True
      @param AutoProgram Desc: AutoProgram   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECCReportDefaultStyleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ECCReportDefaultStyles_Company_ExtCompanyID_ExtSystemID_ECCID_AutoProgram(Company:string, ExtCompanyID:string, ExtSystemID:string, ECCID:string, AutoProgram:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ECCReportDefaultStyles(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + "," + AutoProgram + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete ECCReportDefaultStyle item
   Description: Call UpdateExt to delete ECCReportDefaultStyle item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECCReportDefaultStyle
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ECCID Desc: ECCID   Required: True
      @param AutoProgram Desc: AutoProgram   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ECCReportDefaultStyles_Company_ExtCompanyID_ExtSystemID_ECCID_AutoProgram(Company:string, ExtCompanyID:string, ExtSystemID:string, ECCID:string, AutoProgram:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ECCReportDefaultStyles(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + "," + AutoProgram + ")", {
          method: 'delete',
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
   Summary: Calls GetRows for the service
   Description: Get ExtPlants items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtPlants
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtPlantRow
   */  
export function get_ExtPlants(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPlantRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtPlants", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPlantRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtPlants
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtPlantRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtPlantRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExtPlants(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtPlants", {
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
   Summary: Calls GetByID to retrieve the ExtPlant item
   Description: Calls GetByID to retrieve the ExtPlant item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtPlant
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param TransferMethod Desc: TransferMethod   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param ExtPlantID Desc: ExtPlantID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtPlantRow
   */  
export function get_ExtPlants_Company_ExtSystemID_TransferMethod_ExtCompanyID_ExtPlantID(Company:string, ExtSystemID:string, TransferMethod:string, ExtCompanyID:string, ExtPlantID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ExtPlantRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtPlants(" + Company + "," + ExtSystemID + "," + TransferMethod + "," + ExtCompanyID + "," + ExtPlantID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ExtPlantRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ExtPlant for the service
   Description: Calls UpdateExt to update ExtPlant. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtPlant
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param TransferMethod Desc: TransferMethod   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param ExtPlantID Desc: ExtPlantID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtPlantRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ExtPlants_Company_ExtSystemID_TransferMethod_ExtCompanyID_ExtPlantID(Company:string, ExtSystemID:string, TransferMethod:string, ExtCompanyID:string, ExtPlantID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtPlants(" + Company + "," + ExtSystemID + "," + TransferMethod + "," + ExtCompanyID + "," + ExtPlantID + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete ExtPlant item
   Description: Call UpdateExt to delete ExtPlant item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtPlant
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param TransferMethod Desc: TransferMethod   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param ExtPlantID Desc: ExtPlantID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ExtPlants_Company_ExtSystemID_TransferMethod_ExtCompanyID_ExtPlantID(Company:string, ExtSystemID:string, TransferMethod:string, ExtCompanyID:string, ExtPlantID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtPlants(" + Company + "," + ExtSystemID + "," + TransferMethod + "," + ExtCompanyID + "," + ExtPlantID + ")", {
          method: 'delete',
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
   Summary: Calls GetByID for the service
   Description: Get ExtWarehouses items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ExtWarehouses1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param TransferMethod Desc: TransferMethod   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param ExtPlantID Desc: ExtPlantID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtWarehouseRow
   */  
export function get_ExtPlants_Company_ExtSystemID_TransferMethod_ExtCompanyID_ExtPlantID_ExtWarehouses(Company:string, ExtSystemID:string, TransferMethod:string, ExtCompanyID:string, ExtPlantID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtWarehouseRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtPlants(" + Company + "," + ExtSystemID + "," + TransferMethod + "," + ExtCompanyID + "," + ExtPlantID + ")/ExtWarehouses", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtWarehouseRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ExtWarehouse item
   Description: Calls GetByID to retrieve the ExtWarehouse item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtWarehouse1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param TransferMethod Desc: TransferMethod   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param ExtPlantID Desc: ExtPlantID   Required: True   Allow empty value : True
      @param ExtWarehouseID Desc: ExtWarehouseID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtWarehouseRow
   */  
export function get_ExtPlants_Company_ExtSystemID_TransferMethod_ExtCompanyID_ExtPlantID_ExtWarehouses_Company_ExtSystemID_TransferMethod_ExtCompanyID_ExtPlantID_ExtWarehouseID(Company:string, ExtSystemID:string, TransferMethod:string, ExtCompanyID:string, ExtPlantID:string, ExtWarehouseID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ExtWarehouseRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtPlants(" + Company + "," + ExtSystemID + "," + TransferMethod + "," + ExtCompanyID + "," + ExtPlantID + ")/ExtWarehouses(" + Company + "," + ExtSystemID + "," + TransferMethod + "," + ExtCompanyID + "," + ExtPlantID + "," + ExtWarehouseID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ExtWarehouseRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ExtWarehouses items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtWarehouses
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtWarehouseRow
   */  
export function get_ExtWarehouses(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtWarehouseRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtWarehouses", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtWarehouseRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtWarehouses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtWarehouseRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtWarehouseRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExtWarehouses(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtWarehouses", {
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
   Summary: Calls GetByID to retrieve the ExtWarehouse item
   Description: Calls GetByID to retrieve the ExtWarehouse item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtWarehouse
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param TransferMethod Desc: TransferMethod   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param ExtPlantID Desc: ExtPlantID   Required: True   Allow empty value : True
      @param ExtWarehouseID Desc: ExtWarehouseID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtWarehouseRow
   */  
export function get_ExtWarehouses_Company_ExtSystemID_TransferMethod_ExtCompanyID_ExtPlantID_ExtWarehouseID(Company:string, ExtSystemID:string, TransferMethod:string, ExtCompanyID:string, ExtPlantID:string, ExtWarehouseID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ExtWarehouseRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtWarehouses(" + Company + "," + ExtSystemID + "," + TransferMethod + "," + ExtCompanyID + "," + ExtPlantID + "," + ExtWarehouseID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ExtWarehouseRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ExtWarehouse for the service
   Description: Calls UpdateExt to update ExtWarehouse. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtWarehouse
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param TransferMethod Desc: TransferMethod   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param ExtPlantID Desc: ExtPlantID   Required: True   Allow empty value : True
      @param ExtWarehouseID Desc: ExtWarehouseID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtWarehouseRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ExtWarehouses_Company_ExtSystemID_TransferMethod_ExtCompanyID_ExtPlantID_ExtWarehouseID(Company:string, ExtSystemID:string, TransferMethod:string, ExtCompanyID:string, ExtPlantID:string, ExtWarehouseID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtWarehouses(" + Company + "," + ExtSystemID + "," + TransferMethod + "," + ExtCompanyID + "," + ExtPlantID + "," + ExtWarehouseID + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete ExtWarehouse item
   Description: Call UpdateExt to delete ExtWarehouse item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtWarehouse
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param TransferMethod Desc: TransferMethod   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param ExtPlantID Desc: ExtPlantID   Required: True   Allow empty value : True
      @param ExtWarehouseID Desc: ExtWarehouseID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ExtWarehouses_Company_ExtSystemID_TransferMethod_ExtCompanyID_ExtPlantID_ExtWarehouseID(Company:string, ExtSystemID:string, TransferMethod:string, ExtCompanyID:string, ExtPlantID:string, ExtWarehouseID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtWarehouses(" + Company + "," + ExtSystemID + "," + TransferMethod + "," + ExtCompanyID + "," + ExtPlantID + "," + ExtWarehouseID + ")", {
          method: 'delete',
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
   Summary: Calls GetRows for the service
   Description: Get EntityGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EntityGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   */  
export function get_EntityGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/EntityGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EntityGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EntityGLCs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/EntityGLCs", {
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
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   */  
export function get_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update EntityGLC for the service
   Description: Calls UpdateExt to update EntityGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete EntityGLC item
   Description: Call UpdateExt to delete EntityGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'delete',
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
   Summary: Calls GetRows for the service
   Description: Get ExtCompanyAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtCompanyAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtCompanyAttchRow
   */  
export function get_ExtCompanyAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtCompanyAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtCompanyAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtCompanyAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExtCompanyAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyAttches", {
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
   Summary: Calls GetByID to retrieve the ExtCompanyAttch item
   Description: Calls GetByID to retrieve the ExtCompanyAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtCompanyAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtCompanyAttchRow
   */  
export function get_ExtCompanyAttches_Company_ExtSystemID_ExtCompanyID_DrawingSeq(Company:string, ExtSystemID:string, ExtCompanyID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ExtCompanyAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyAttches(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ExtCompanyAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ExtCompanyAttch for the service
   Description: Calls UpdateExt to update ExtCompanyAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtCompanyAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtCompanyAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ExtCompanyAttches_Company_ExtSystemID_ExtCompanyID_DrawingSeq(Company:string, ExtSystemID:string, ExtCompanyID:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyAttches(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + DrawingSeq + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete ExtCompanyAttch item
   Description: Call UpdateExt to delete ExtCompanyAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtCompanyAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ExtCompanyAttches_Company_ExtSystemID_ExtCompanyID_DrawingSeq(Company:string, ExtSystemID:string, ExtCompanyID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyAttches(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + DrawingSeq + ")", {
          method: 'delete',
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
   Summary: Calls GetRows for the service
   Description: Get ExtCompanyTriggerDefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtCompanyTriggerDefs
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtCompanyTriggerDefRow
   */  
export function get_ExtCompanyTriggerDefs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyTriggerDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerDefs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyTriggerDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtCompanyTriggerDefs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExtCompanyTriggerDefs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerDefs", {
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
   Summary: Calls GetByID to retrieve the ExtCompanyTriggerDef item
   Description: Calls GetByID to retrieve the ExtCompanyTriggerDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtCompanyTriggerDef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param SchemaName Desc: SchemaName   Required: True   Allow empty value : True
      @param DBTableName Desc: DBTableName   Required: True   Allow empty value : True
      @param TriggerType Desc: TriggerType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerDefRow
   */  
export function get_ExtCompanyTriggerDefs_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType(Company:string, ExtSystemID:string, ExtCompanyID:string, SchemaName:string, DBTableName:string, TriggerType:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ExtCompanyTriggerDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerDefs(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ExtCompanyTriggerDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ExtCompanyTriggerDef for the service
   Description: Calls UpdateExt to update ExtCompanyTriggerDef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtCompanyTriggerDef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param SchemaName Desc: SchemaName   Required: True   Allow empty value : True
      @param DBTableName Desc: DBTableName   Required: True   Allow empty value : True
      @param TriggerType Desc: TriggerType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ExtCompanyTriggerDefs_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType(Company:string, ExtSystemID:string, ExtCompanyID:string, SchemaName:string, DBTableName:string, TriggerType:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerDefs(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete ExtCompanyTriggerDef item
   Description: Call UpdateExt to delete ExtCompanyTriggerDef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtCompanyTriggerDef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param SchemaName Desc: SchemaName   Required: True   Allow empty value : True
      @param DBTableName Desc: DBTableName   Required: True   Allow empty value : True
      @param TriggerType Desc: TriggerType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ExtCompanyTriggerDefs_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType(Company:string, ExtSystemID:string, ExtCompanyID:string, SchemaName:string, DBTableName:string, TriggerType:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerDefs(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + ")", {
          method: 'delete',
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
   Summary: Calls GetByID for the service
   Description: Get ExtCompanyTriggerConditionGrps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ExtCompanyTriggerConditionGrps1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param SchemaName Desc: SchemaName   Required: True   Allow empty value : True
      @param DBTableName Desc: DBTableName   Required: True   Allow empty value : True
      @param TriggerType Desc: TriggerType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtCompanyTriggerConditionGrpRow
   */  
export function get_ExtCompanyTriggerDefs_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_ExtCompanyTriggerConditionGrps(Company:string, ExtSystemID:string, ExtCompanyID:string, SchemaName:string, DBTableName:string, TriggerType:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyTriggerConditionGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerDefs(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + ")/ExtCompanyTriggerConditionGrps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyTriggerConditionGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ExtCompanyTriggerConditionGrp item
   Description: Calls GetByID to retrieve the ExtCompanyTriggerConditionGrp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtCompanyTriggerConditionGrp1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param SchemaName Desc: SchemaName   Required: True   Allow empty value : True
      @param DBTableName Desc: DBTableName   Required: True   Allow empty value : True
      @param TriggerType Desc: TriggerType   Required: True   Allow empty value : True
      @param TriggerConditionGroupNum Desc: TriggerConditionGroupNum   Required: True
      @param TriggerActionNum Desc: TriggerActionNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerConditionGrpRow
   */  
export function get_ExtCompanyTriggerDefs_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_ExtCompanyTriggerConditionGrps_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_TriggerConditionGroupNum_TriggerActionNum(Company:string, ExtSystemID:string, ExtCompanyID:string, SchemaName:string, DBTableName:string, TriggerType:string, TriggerConditionGroupNum:string, TriggerActionNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ExtCompanyTriggerConditionGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerDefs(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + ")/ExtCompanyTriggerConditionGrps(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + "," + TriggerConditionGroupNum + "," + TriggerActionNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ExtCompanyTriggerConditionGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ExtCompanyTriggerConditionGrps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtCompanyTriggerConditionGrps
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtCompanyTriggerConditionGrpRow
   */  
export function get_ExtCompanyTriggerConditionGrps(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyTriggerConditionGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditionGrps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyTriggerConditionGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtCompanyTriggerConditionGrps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerConditionGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerConditionGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExtCompanyTriggerConditionGrps(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditionGrps", {
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
   Summary: Calls GetByID to retrieve the ExtCompanyTriggerConditionGrp item
   Description: Calls GetByID to retrieve the ExtCompanyTriggerConditionGrp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtCompanyTriggerConditionGrp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param SchemaName Desc: SchemaName   Required: True   Allow empty value : True
      @param DBTableName Desc: DBTableName   Required: True   Allow empty value : True
      @param TriggerType Desc: TriggerType   Required: True   Allow empty value : True
      @param TriggerConditionGroupNum Desc: TriggerConditionGroupNum   Required: True
      @param TriggerActionNum Desc: TriggerActionNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerConditionGrpRow
   */  
export function get_ExtCompanyTriggerConditionGrps_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_TriggerConditionGroupNum_TriggerActionNum(Company:string, ExtSystemID:string, ExtCompanyID:string, SchemaName:string, DBTableName:string, TriggerType:string, TriggerConditionGroupNum:string, TriggerActionNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ExtCompanyTriggerConditionGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditionGrps(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + "," + TriggerConditionGroupNum + "," + TriggerActionNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ExtCompanyTriggerConditionGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ExtCompanyTriggerConditionGrp for the service
   Description: Calls UpdateExt to update ExtCompanyTriggerConditionGrp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtCompanyTriggerConditionGrp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param SchemaName Desc: SchemaName   Required: True   Allow empty value : True
      @param DBTableName Desc: DBTableName   Required: True   Allow empty value : True
      @param TriggerType Desc: TriggerType   Required: True   Allow empty value : True
      @param TriggerConditionGroupNum Desc: TriggerConditionGroupNum   Required: True
      @param TriggerActionNum Desc: TriggerActionNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerConditionGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ExtCompanyTriggerConditionGrps_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_TriggerConditionGroupNum_TriggerActionNum(Company:string, ExtSystemID:string, ExtCompanyID:string, SchemaName:string, DBTableName:string, TriggerType:string, TriggerConditionGroupNum:string, TriggerActionNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditionGrps(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + "," + TriggerConditionGroupNum + "," + TriggerActionNum + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete ExtCompanyTriggerConditionGrp item
   Description: Call UpdateExt to delete ExtCompanyTriggerConditionGrp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtCompanyTriggerConditionGrp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param SchemaName Desc: SchemaName   Required: True   Allow empty value : True
      @param DBTableName Desc: DBTableName   Required: True   Allow empty value : True
      @param TriggerType Desc: TriggerType   Required: True   Allow empty value : True
      @param TriggerConditionGroupNum Desc: TriggerConditionGroupNum   Required: True
      @param TriggerActionNum Desc: TriggerActionNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ExtCompanyTriggerConditionGrps_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_TriggerConditionGroupNum_TriggerActionNum(Company:string, ExtSystemID:string, ExtCompanyID:string, SchemaName:string, DBTableName:string, TriggerType:string, TriggerConditionGroupNum:string, TriggerActionNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditionGrps(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + "," + TriggerConditionGroupNum + "," + TriggerActionNum + ")", {
          method: 'delete',
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
   Summary: Calls GetRows for the service
   Description: Get ExtCompanyTriggerActions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtCompanyTriggerActions
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtCompanyTriggerActionRow
   */  
export function get_ExtCompanyTriggerActions(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyTriggerActionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerActions", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyTriggerActionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtCompanyTriggerActions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerActionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerActionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExtCompanyTriggerActions(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerActions", {
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
   Summary: Calls GetByID to retrieve the ExtCompanyTriggerAction item
   Description: Calls GetByID to retrieve the ExtCompanyTriggerAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtCompanyTriggerAction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param SchemaName Desc: SchemaName   Required: True   Allow empty value : True
      @param DBTableName Desc: DBTableName   Required: True   Allow empty value : True
      @param TriggerType Desc: TriggerType   Required: True   Allow empty value : True
      @param TriggerActionNum Desc: TriggerActionNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerActionRow
   */  
export function get_ExtCompanyTriggerActions_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_TriggerActionNum(Company:string, ExtSystemID:string, ExtCompanyID:string, SchemaName:string, DBTableName:string, TriggerType:string, TriggerActionNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ExtCompanyTriggerActionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerActions(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + "," + TriggerActionNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ExtCompanyTriggerActionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ExtCompanyTriggerAction for the service
   Description: Calls UpdateExt to update ExtCompanyTriggerAction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtCompanyTriggerAction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param SchemaName Desc: SchemaName   Required: True   Allow empty value : True
      @param DBTableName Desc: DBTableName   Required: True   Allow empty value : True
      @param TriggerType Desc: TriggerType   Required: True   Allow empty value : True
      @param TriggerActionNum Desc: TriggerActionNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerActionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ExtCompanyTriggerActions_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_TriggerActionNum(Company:string, ExtSystemID:string, ExtCompanyID:string, SchemaName:string, DBTableName:string, TriggerType:string, TriggerActionNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerActions(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + "," + TriggerActionNum + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete ExtCompanyTriggerAction item
   Description: Call UpdateExt to delete ExtCompanyTriggerAction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtCompanyTriggerAction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param SchemaName Desc: SchemaName   Required: True   Allow empty value : True
      @param DBTableName Desc: DBTableName   Required: True   Allow empty value : True
      @param TriggerType Desc: TriggerType   Required: True   Allow empty value : True
      @param TriggerActionNum Desc: TriggerActionNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ExtCompanyTriggerActions_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_TriggerActionNum(Company:string, ExtSystemID:string, ExtCompanyID:string, SchemaName:string, DBTableName:string, TriggerType:string, TriggerActionNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerActions(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + "," + TriggerActionNum + ")", {
          method: 'delete',
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
   Summary: Calls GetRows for the service
   Description: Get ExtCompanyTriggerConditions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtCompanyTriggerConditions
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtCompanyTriggerConditionRow
   */  
export function get_ExtCompanyTriggerConditions(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyTriggerConditionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditions", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyTriggerConditionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtCompanyTriggerConditions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerConditionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerConditionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExtCompanyTriggerConditions(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditions", {
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
   Summary: Calls GetByID to retrieve the ExtCompanyTriggerCondition item
   Description: Calls GetByID to retrieve the ExtCompanyTriggerCondition item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtCompanyTriggerCondition
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param SchemaName Desc: SchemaName   Required: True   Allow empty value : True
      @param DBTableName Desc: DBTableName   Required: True   Allow empty value : True
      @param TriggerType Desc: TriggerType   Required: True   Allow empty value : True
      @param TriggerConditionGroupNum Desc: TriggerConditionGroupNum   Required: True
      @param TriggerConditionNum Desc: TriggerConditionNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerConditionRow
   */  
export function get_ExtCompanyTriggerConditions_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_TriggerConditionGroupNum_TriggerConditionNum(Company:string, ExtSystemID:string, ExtCompanyID:string, SchemaName:string, DBTableName:string, TriggerType:string, TriggerConditionGroupNum:string, TriggerConditionNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ExtCompanyTriggerConditionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditions(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + "," + TriggerConditionGroupNum + "," + TriggerConditionNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ExtCompanyTriggerConditionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ExtCompanyTriggerCondition for the service
   Description: Calls UpdateExt to update ExtCompanyTriggerCondition. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtCompanyTriggerCondition
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param SchemaName Desc: SchemaName   Required: True   Allow empty value : True
      @param DBTableName Desc: DBTableName   Required: True   Allow empty value : True
      @param TriggerType Desc: TriggerType   Required: True   Allow empty value : True
      @param TriggerConditionGroupNum Desc: TriggerConditionGroupNum   Required: True
      @param TriggerConditionNum Desc: TriggerConditionNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerConditionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ExtCompanyTriggerConditions_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_TriggerConditionGroupNum_TriggerConditionNum(Company:string, ExtSystemID:string, ExtCompanyID:string, SchemaName:string, DBTableName:string, TriggerType:string, TriggerConditionGroupNum:string, TriggerConditionNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditions(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + "," + TriggerConditionGroupNum + "," + TriggerConditionNum + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete ExtCompanyTriggerCondition item
   Description: Call UpdateExt to delete ExtCompanyTriggerCondition item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtCompanyTriggerCondition
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param SchemaName Desc: SchemaName   Required: True   Allow empty value : True
      @param DBTableName Desc: DBTableName   Required: True   Allow empty value : True
      @param TriggerType Desc: TriggerType   Required: True   Allow empty value : True
      @param TriggerConditionGroupNum Desc: TriggerConditionGroupNum   Required: True
      @param TriggerConditionNum Desc: TriggerConditionNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ExtCompanyTriggerConditions_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_TriggerConditionGroupNum_TriggerConditionNum(Company:string, ExtSystemID:string, ExtCompanyID:string, SchemaName:string, DBTableName:string, TriggerType:string, TriggerConditionGroupNum:string, TriggerConditionNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditions(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + "," + TriggerConditionGroupNum + "," + TriggerConditionNum + ")", {
          method: 'delete',
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
   Summary: Calls GetRows for the service
   Description: Get ExtCompanyTriggerConditionDatas items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtCompanyTriggerConditionDatas
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtCompanyTriggerConditionDataRow
   */  
export function get_ExtCompanyTriggerConditionDatas(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyTriggerConditionDataRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditionDatas", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyTriggerConditionDataRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtCompanyTriggerConditionDatas
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerConditionDataRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerConditionDataRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExtCompanyTriggerConditionDatas(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditionDatas", {
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
   Summary: Calls GetByID to retrieve the ExtCompanyTriggerConditionData item
   Description: Calls GetByID to retrieve the ExtCompanyTriggerConditionData item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtCompanyTriggerConditionData
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param SchemaName Desc: SchemaName   Required: True   Allow empty value : True
      @param DBTableName Desc: DBTableName   Required: True   Allow empty value : True
      @param TriggerType Desc: TriggerType   Required: True   Allow empty value : True
      @param TriggerConditionGroupNum Desc: TriggerConditionGroupNum   Required: True
      @param TriggerConditionNum Desc: TriggerConditionNum   Required: True
      @param TriggerConditionDataNum Desc: TriggerConditionDataNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerConditionDataRow
   */  
export function get_ExtCompanyTriggerConditionDatas_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_TriggerConditionGroupNum_TriggerConditionNum_TriggerConditionDataNum(Company:string, ExtSystemID:string, ExtCompanyID:string, SchemaName:string, DBTableName:string, TriggerType:string, TriggerConditionGroupNum:string, TriggerConditionNum:string, TriggerConditionDataNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ExtCompanyTriggerConditionDataRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditionDatas(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + "," + TriggerConditionGroupNum + "," + TriggerConditionNum + "," + TriggerConditionDataNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ExtCompanyTriggerConditionDataRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ExtCompanyTriggerConditionData for the service
   Description: Calls UpdateExt to update ExtCompanyTriggerConditionData. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtCompanyTriggerConditionData
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param SchemaName Desc: SchemaName   Required: True   Allow empty value : True
      @param DBTableName Desc: DBTableName   Required: True   Allow empty value : True
      @param TriggerType Desc: TriggerType   Required: True   Allow empty value : True
      @param TriggerConditionGroupNum Desc: TriggerConditionGroupNum   Required: True
      @param TriggerConditionNum Desc: TriggerConditionNum   Required: True
      @param TriggerConditionDataNum Desc: TriggerConditionDataNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerConditionDataRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ExtCompanyTriggerConditionDatas_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_TriggerConditionGroupNum_TriggerConditionNum_TriggerConditionDataNum(Company:string, ExtSystemID:string, ExtCompanyID:string, SchemaName:string, DBTableName:string, TriggerType:string, TriggerConditionGroupNum:string, TriggerConditionNum:string, TriggerConditionDataNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditionDatas(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + "," + TriggerConditionGroupNum + "," + TriggerConditionNum + "," + TriggerConditionDataNum + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete ExtCompanyTriggerConditionData item
   Description: Call UpdateExt to delete ExtCompanyTriggerConditionData item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtCompanyTriggerConditionData
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtSystemID Desc: ExtSystemID   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param SchemaName Desc: SchemaName   Required: True   Allow empty value : True
      @param DBTableName Desc: DBTableName   Required: True   Allow empty value : True
      @param TriggerType Desc: TriggerType   Required: True   Allow empty value : True
      @param TriggerConditionGroupNum Desc: TriggerConditionGroupNum   Required: True
      @param TriggerConditionNum Desc: TriggerConditionNum   Required: True
      @param TriggerConditionDataNum Desc: TriggerConditionDataNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ExtCompanyTriggerConditionDatas_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_TriggerConditionGroupNum_TriggerConditionNum_TriggerConditionDataNum(Company:string, ExtSystemID:string, ExtCompanyID:string, SchemaName:string, DBTableName:string, TriggerType:string, TriggerConditionGroupNum:string, TriggerConditionNum:string, TriggerConditionDataNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditionDatas(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + "," + TriggerConditionGroupNum + "," + TriggerConditionNum + "," + TriggerConditionDataNum + ")", {
          method: 'delete',
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtCompanyListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyListRow)
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
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseExtCompany:string, whereClauseExtCompanyAttch:string, whereClauseExtCompanyECC:string, whereClauseECCDocType:string, whereClauseECCReportDefaultStyle:string, whereClauseExtPlant:string, whereClauseExtWarehouse:string, whereClauseEntityGLC:string, whereClauseExtCompanyTriggerDef:string, whereClauseExtCompanyTriggerConditionGrp:string, whereClauseExtCompanyTriggerAction:string, whereClauseExtCompanyTriggerCondition:string, whereClauseExtCompanyTriggerConditionData:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseExtCompany!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseExtCompany=" + whereClauseExtCompany
   }
   if(typeof whereClauseExtCompanyAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseExtCompanyAttch=" + whereClauseExtCompanyAttch
   }
   if(typeof whereClauseExtCompanyECC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseExtCompanyECC=" + whereClauseExtCompanyECC
   }
   if(typeof whereClauseECCDocType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseECCDocType=" + whereClauseECCDocType
   }
   if(typeof whereClauseECCReportDefaultStyle!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseECCReportDefaultStyle=" + whereClauseECCReportDefaultStyle
   }
   if(typeof whereClauseExtPlant!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseExtPlant=" + whereClauseExtPlant
   }
   if(typeof whereClauseExtWarehouse!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseExtWarehouse=" + whereClauseExtWarehouse
   }
   if(typeof whereClauseEntityGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEntityGLC=" + whereClauseEntityGLC
   }
   if(typeof whereClauseExtCompanyTriggerDef!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseExtCompanyTriggerDef=" + whereClauseExtCompanyTriggerDef
   }
   if(typeof whereClauseExtCompanyTriggerConditionGrp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseExtCompanyTriggerConditionGrp=" + whereClauseExtCompanyTriggerConditionGrp
   }
   if(typeof whereClauseExtCompanyTriggerAction!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseExtCompanyTriggerAction=" + whereClauseExtCompanyTriggerAction
   }
   if(typeof whereClauseExtCompanyTriggerCondition!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseExtCompanyTriggerCondition=" + whereClauseExtCompanyTriggerCondition
   }
   if(typeof whereClauseExtCompanyTriggerConditionData!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseExtCompanyTriggerConditionData=" + whereClauseExtCompanyTriggerConditionData
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/GetRows" + params, {
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
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(extSystemID:string, extCompanyID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof extSystemID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "extSystemID=" + extSystemID
   }
   if(typeof extCompanyID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "extCompanyID=" + extCompanyID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/GetByID" + params, {
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
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      @param whereClause Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      @param pageSize Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      @param absolutePage Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetList(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClause!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClause=" + whereClause
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/GetList" + params, {
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
   Summary: Invoke method GetCodeDescList
   Description: To return the CodeDescriptionList values of a given table.field.
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/GetCodeDescList", {
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
   Summary: Invoke method GetECCReportServiceDescList
   Description: Method to call to get a Code Description list.
   OperationID: GetECCReportServiceDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetECCReportServiceDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetECCReportServiceDescList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/GetECCReportServiceDescList", {
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
   Summary: Invoke method ConvertToMultiCompanyDirect
   Description: Convert this ExtCompany record from Sonic to Direct
   OperationID: ConvertToMultiCompanyDirect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConvertToMultiCompanyDirect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvertToMultiCompanyDirect_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConvertToMultiCompanyDirect(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ConvertToMultiCompanyDirect", {
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
   Summary: Invoke method ConvertToMultiCompanyServiceBus
   Description: Convert this ExtCompany record from Direct to Sonic
   OperationID: ConvertToMultiCompanyServiceBus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConvertToMultiCompanyServiceBus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvertToMultiCompanyServiceBus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConvertToMultiCompanyServiceBus(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ConvertToMultiCompanyServiceBus", {
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
   Summary: Invoke method CreateXSDSchemas
   Description: CreateXSDSchemas
   OperationID: CreateXSDSchemas
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateXSDSchemas_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateXSDSchemas_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateXSDSchemas(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/CreateXSDSchemas", {
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
   Summary: Invoke method WriteXSDSchemasToServer
   Description: Write schema files to the proposed location on the server
   OperationID: WriteXSDSchemasToServer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WriteXSDSchemasToServer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WriteXSDSchemasToServer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WriteXSDSchemasToServer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/WriteXSDSchemasToServer", {
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
   Summary: Invoke method CustomerConnect
   Description: Customer Connect
   OperationID: CustomerConnect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomerConnect_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CustomerConnect(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/CustomerConnect", {
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
   Summary: Invoke method EntPrsConf
   Description: Enterprise Configurator
   OperationID: EntPrsConf
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/EntPrsConf_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EntPrsConf(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/EntPrsConf", {
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
   Summary: Invoke method ChangedReportService
   Description: This method populate Report list when Report. AutoProgram Changed
   OperationID: ChangedReportService
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedReportService_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedReportService_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangedReportService(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ChangedReportService", {
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
   Summary: Invoke method ValidateReportService
   Description: This method validate Report Service make sure that it's unique
   OperationID: ValidateReportService
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateReportService_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateReportService_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateReportService(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ValidateReportService", {
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
   Summary: Invoke method ChangedReportID
   Description: This method populate Report Style list when Report ID Changed
   OperationID: ChangedReportID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedReportID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedReportID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangedReportID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ChangedReportID", {
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
   Summary: Invoke method ChangedStyleNum
   OperationID: ChangedStyleNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedStyleNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedStyleNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangedStyleNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ChangedStyleNum", {
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
   Summary: Invoke method ECCAttachmentAccessRisk
   Description: Method to establish if the attachment configuration is a risk for ECC
If the Attachment Type or Document Type records have a client based transfer a warning will be given if selected.
   OperationID: ECCAttachmentAccessRisk
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ECCAttachmentAccessRisk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ECCAttachmentAccessRisk_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECCAttachmentAccessRisk(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ECCAttachmentAccessRisk", {
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
   Summary: Invoke method FSA
   Description: FSA
   OperationID: FSA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/FSA_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FSA(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/FSA", {
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
   Summary: Invoke method Generic
   Description: Generic
   OperationID: Generic
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Generic_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Generic(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/Generic", {
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
   Summary: Invoke method InitEntprsConf
   Description: This method initializes/sends the enterprise configurator records for the
specified ExtCompanyID
   OperationID: InitEntprsConf
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InitEntprsConf_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InitEntprsConf_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InitEntprsConf(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/InitEntprsConf", {
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
   Summary: Invoke method InitMultiCompany
   Description: This method initializes/sends the applicable GL data for the specified ExtCompanyID
   OperationID: InitMultiCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InitMultiCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InitMultiCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InitMultiCompany(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/InitMultiCompany", {
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
   Summary: Invoke method InitCOA
   Description: This method initializes/sends the applicable COA/GL data for the specified ExtCompanyID
   OperationID: InitCOA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InitCOA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InitCOA_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InitCOA(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/InitCOA", {
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
   Summary: Invoke method InitConsolidationMonitor
   Description: This method Initialize/Send Consolidation data for the specified ExtCompanyID
   OperationID: InitConsolidationMonitor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InitConsolidationMonitor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InitConsolidationMonitor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InitConsolidationMonitor(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/InitConsolidationMonitor", {
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
   Summary: Invoke method Mobile
   Description: Mobile
   OperationID: Mobile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Mobile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Mobile(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/Mobile", {
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
   Summary: Invoke method MultiCompany
   Description: Multi Company
   OperationID: MultiCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/MultiCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MultiCompany(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/MultiCompany", {
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
   Summary: Invoke method OnChangeECCSiteName
   Description: Validate if existing ECCExtended records exist.
The ECCExtended record holds information on the originating site use for creating Order, Quotes, RMAs.
   OperationID: OnChangeECCSiteName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeECCSiteName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeECCSiteName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeECCSiteName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/OnChangeECCSiteName", {
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
   Summary: Invoke method OnChangeLocation
   Description: OnChangeLocation
   OperationID: OnChangeLocation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeLocation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLocation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeLocation(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/OnChangeLocation", {
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
   Summary: Invoke method OnChangeTriggerDefTableName
   Description: OnChangeTriggerDefTableName
   OperationID: OnChangeTriggerDefTableName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTriggerDefTableName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTriggerDefTableName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTriggerDefTableName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/OnChangeTriggerDefTableName", {
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
   Summary: Invoke method PLM
   Description: PLM
   OperationID: PLM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/PLM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PLM(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/PLM", {
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
   Summary: Invoke method SupplierConnect
   Description: Supplier Connect
   OperationID: SupplierConnect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/SupplierConnect_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SupplierConnect(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/SupplierConnect", {
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
   Summary: Invoke method TestConnection
   Description: Test Connection
   OperationID: TestConnection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TestConnection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestConnection_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TestConnection(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/TestConnection", {
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
   Summary: Invoke method TestECCConnection
   Description: Test ECC Conneciont
   OperationID: TestECCConnection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TestECCConnection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestECCConnection_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TestECCConnection(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/TestECCConnection", {
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
   Summary: Invoke method GetNewExtCompany
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewExtCompany(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/GetNewExtCompany", {
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
   Summary: Invoke method GetNewExtCompanyAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtCompanyAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtCompanyAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtCompanyAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewExtCompanyAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/GetNewExtCompanyAttch", {
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
   Summary: Invoke method GetNewExtCompanyECC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtCompanyECC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtCompanyECC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtCompanyECC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewExtCompanyECC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/GetNewExtCompanyECC", {
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
   Summary: Invoke method GetNewECCDocType
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECCDocType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECCDocType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECCDocType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECCDocType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/GetNewECCDocType", {
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
   Summary: Invoke method GetNewECCReportDefaultStyle
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECCReportDefaultStyle
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECCReportDefaultStyle_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECCReportDefaultStyle_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECCReportDefaultStyle(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/GetNewECCReportDefaultStyle", {
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
   Summary: Invoke method GetNewExtPlant
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewExtPlant(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/GetNewExtPlant", {
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
   Summary: Invoke method GetNewExtWarehouse
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtWarehouse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtWarehouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewExtWarehouse(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/GetNewExtWarehouse", {
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
   Summary: Invoke method GetNewEntityGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEntityGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEntityGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEntityGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEntityGLC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/GetNewEntityGLC", {
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
   Summary: Invoke method GetNewExtCompanyTriggerDef
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtCompanyTriggerDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtCompanyTriggerDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtCompanyTriggerDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewExtCompanyTriggerDef(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/GetNewExtCompanyTriggerDef", {
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
   Summary: Invoke method GetNewExtCompanyTriggerConditionGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtCompanyTriggerConditionGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtCompanyTriggerConditionGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtCompanyTriggerConditionGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewExtCompanyTriggerConditionGrp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/GetNewExtCompanyTriggerConditionGrp", {
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
   Summary: Invoke method GetNewExtCompanyTriggerAction
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtCompanyTriggerAction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtCompanyTriggerAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtCompanyTriggerAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewExtCompanyTriggerAction(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/GetNewExtCompanyTriggerAction", {
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
   Summary: Invoke method GetNewExtCompanyTriggerCondition
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtCompanyTriggerCondition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtCompanyTriggerCondition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtCompanyTriggerCondition_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewExtCompanyTriggerCondition(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/GetNewExtCompanyTriggerCondition", {
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
   Summary: Invoke method GetNewExtCompanyTriggerConditionData
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtCompanyTriggerConditionData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtCompanyTriggerConditionData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtCompanyTriggerConditionData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewExtCompanyTriggerConditionData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/GetNewExtCompanyTriggerConditionData", {
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
   Description: Deletes a row given its ID.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/DeleteByID", {
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
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowID(id:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof id!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "id=" + id
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/GetBySysRowID" + params, {
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
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowIDs(ids:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof ids!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ids=" + ids
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/GetBySysRowIDs" + params, {
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
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/Update", {
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
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECCDocTypeRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECCDocTypeRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECCReportDefaultStyleRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECCReportDefaultStyleRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EntityGLCRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ExtCompanyAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyECCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ExtCompanyECCRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ExtCompanyListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ExtCompanyRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyTriggerActionRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ExtCompanyTriggerActionRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyTriggerConditionDataRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ExtCompanyTriggerConditionDataRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyTriggerConditionGrpRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ExtCompanyTriggerConditionGrpRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyTriggerConditionRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ExtCompanyTriggerConditionRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyTriggerDefRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ExtCompanyTriggerDefRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPlantRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ExtPlantRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtWarehouseRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ExtWarehouseRow[],
}

export interface Erp_Tablesets_ECCDocTypeRow{
      /**  Company  */  
   "Company":string,
      /**  The ID of the interfaced company  */  
   "ExtCompanyID":string,
      /**  Code for the external package to be interfaced with.  */  
   "ExtSystemID":string,
      /**  Unique ID.  */  
   "ECCID":number,
      /**  Unique identifier of a DocType.  By selecting this Doc Type all related attachments will be viewable on the web.  */  
   "DocTypeID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "DocTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ECCReportDefaultStyleRow{
      /**  Company identifier.  */  
   "Company":string,
      /**  The ID of the interfaced company  */  
   "ExtCompanyID":string,
      /**  Code for the external package to be interfaced with.  */  
   "ExtSystemID":string,
      /**  Unique ID.  */  
   "ECCID":number,
      /**  Name of the BL program file used as a broker when auto-printing Crystal Reports or Bartender Labels from a BAM.  */  
   "AutoProgram":string,
      /**  Report ID  */  
   "ReportID":string,
      /**  Report Style Number.  */  
   "StyleNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "StyleList":string,
   "RptDescription":string,
   "StyleDescription":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_EntityGLCRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  */  
   "Key1":string,
      /**   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  */  
   "Key2":string,
      /**   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key3":string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key4":string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key5":string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key6":string,
      /**  Identifier of the GL Control Type.  */  
   "GLControlType":string,
      /**  GL Control Identifier.  */  
   "GLControlCode":string,
      /**  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  */  
   "BusinessEntity":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   "IsExternalCompany":boolean,
      /**  Marks this EntityGLC as global, available to be sent out to other companies.  */  
   "GlobalEntityGLC":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  BankAcctID of the related BankAcct record.  */  
   "BankAcctID":string,
   "BankFeeID":string,
      /**  CallCode of the related FSCallCd record.  */  
   "CallCode":string,
   "ChargeCode":string,
      /**  ClassCode of the related FAClass record.  */  
   "ClassCode":string,
      /**  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  */  
   "ClassID":string,
      /**  ContractCode of the related FSContCd record.  */  
   "ContractCode":string,
      /**  CurrencyCode of the related Currency record.  */  
   "CurrencyCode":string,
      /**  CustNum of the related Customer record  */  
   "CustNum":number,
      /**  DeductionID of PRClsDed or PRDeduct.  */  
   "DeductionID":string,
      /**  EmpID of the related PREmpMas record.  */  
   "EmpID":string,
      /**  ExpenseCode of PayTLbr, LabExpCd  */  
   "ExpenseCode":string,
      /**  ExtSystemID of ExtCompany table  */  
   "ExtSystemID":string,
      /**  FromPlant value of the related PlntTranDef record.  */  
   "FromPlant":string,
      /**  GroupCode of the related FAGroup record.  */  
   "GroupCode":string,
   "GroupID":string,
   "HeadNum":number,
   "InvoiceNum":string,
      /**  JCDept of the related JCDept record.  */  
   "JCDept":string,
      /**  MiscCode of the related MiscChrg or PurMisc record.  */  
   "MiscCode":string,
      /**  PartNum of the related Part record.  */  
   "PartNum":string,
      /**  PayTypeID of PayType  */  
   "PayTypeID":string,
   "PerConName":string,
      /**  PI Status  */  
   "PIStatus":string,
      /**  Plant of the related PlantConfCtrl record.  */  
   "Plant":string,
      /**  ProdCode of the related ProdGrup record.  */  
   "ProdCode":string,
      /**  ProjectID of the related Project record.  */  
   "ProjectID":string,
      /**  PurchCode of the related GLPurch record.  */  
   "PurchCode":string,
      /**  RateCode of the related GLRate record.  */  
   "RateCode":string,
      /**  ReasonCode of the related Reason record.  */  
   "ReasonCode":string,
      /**  ReasonType of the related Reason record.  */  
   "ReasonType":string,
      /**  SalesCatID of the related SalesCat record.  */  
   "SalesCatID":string,
      /**  Shift value of the related JCShift record.  */  
   "Shift":number,
      /**  TaxCode of the related SalesTax record.  */  
   "TaxCode":string,
      /**  TaxTblID of PRTaxMas or PRClsTax.  */  
   "TaxTblID":string,
      /**  ToPlant value of the related PlntTranDef record.  */  
   "ToPlant":string,
      /**  TransferMethod of ExtCompany table  */  
   "TransferMethod":string,
      /**  Type ID  */  
   "TypeID":string,
      /**  VendorNum of the related Vendor record.  */  
   "VendorNum":number,
      /**  WarehouseCode of the related Warehse record.  */  
   "WarehouseCode":string,
   "ExpenseTypeCode":string,
   "IsFiltered":boolean,
   "OprTypeCode":string,
   "CashDeskID":string,
   "TIN":string,
   "ReclassCodeID":string,
   "BitFlag":number,
   "GLCntrlDescription":string,
   "GLCntrlTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ExtCompanyAttchRow{
   "Company":string,
   "ExtSystemID":string,
   "ExtCompanyID":string,
   "DrawingSeq":number,
   "XFileRefNum":number,
   "SysRevID":number,
   "SysRowID":string,
   "ForeignSysRowID":string,
   "DrawDesc":string,
   "FileName":string,
   "PDMDocID":string,
   "DocTypeID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ExtCompanyECCRow{
      /**  Company  */  
   "Company":string,
      /**  The ID of the interfaced company.  */  
   "ExtCompanyID":string,
      /**  Code for the external package to be interfaced with.  */  
   "ExtSystemID":string,
      /**  Unique ID.  */  
   "ECCID":number,
      /**  URL for ECC uploads  */  
   "ECCURL":string,
      /**  ECC Password  */  
   "ECCPassword":string,
      /**  User ID  */  
   "DefaultEpicorUserID":string,
      /**  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  */  
   "DefaultEpicorCustNum":number,
      /**  Miscellaneous charge code for ECC shipping charges  */  
   "DefaultMiscChargeCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Miscellaneous charge code for ECC discount  */  
   "DefaultDiscountCode":string,
      /**  Link To Task set  */  
   "TaskSetID":string,
      /**  Inbound attachments from the web will be related to this Doc Type.  */  
   "DocTypeID":string,
      /**  Customer ID prefix that all new customers created by the CNC message will begin with, followed by an incremented number.  */  
   "CNCPrefix":string,
      /**  Incremented sequence that will be added to the prefix to create unique Customer IDs for all new customers created from CNC message.  */  
   "CNCSeq":number,
      /**  Specifies the length of time, in seconds, that the sync waits for a response from ECC web site.  */  
   "TimeOutLimit":number,
      /**  Specifies the number of times the sync will attempt to reprocess a previous failed sync.  */  
   "RecycleLimit":number,
      /**  Use Location or use the standard Brand Site.  */  
   "UseLocation":boolean,
      /**  ECC Site Name, needs to match what is setup in ECC.  */  
   "ECCSiteName":string,
      /**  Link to Work Flow Group  */  
   "WFGroupID":string,
      /**  Specifies the cash group prefix for ECC payments. All of the ECC payment cash groups are grouped together using this user-defined prefix.  */  
   "BTCashGrpPfx":string,
      /**  Select the default bank to be used for ECC payments from the list of available banks.  */  
   "BTDefBankAcctID":string,
      /**  Select this checkbox to indicate Default Documents will be viewable on the web.  Only Default Documents of type File System Document will be supported.  */  
   "ViewDefaultDoc":boolean,
      /**  Specifies the A/R invoice group prefix for all ECC payments. All of the ECC payment invoices are grouped together, separate from other shipments using this user-defined prefix.  */  
   "InvcGrpPfx":string,
      /**  Select this option to send populated part attributes to ECC  */  
   "SendPartAttribute":boolean,
      /**  True when company Allow default document is enabled and the method is File System.  */  
   "EnableDefDocsViewable":boolean,
      /**  ECC Masked password field  */  
   "ECCPasswordMasked":string,
   "BitFlag":number,
   "BankAcctIDBankName":string,
   "BankAcctIDDescription":string,
   "CustomerCustID":string,
   "CustomerBTName":string,
   "CustomerName":string,
   "CustomerInactive":boolean,
   "DiscountCodeDescription":string,
   "DocTypeDescription":string,
   "MiscCodeDescription":string,
   "TaskSetWorkflowType":string,
   "TaskSetTaskSetDescription":string,
   "UserIDName":string,
   "WFGroupIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ExtCompanyListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Code for the external package to be interfaced with  */  
   "ExtSystemID":string,
      /**  The ID of the interfaced company  */  
   "ExtCompanyID":string,
      /**  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  */  
   "TransferMethod":string,
      /**  Customers will be sent . CustomerType = "CUS". Init YES  */  
   "SendCustomer":boolean,
      /**  Prospects will be sent . CustomerType = "PRO". Init YES  */  
   "SendProspect":boolean,
      /**  Suspects  will be sent. CustomerType = "SUS". Init NO  */  
   "SendSuspect":boolean,
      /**  Vendors will be sent .  Init YES  */  
   "SendVend":boolean,
      /**  Parts will be sent.  Init NO (Future USE)  */  
   "SendPart":boolean,
      /**  Shipments will be sent .  Init YES  */  
   "SendShip":boolean,
      /**  AR Invoices will be sent .  Init YES  */  
   "SendARInv":boolean,
      /**  AR Invoices will be received .  Init YES  */  
   "RcvARInv":boolean,
      /**  AP Invoices will be sent .  Init YES  */  
   "SendAPInv":boolean,
      /**  AP Invoices will be received .  Init YES  */  
   "RcvAPInv":boolean,
      /**  If box is checked, then the AP Invoice system will enable the APInvDtl.PurchCode field for European Financial postings  */  
   "APPurchType":boolean,
      /**  For this interface, should acknowledgments be sent back to the interfaced software when a record is received into the intermediate tables?  */  
   "SendAckToQue":boolean,
      /**  Indicates if this external company setup supports Inter-Company Trading.  */  
   "ICTrading":boolean,
      /**  A  unique integer assigned by the system to identify the Vendor participating in the Inter-Company Trading.  */  
   "ICVendorNum":number,
      /**  A  unique integer assigned by the system to identify the Customer participating in the Inter-Company Trading.  */  
   "ICCustNum":number,
      /**  A user defined external customer ID.  Identifies the External Customer participating in the Inter-Company Trading.  */  
   "ExtCustID":string,
      /**  A user defined external vendor ID.  Identifies the External Vendor participating in the Inter-Company Trading.  */  
   "ExtVendorID":string,
      /**  Indicates that the discount amount by line needs to be captured to be sent to the Financials package  */  
   "APDiscount":boolean,
      /**  The type of program being called (ProgressProgram or WindowsProgram)  */  
   "AuxPrgmType":string,
      /**  Name of Auxiliary program to run to alert external system that there are records ready for processing  */  
   "AuxPrgmName":string,
      /**  New PO Suggestions will be sent.  */  
   "SendPOSugg":boolean,
      /**  Number of days it will take to transfer an order from one company to the other.  Only for Inter-Company traders.  Will subtract this number from the po need by date to get the correct need by date on the order side.  Controlled on the Order side (po due-date - transfertime = orderdate)  */  
   "TransferDays":number,
      /**  Size of blocks for POHeader.PONum to be generated for this Consolidated Purchasing Company.  */  
   "PONumBlockSize":number,
      /**  When a Consolidated Purchasing Company requests a new block because their portion of their POHeader.PONum block is less than this Reorder Point, create a new block and send it out.  */  
   "PONumBlockReorderPoint":number,
      /**  When a Consolidated Purchasing Company creates a Purchase Order and the number of allocated PONum values drops below this warning point, message the user to inform them.  */  
   "PONumBlockWarnPoint":number,
      /**  Establishes the default ExtSite.ExtSiteID to be used as the default for a Site field during creation of a Consolidated Purchase Order Release.  */  
   "DefaultPlant":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Send G/L Accounts for Multi-Company Journal.  */  
   "SendGLAccounts":boolean,
      /**  Indicates if the current company is allowed to send Multi-Company General Journals to this external company.  */  
   "AllowGJAlloc":boolean,
      /**  Indicates if the current company is allowed to send Multi-Company AP G/L entries to this external company.  */  
   "AllowAPAlloc":boolean,
      /**  The Journal Group prefix to use when determining the group ID for the Multi-Company Journals coming from this external company.  */  
   "JrnGroupPrefix":string,
      /**  Flag to indicate if the Multi-Company Journals coming from this external company needs to be posted automatically.  */  
   "AutoPostGJ":boolean,
      /**  The Journal Code to use to enter Multi-Company Journals from this external company.  */  
   "JournalCode":string,
      /**  The default Invoice Group Prefix that will be used by Centralized Payment process.  */  
   "CPayGroupPrefix":string,
      /**  The flag to indicate if invoices flagged for Centralized Payment from external company will be posted automatically.  */  
   "CPayAutoPost":boolean,
      /**   This field will indicate how Legal Number will be generated.  The valid options are:
'O'  -  Use Original Legal Number from the source invoice prefixed with the Source Company ID; 
'N'  -  Generate New Legal Number using the current company's Legal Number rules.  */  
   "CPayLegalNum":string,
      /**  When receiving global customers, try to create/link the Part without human intervention  */  
   "AutoLoadCust":boolean,
      /**  When receiving global vendors, try to create/link a vendor without human intervention  */  
   "AutoLoadVend":boolean,
      /**  When receiving Global Parts, try to create/link a Part without human intervention  */  
   "AutoLoadPart":boolean,
      /**  Part revisions will be sent.  Init NO (Future USE)  */  
   "SendRev":boolean,
      /**  PerCon will be sent.  */  
   "SendPerCon":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "AllowAPPurchType":boolean,
      /**  Flag to indicate when to enable the CPay Group Prefix.  */  
   "EnableCPayGroup":boolean,
      /**  Flag to indicate when to enable the CPay Legal Number combo  */  
   "EnableCPayLegal":boolean,
      /**  Flag to indicate if the External Company is the Central Payment Parent Company.  */  
   "DispCPayParent":boolean,
      /**  Flag to indicate when to enable the AR Intercompany Account button.  */  
   "EnableARIntercompany":boolean,
      /**  Full Name of external package  */  
   "ExtSystemExtSystemName":string,
      /**  Journal  Description.  */  
   "JournalCodeJrnlDescription":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "LinkCustomerBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "LinkCustomerCustID":string,
      /**  The full name of the customer.  */  
   "LinkCustomerName":string,
      /**  First address line of the Supplier  */  
   "LinkVendorAddress1":string,
      /**  City portion of the address of the Supplier  */  
   "LinkVendorCity":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "LinkVendorDefaultFOB":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "LinkVendorTermsCode":string,
      /**  Second address line of the Supplier  */  
   "LinkVendorAddress2":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "LinkVendorCountry":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "LinkVendorName":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "LinkVendorVendorID":string,
      /**  Third address line of the Supplier  */  
   "LinkVendorAddress3":string,
      /**  A unique code that identifies the currency.  */  
   "LinkVendorCurrencyCode":string,
      /**  Can be blank.  */  
   "LinkVendorState":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "LinkVendorZIP":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ExtCompanyRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Code for the external package to be interfaced with  */  
   "ExtSystemID":string,
      /**  The ID of the interfaced company  */  
   "ExtCompanyID":string,
      /**  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  */  
   "TransferMethod":string,
      /**  CompanyCountryLangNameID  */  
   "CompanyCountryLangNameID":string,
      /**  Customers will be sent . CustomerType = "CUS". Init YES  */  
   "SendCustomer":boolean,
      /**  Prospects will be sent . CustomerType = "PRO". Init YES  */  
   "SendProspect":boolean,
      /**  Suspects  will be sent. CustomerType = "SUS". Init NO  */  
   "SendSuspect":boolean,
      /**  Vendors will be sent .  Init YES  */  
   "SendVend":boolean,
      /**  Parts will be sent.  Init NO (Future USE)  */  
   "SendPart":boolean,
      /**  Shipments will be sent .  Init YES  */  
   "SendShip":boolean,
      /**  AR Invoices will be sent .  Init YES  */  
   "SendARInv":boolean,
      /**  AR Invoices will be received .  Init YES  */  
   "RcvARInv":boolean,
      /**  AP Invoices will be sent .  Init YES  */  
   "SendAPInv":boolean,
      /**  AP Invoices will be received .  Init YES  */  
   "RcvAPInv":boolean,
      /**  If box is checked, then the AP Invoice system will enable the APInvDtl.PurchCode field for European Financial postings  */  
   "APPurchType":boolean,
      /**  For this interface, should acknowledgments be sent back to the interfaced software when a record is received into the intermediate tables?  */  
   "SendAckToQue":boolean,
      /**  Indicates if this external company setup supports Inter-Company Trading.  */  
   "ICTrading":boolean,
      /**  A  unique integer assigned by the system to identify the Vendor participating in the Inter-Company Trading.  */  
   "ICVendorNum":number,
      /**  A  unique integer assigned by the system to identify the Customer participating in the Inter-Company Trading.  */  
   "ICCustNum":number,
      /**  A user defined external customer ID.  Identifies the External Customer participating in the Inter-Company Trading.  */  
   "ExtCustID":string,
      /**  A user defined external vendor ID.  Identifies the External Vendor participating in the Inter-Company Trading.  */  
   "ExtVendorID":string,
      /**  Indicates that the discount amount by line needs to be captured to be sent to the Financials package  */  
   "APDiscount":boolean,
      /**  The type of program being called (ProgressProgram or WindowsProgram)  */  
   "AuxPrgmType":string,
      /**  Name of Auxiliary program to run to alert external system that there are records ready for processing  */  
   "AuxPrgmName":string,
      /**  New PO Suggestions will be sent.  */  
   "SendPOSugg":boolean,
      /**  Last date the connection was made successfully  */  
   "LastConDate":string,
      /**  Last Time the connection was made successfully  */  
   "LastConTime":number,
      /**  last date the connection was attempted and failed  */  
   "LastFailedDate":string,
      /**  Last time the connection was tried and failed  */  
   "LastFailedTime":number,
      /**  Number of days it will take to transfer an order from one company to the other.  Only for Inter-Company traders.  Will subtract this number from the po need by date to get the correct need by date on the order side.  Controlled on the Order side (po due-date - transfertime = orderdate)  */  
   "TransferDays":number,
      /**  Size of blocks for POHeader.PONum to be generated for this Consolidated Purchasing Company.  */  
   "PONumBlockSize":number,
      /**  When a Consolidated Purchasing Company requests a new block because their portion of their POHeader.PONum block is less than this Reorder Point, create a new block and send it out.  */  
   "PONumBlockReorderPoint":number,
      /**  When a Consolidated Purchasing Company creates a Purchase Order and the number of allocated PONum values drops below this warning point, message the user to inform them.  */  
   "PONumBlockWarnPoint":number,
      /**  Establishes the default ExtSite.ExtSiteID to be used as the default for a Site field during creation of a Consolidated Purchase Order Release.  */  
   "DefaultPlant":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Send G/L Accounts for Multi-Company Journal.  */  
   "SendGLAccounts":boolean,
      /**  Indicates if the current company is allowed to send Multi-Company General Journals to this external company.  */  
   "AllowGJAlloc":boolean,
      /**  Indicates if the current company is allowed to send Multi-Company AP G/L entries to this external company.  */  
   "AllowAPAlloc":boolean,
      /**  The Journal Group prefix to use when determining the group ID for the Multi-Company Journals coming from this external company.  */  
   "JrnGroupPrefix":string,
      /**  Flag to indicate if the Multi-Company Journals coming from this external company needs to be posted automatically.  */  
   "AutoPostGJ":boolean,
      /**  The Journal Code to use to enter Multi-Company Journals from this external company.  */  
   "JournalCode":string,
      /**  The default Invoice Group Prefix that will be used by Centralized Payment process.  */  
   "CPayGroupPrefix":string,
      /**  The flag to indicate if invoices flagged for Centralized Payment from external company will be posted automatically.  */  
   "CPayAutoPost":boolean,
      /**   This field will indicate how Legal Number will be generated.  The valid options are:
'O'  -  Use Original Legal Number from the source invoice prefixed with the Source Company ID; 
'N'  -  Generate New Legal Number using the current company's Legal Number rules.  */  
   "CPayLegalNum":string,
      /**  When receiving global customers, try to create/link the Part without human intervention  */  
   "AutoLoadCust":boolean,
      /**  When receiving global vendors, try to create/link a vendor without human intervention  */  
   "AutoLoadVend":boolean,
      /**  When receiving Global Parts, try to create/link a Part without human intervention  */  
   "AutoLoadPart":boolean,
      /**  Part revisions will be sent.  Init NO (Future USE)  */  
   "SendRev":boolean,
      /**  PerCon will be sent.  */  
   "SendPerCon":boolean,
      /**  MCSegOnly  */  
   "MCSegOnly":boolean,
      /**  SendConfigurator  */  
   "SendConfigurator":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Turns Global COA on  */  
   "SendGlobalCOA":boolean,
      /**  Indicates how much of the COA supporting structure to send. seg`Send Segments Only~coa`Send Full COA  */  
   "SendGlobalCOAType":string,
      /**  It is used for rules of creation offsetting GL inter-company lines in multi-company process. If it is checked the journal will have an offsetting line with inter-company account for each multi-company line.  */  
   "AlwaysUseGLInterComp":boolean,
      /**  The default Invoice Group Prefix that will be used by Centralized Collection process.  */  
   "CColGroupPrefix":string,
      /**  This field will indicate how Legal Number will be generated for Central Collection invoices.  The valid options are: 'O'  -  Use Original Legal Number from the source invoice prefixed with the Source Company ID; 'N'  -  Generate New Legal Number using the current company's Legal Number rules.  */  
   "CColCPayLegalNum":string,
      /**  Dynamic Attributes will be sent.  Init NO  */  
   "SendDynAttr":boolean,
      /**  Dynamic Attributes will be received.  Init NO  */  
   "RcvDynAttr":boolean,
      /**  Flag to indicate if the External Company is the Central Payment Parent Company.  */  
   "DispCPayParent":boolean,
      /**  Flag to indicate when to enable the AR Intercompany Account button.  */  
   "EnableARIntercompany":boolean,
   "EnableConvertToDirect":boolean,
   "EnableConvertToSonic":boolean,
      /**  Flag to indicate when to enable the CPay Group Prefix.  */  
   "EnableCPayGroup":boolean,
      /**  Flag to indicate when to enable the CPay Legal Number combo  */  
   "EnableCPayLegal":boolean,
      /**  Name or description of the external company.  */  
   "ExtCompanyName":string,
   "ExtSystemIDTransferMethod":string,
   "AllowAPPurchType":boolean,
      /**  Flag to indicate when to enable the Central Collection Legal Number  */  
   "EnableCColCPayLegalNum":boolean,
      /**  Flag to indicate when to enable the Central Collection Group Prefix.  */  
   "EnableCColGroupPrefix":boolean,
   "BitFlag":number,
   "ExtSystemExtSystemName":string,
   "JournalCodeJrnlDescription":string,
   "LinkCustomerName":string,
   "LinkCustomerBTName":string,
   "LinkCustomerCustID":string,
   "LinkCustomerInactive":boolean,
   "LinkVendorAddress1":string,
   "LinkVendorCity":string,
   "LinkVendorDefaultFOB":string,
   "LinkVendorTermsCode":string,
   "LinkVendorAddress2":string,
   "LinkVendorCountry":string,
   "LinkVendorName":string,
   "LinkVendorVendorID":string,
   "LinkVendorAddress3":string,
   "LinkVendorCurrencyCode":string,
   "LinkVendorState":string,
   "LinkVendorZIP":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ExtCompanyTriggerActionRow{
      /**  Company  */  
   "Company":string,
      /**  ExtSystemID  */  
   "ExtSystemID":string,
      /**  ExtCompanyID  */  
   "ExtCompanyID":string,
      /**  SchemaName  */  
   "SchemaName":string,
      /**  DBTableName  */  
   "DBTableName":string,
      /**  TriggerType  */  
   "TriggerType":string,
      /**  TriggerActionNum  */  
   "TriggerActionNum":number,
      /**  ActionType  */  
   "ActionType":string,
      /**  WorkflowName  */  
   "WorkflowName":string,
      /**  ActionIsAsynchronous  */  
   "ActionIsAsynchronous":boolean,
      /**  ExtCompCharacter01  */  
   "ExtCompCharacter01":string,
      /**  ExtCompCharacter02  */  
   "ExtCompCharacter02":string,
      /**  ExtCompBoolean01  */  
   "ExtCompBoolean01":boolean,
      /**  ExtCompBoolean02  */  
   "ExtCompBoolean02":boolean,
      /**  ExtCompDateTime01  */  
   "ExtCompDateTime01":string,
      /**  ExtCompDateTime02  */  
   "ExtCompDateTime02":string,
      /**  ExtCompInteger01  */  
   "ExtCompInteger01":number,
      /**  ExtCompInteger02  */  
   "ExtCompInteger02":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "IsUpdatable":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ExtCompanyTriggerConditionDataRow{
      /**  Company  */  
   "Company":string,
      /**  ExtSystemID  */  
   "ExtSystemID":string,
      /**  ExtCompanyID  */  
   "ExtCompanyID":string,
      /**  SchemaName  */  
   "SchemaName":string,
      /**  DBTableName  */  
   "DBTableName":string,
      /**  TriggerType  */  
   "TriggerType":string,
      /**  TriggerConditionGroupNum  */  
   "TriggerConditionGroupNum":number,
      /**  TriggerConditionNum  */  
   "TriggerConditionNum":number,
      /**  TriggerConditionDataNum  */  
   "TriggerConditionDataNum":number,
      /**  Data  */  
   "Data":string,
      /**  ExtCompCharacter01  */  
   "ExtCompCharacter01":string,
      /**  ExtCompCharacter02  */  
   "ExtCompCharacter02":string,
      /**  ExtCompBoolean01  */  
   "ExtCompBoolean01":boolean,
      /**  ExtCompBoolean02  */  
   "ExtCompBoolean02":boolean,
      /**  ExtCompDateTime01  */  
   "ExtCompDateTime01":string,
      /**  ExtCompDateTime02  */  
   "ExtCompDateTime02":string,
      /**  ExtCompInteger01  */  
   "ExtCompInteger01":number,
      /**  ExtCompInteger02  */  
   "ExtCompInteger02":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "IsUpdatable":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ExtCompanyTriggerConditionGrpRow{
      /**  Company  */  
   "Company":string,
      /**  ExtSystemID  */  
   "ExtSystemID":string,
      /**  ExtCompanyID  */  
   "ExtCompanyID":string,
      /**  SchemaName  */  
   "SchemaName":string,
      /**  DBTableName  */  
   "DBTableName":string,
      /**  TriggerType  */  
   "TriggerType":string,
      /**  TriggerConditionGroupNum  */  
   "TriggerConditionGroupNum":number,
      /**  TriggerActionNum  */  
   "TriggerActionNum":number,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  ExtCompCharacter01  */  
   "ExtCompCharacter01":string,
      /**  ExtCompCharacter02  */  
   "ExtCompCharacter02":string,
      /**  ExtCompBoolean01  */  
   "ExtCompBoolean01":boolean,
      /**  ExtCompBoolean02  */  
   "ExtCompBoolean02":boolean,
      /**  ExtCompDateTime01  */  
   "ExtCompDateTime01":string,
      /**  ExtCompDateTime02  */  
   "ExtCompDateTime02":string,
      /**  ExtCompInteger01  */  
   "ExtCompInteger01":number,
      /**  ExtCompInteger02  */  
   "ExtCompInteger02":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "IsUpdatable":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ExtCompanyTriggerConditionRow{
      /**  Company  */  
   "Company":string,
      /**  ExtSystemID  */  
   "ExtSystemID":string,
      /**  ExtCompanyID  */  
   "ExtCompanyID":string,
      /**  SchemaName  */  
   "SchemaName":string,
      /**  DBTableName  */  
   "DBTableName":string,
      /**  TriggerType  */  
   "TriggerType":string,
      /**  TriggerConditionGroupNum  */  
   "TriggerConditionGroupNum":number,
      /**  TriggerConditionNum  */  
   "TriggerConditionNum":number,
      /**  OrderSeq  */  
   "OrderSeq":number,
      /**  Operator  */  
   "Operator":string,
      /**  Prefix  */  
   "Prefix":string,
      /**  ConditionTypeName  */  
   "ConditionTypeName":string,
      /**  Postfix  */  
   "Postfix":string,
      /**  ExtCompCharacter01  */  
   "ExtCompCharacter01":string,
      /**  ExtCompCharacter02  */  
   "ExtCompCharacter02":string,
      /**  ExtCompBoolean01  */  
   "ExtCompBoolean01":boolean,
      /**  ExtCompBoolean02  */  
   "ExtCompBoolean02":boolean,
      /**  ExtCompDateTime01  */  
   "ExtCompDateTime01":string,
      /**  ExtCompDateTime02  */  
   "ExtCompDateTime02":string,
      /**  ExtCompInteger01  */  
   "ExtCompInteger01":number,
      /**  ExtCompInteger02  */  
   "ExtCompInteger02":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "IsUpdatable":boolean,
   "Data":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ExtCompanyTriggerDefRow{
      /**  Company  */  
   "Company":string,
      /**  ExtSystemID  */  
   "ExtSystemID":string,
      /**  ExtCompanyID  */  
   "ExtCompanyID":string,
      /**  SchemaName  */  
   "SchemaName":string,
      /**  DBTableName  */  
   "DBTableName":string,
      /**  TriggerType  */  
   "TriggerType":string,
      /**  IsEnabled  */  
   "IsEnabled":boolean,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  ExtCompCharacter01  */  
   "ExtCompCharacter01":string,
      /**  ExtCompCharacter02  */  
   "ExtCompCharacter02":string,
      /**  ExtCompBoolean01  */  
   "ExtCompBoolean01":boolean,
      /**  ExtCompBoolean02  */  
   "ExtCompBoolean02":boolean,
      /**  ExtCompDateTime01  */  
   "ExtCompDateTime01":string,
      /**  ExtCompDateTime02  */  
   "ExtCompDateTime02":string,
      /**  ExtCompInteger01  */  
   "ExtCompInteger01":number,
      /**  ExtCompInteger02  */  
   "ExtCompInteger02":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "DeveloperMode":boolean,
   "IsUpdatable":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ExtPlantRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Code for the external package to be interfaced with  */  
   "ExtSystemID":string,
      /**  Unique identifier of this Site assigned by the user.  */  
   "ExtPlantID":string,
      /**  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  */  
   "TransferMethod":string,
      /**  The ID of the interfaced company  */  
   "ExtCompanyID":string,
      /**  The Site name. Used on shipping reports.  */  
   "Name":string,
      /**  Site address line 1.  */  
   "Address1":string,
      /**  Site address line 2.  */  
   "Address2":string,
      /**  Site address line 3.  */  
   "Address3":string,
      /**  City  */  
   "City":string,
      /**  State/Province  */  
   "State":string,
      /**  Zip/Postal Code  */  
   "Zip":string,
      /**  Country part of the address. This field is in sync with the Country.Country field. Must be a valid entry in the Country table.  */  
   "CountryNum":number,
      /**  Main phone number of the Site.  */  
   "PhoneNum":string,
      /**  Main fax number of the Site.  */  
   "FaxNum":string,
      /**  ExtWarehouse.ExtWarehouseID as the default external warehouse for this external Site.  */  
   "DefaultWhse":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "CountryDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ExtWarehouseRow{
      /**  Company identifier  */  
   "Company":string,
      /**  Code for the external package to be interfaced with  */  
   "ExtSystemID":string,
      /**  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  */  
   "TransferMethod":string,
      /**  The ID of the interfaced company  */  
   "ExtCompanyID":string,
      /**  Unique identifier of this external Site assigned by the user.  */  
   "ExtPlantID":string,
      /**  Unique identifier of this warehouse assigned by the user.  */  
   "ExtWarehouseID":string,
      /**  The Site name. Used on shipping reports.  */  
   "Name":string,
      /**  Site address line 1.  */  
   "Address1":string,
      /**  Site address line 2.  */  
   "Address2":string,
      /**  Site address line 3.  */  
   "Address3":string,
      /**  City  */  
   "City":string,
      /**  State/Province  */  
   "State":string,
      /**  Zip/Postal Code  */  
   "Zip":string,
      /**  Country  */  
   "Country":string,
      /**  Country part of the address. This field is in sync with the Country.Country field. Must be a valid entry in the Country table.  */  
   "CountryNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "CountryDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ds
   */  
export interface ChangedReportID_input{
   ds:Erp_Tablesets_ExtCompanyTableset[],
}

export interface ChangedReportID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ExtCompanyTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangedReportService_input{
   ds:Erp_Tablesets_ExtCompanyTableset[],
}

export interface ChangedReportService_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ExtCompanyTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangedStyleNum_input{
   ds:Erp_Tablesets_ExtCompanyTableset[],
}

export interface ChangedStyleNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ExtCompanyTableset[],
}
}

   /** Required : 
      @param ipCompany
      @param ipExtSystemID
      @param ipTransferMethod
      @param ipExtCompanyID
      @param ipSysRowID
   */  
export interface ConvertToMultiCompanyDirect_input{
      /**  Input the ExtCompany.Company value to be converted  */  
   ipCompany:string,
      /**  Input the ExtCompany.ExtSystemID value to be converted  */  
   ipExtSystemID:string,
      /**  Input the ExtCompany.TransferMethod value to be converted  */  
   ipTransferMethod:string,
      /**  Input the ExtCompany.ExtCompanyID value to be converted  */  
   ipExtCompanyID:string,
      /**  Input the ExtCompany.SysRowID value to be converted  */  
   ipSysRowID:string,
}

export interface ConvertToMultiCompanyDirect_output{
parameters : {
      /**  output parameters  */  
   opSuccess:boolean,
}
}

   /** Required : 
      @param ipCompany
      @param ipExtSystemID
      @param ipTransferMethod
      @param ipExtCompanyID
      @param ipSysRowID
   */  
export interface ConvertToMultiCompanyServiceBus_input{
      /**  Input the ExtCompany.Company value to be converted  */  
   ipCompany:string,
      /**  Input the ExtCompany.ExtSystemID value to be converted  */  
   ipExtSystemID:string,
      /**  Input the ExtCompany.TransferMethod value to be converted  */  
   ipTransferMethod:string,
      /**  Input the ExtCompany.ExtCompanyID value to be converted  */  
   ipExtCompanyID:string,
      /**  Input the ExtCompany.SysRowID value to be converted  */  
   ipSysRowID:string,
}

export interface ConvertToMultiCompanyServiceBus_output{
parameters : {
      /**  output parameters  */  
   opSuccess:boolean,
}
}

   /** Required : 
      @param proposedLocation
      @param proposedTableName
   */  
export interface CreateXSDSchemas_input{
   proposedLocation:string,
   proposedTableName:string,
}

export interface CreateXSDSchemas_output{
parameters : {
      /**  output parameters  */  
   success:boolean,
}
}

export interface CustomerConnect_output{
parameters : {
      /**  output parameters  */  
   disabledList:string,
   checkedList:string,
}
}

   /** Required : 
      @param extSystemID
      @param extCompanyID
   */  
export interface DeleteByID_input{
   extSystemID:string,
   extCompanyID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param defaultDocsEnabled
      @param addedDocType
   */  
export interface ECCAttachmentAccessRisk_input{
      /**  Will collect default storage type and check for client transfer  */  
   defaultDocsEnabled:boolean,
      /**  Checks the File Transfer Mode on the Doc Type  */  
   addedDocType:string,
}

export interface ECCAttachmentAccessRisk_output{
   returnObj:boolean,
}

export interface EntPrsConf_output{
parameters : {
      /**  output parameters  */  
   disabledList:string,
   checkedList:string,
}
}

export interface Erp_Tablesets_ECCDocTypeRow{
      /**  Company  */  
   Company:string,
      /**  The ID of the interfaced company  */  
   ExtCompanyID:string,
      /**  Code for the external package to be interfaced with.  */  
   ExtSystemID:string,
      /**  Unique ID.  */  
   ECCID:number,
      /**  Unique identifier of a DocType.  By selecting this Doc Type all related attachments will be viewable on the web.  */  
   DocTypeID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   DocTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ECCReportDefaultStyleRow{
      /**  Company identifier.  */  
   Company:string,
      /**  The ID of the interfaced company  */  
   ExtCompanyID:string,
      /**  Code for the external package to be interfaced with.  */  
   ExtSystemID:string,
      /**  Unique ID.  */  
   ECCID:number,
      /**  Name of the BL program file used as a broker when auto-printing Crystal Reports or Bartender Labels from a BAM.  */  
   AutoProgram:string,
      /**  Report ID  */  
   ReportID:string,
      /**  Report Style Number.  */  
   StyleNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   StyleList:string,
   RptDescription:string,
   StyleDescription:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_EntityGLCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  */  
   Key2:string,
      /**   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key3:string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key4:string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key5:string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key6:string,
      /**  Identifier of the GL Control Type.  */  
   GLControlType:string,
      /**  GL Control Identifier.  */  
   GLControlCode:string,
      /**  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  */  
   BusinessEntity:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   IsExternalCompany:boolean,
      /**  Marks this EntityGLC as global, available to be sent out to other companies.  */  
   GlobalEntityGLC:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  BankAcctID of the related BankAcct record.  */  
   BankAcctID:string,
   BankFeeID:string,
      /**  CallCode of the related FSCallCd record.  */  
   CallCode:string,
   ChargeCode:string,
      /**  ClassCode of the related FAClass record.  */  
   ClassCode:string,
      /**  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  */  
   ClassID:string,
      /**  ContractCode of the related FSContCd record.  */  
   ContractCode:string,
      /**  CurrencyCode of the related Currency record.  */  
   CurrencyCode:string,
      /**  CustNum of the related Customer record  */  
   CustNum:number,
      /**  DeductionID of PRClsDed or PRDeduct.  */  
   DeductionID:string,
      /**  EmpID of the related PREmpMas record.  */  
   EmpID:string,
      /**  ExpenseCode of PayTLbr, LabExpCd  */  
   ExpenseCode:string,
      /**  ExtSystemID of ExtCompany table  */  
   ExtSystemID:string,
      /**  FromPlant value of the related PlntTranDef record.  */  
   FromPlant:string,
      /**  GroupCode of the related FAGroup record.  */  
   GroupCode:string,
   GroupID:string,
   HeadNum:number,
   InvoiceNum:string,
      /**  JCDept of the related JCDept record.  */  
   JCDept:string,
      /**  MiscCode of the related MiscChrg or PurMisc record.  */  
   MiscCode:string,
      /**  PartNum of the related Part record.  */  
   PartNum:string,
      /**  PayTypeID of PayType  */  
   PayTypeID:string,
   PerConName:string,
      /**  PI Status  */  
   PIStatus:string,
      /**  Plant of the related PlantConfCtrl record.  */  
   Plant:string,
      /**  ProdCode of the related ProdGrup record.  */  
   ProdCode:string,
      /**  ProjectID of the related Project record.  */  
   ProjectID:string,
      /**  PurchCode of the related GLPurch record.  */  
   PurchCode:string,
      /**  RateCode of the related GLRate record.  */  
   RateCode:string,
      /**  ReasonCode of the related Reason record.  */  
   ReasonCode:string,
      /**  ReasonType of the related Reason record.  */  
   ReasonType:string,
      /**  SalesCatID of the related SalesCat record.  */  
   SalesCatID:string,
      /**  Shift value of the related JCShift record.  */  
   Shift:number,
      /**  TaxCode of the related SalesTax record.  */  
   TaxCode:string,
      /**  TaxTblID of PRTaxMas or PRClsTax.  */  
   TaxTblID:string,
      /**  ToPlant value of the related PlntTranDef record.  */  
   ToPlant:string,
      /**  TransferMethod of ExtCompany table  */  
   TransferMethod:string,
      /**  Type ID  */  
   TypeID:string,
      /**  VendorNum of the related Vendor record.  */  
   VendorNum:number,
      /**  WarehouseCode of the related Warehse record.  */  
   WarehouseCode:string,
   ExpenseTypeCode:string,
   IsFiltered:boolean,
   OprTypeCode:string,
   CashDeskID:string,
   TIN:string,
   ReclassCodeID:string,
   BitFlag:number,
   GLCntrlDescription:string,
   GLCntrlTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ExtCompanyAttchRow{
   Company:string,
   ExtSystemID:string,
   ExtCompanyID:string,
   DrawingSeq:number,
   XFileRefNum:number,
   SysRevID:number,
   SysRowID:string,
   ForeignSysRowID:string,
   DrawDesc:string,
   FileName:string,
   PDMDocID:string,
   DocTypeID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ExtCompanyECCRow{
      /**  Company  */  
   Company:string,
      /**  The ID of the interfaced company.  */  
   ExtCompanyID:string,
      /**  Code for the external package to be interfaced with.  */  
   ExtSystemID:string,
      /**  Unique ID.  */  
   ECCID:number,
      /**  URL for ECC uploads  */  
   ECCURL:string,
      /**  ECC Password  */  
   ECCPassword:string,
      /**  User ID  */  
   DefaultEpicorUserID:string,
      /**  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  */  
   DefaultEpicorCustNum:number,
      /**  Miscellaneous charge code for ECC shipping charges  */  
   DefaultMiscChargeCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Miscellaneous charge code for ECC discount  */  
   DefaultDiscountCode:string,
      /**  Link To Task set  */  
   TaskSetID:string,
      /**  Inbound attachments from the web will be related to this Doc Type.  */  
   DocTypeID:string,
      /**  Customer ID prefix that all new customers created by the CNC message will begin with, followed by an incremented number.  */  
   CNCPrefix:string,
      /**  Incremented sequence that will be added to the prefix to create unique Customer IDs for all new customers created from CNC message.  */  
   CNCSeq:number,
      /**  Specifies the length of time, in seconds, that the sync waits for a response from ECC web site.  */  
   TimeOutLimit:number,
      /**  Specifies the number of times the sync will attempt to reprocess a previous failed sync.  */  
   RecycleLimit:number,
      /**  Use Location or use the standard Brand Site.  */  
   UseLocation:boolean,
      /**  ECC Site Name, needs to match what is setup in ECC.  */  
   ECCSiteName:string,
      /**  Link to Work Flow Group  */  
   WFGroupID:string,
      /**  Specifies the cash group prefix for ECC payments. All of the ECC payment cash groups are grouped together using this user-defined prefix.  */  
   BTCashGrpPfx:string,
      /**  Select the default bank to be used for ECC payments from the list of available banks.  */  
   BTDefBankAcctID:string,
      /**  Select this checkbox to indicate Default Documents will be viewable on the web.  Only Default Documents of type File System Document will be supported.  */  
   ViewDefaultDoc:boolean,
      /**  Specifies the A/R invoice group prefix for all ECC payments. All of the ECC payment invoices are grouped together, separate from other shipments using this user-defined prefix.  */  
   InvcGrpPfx:string,
      /**  Select this option to send populated part attributes to ECC  */  
   SendPartAttribute:boolean,
      /**  True when company Allow default document is enabled and the method is File System.  */  
   EnableDefDocsViewable:boolean,
      /**  ECC Masked password field  */  
   ECCPasswordMasked:string,
   BitFlag:number,
   BankAcctIDBankName:string,
   BankAcctIDDescription:string,
   CustomerCustID:string,
   CustomerBTName:string,
   CustomerName:string,
   CustomerInactive:boolean,
   DiscountCodeDescription:string,
   DocTypeDescription:string,
   MiscCodeDescription:string,
   TaskSetWorkflowType:string,
   TaskSetTaskSetDescription:string,
   UserIDName:string,
   WFGroupIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ExtCompanyListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Code for the external package to be interfaced with  */  
   ExtSystemID:string,
      /**  The ID of the interfaced company  */  
   ExtCompanyID:string,
      /**  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  */  
   TransferMethod:string,
      /**  Customers will be sent . CustomerType = "CUS". Init YES  */  
   SendCustomer:boolean,
      /**  Prospects will be sent . CustomerType = "PRO". Init YES  */  
   SendProspect:boolean,
      /**  Suspects  will be sent. CustomerType = "SUS". Init NO  */  
   SendSuspect:boolean,
      /**  Vendors will be sent .  Init YES  */  
   SendVend:boolean,
      /**  Parts will be sent.  Init NO (Future USE)  */  
   SendPart:boolean,
      /**  Shipments will be sent .  Init YES  */  
   SendShip:boolean,
      /**  AR Invoices will be sent .  Init YES  */  
   SendARInv:boolean,
      /**  AR Invoices will be received .  Init YES  */  
   RcvARInv:boolean,
      /**  AP Invoices will be sent .  Init YES  */  
   SendAPInv:boolean,
      /**  AP Invoices will be received .  Init YES  */  
   RcvAPInv:boolean,
      /**  If box is checked, then the AP Invoice system will enable the APInvDtl.PurchCode field for European Financial postings  */  
   APPurchType:boolean,
      /**  For this interface, should acknowledgments be sent back to the interfaced software when a record is received into the intermediate tables?  */  
   SendAckToQue:boolean,
      /**  Indicates if this external company setup supports Inter-Company Trading.  */  
   ICTrading:boolean,
      /**  A  unique integer assigned by the system to identify the Vendor participating in the Inter-Company Trading.  */  
   ICVendorNum:number,
      /**  A  unique integer assigned by the system to identify the Customer participating in the Inter-Company Trading.  */  
   ICCustNum:number,
      /**  A user defined external customer ID.  Identifies the External Customer participating in the Inter-Company Trading.  */  
   ExtCustID:string,
      /**  A user defined external vendor ID.  Identifies the External Vendor participating in the Inter-Company Trading.  */  
   ExtVendorID:string,
      /**  Indicates that the discount amount by line needs to be captured to be sent to the Financials package  */  
   APDiscount:boolean,
      /**  The type of program being called (ProgressProgram or WindowsProgram)  */  
   AuxPrgmType:string,
      /**  Name of Auxiliary program to run to alert external system that there are records ready for processing  */  
   AuxPrgmName:string,
      /**  New PO Suggestions will be sent.  */  
   SendPOSugg:boolean,
      /**  Number of days it will take to transfer an order from one company to the other.  Only for Inter-Company traders.  Will subtract this number from the po need by date to get the correct need by date on the order side.  Controlled on the Order side (po due-date - transfertime = orderdate)  */  
   TransferDays:number,
      /**  Size of blocks for POHeader.PONum to be generated for this Consolidated Purchasing Company.  */  
   PONumBlockSize:number,
      /**  When a Consolidated Purchasing Company requests a new block because their portion of their POHeader.PONum block is less than this Reorder Point, create a new block and send it out.  */  
   PONumBlockReorderPoint:number,
      /**  When a Consolidated Purchasing Company creates a Purchase Order and the number of allocated PONum values drops below this warning point, message the user to inform them.  */  
   PONumBlockWarnPoint:number,
      /**  Establishes the default ExtSite.ExtSiteID to be used as the default for a Site field during creation of a Consolidated Purchase Order Release.  */  
   DefaultPlant:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Send G/L Accounts for Multi-Company Journal.  */  
   SendGLAccounts:boolean,
      /**  Indicates if the current company is allowed to send Multi-Company General Journals to this external company.  */  
   AllowGJAlloc:boolean,
      /**  Indicates if the current company is allowed to send Multi-Company AP G/L entries to this external company.  */  
   AllowAPAlloc:boolean,
      /**  The Journal Group prefix to use when determining the group ID for the Multi-Company Journals coming from this external company.  */  
   JrnGroupPrefix:string,
      /**  Flag to indicate if the Multi-Company Journals coming from this external company needs to be posted automatically.  */  
   AutoPostGJ:boolean,
      /**  The Journal Code to use to enter Multi-Company Journals from this external company.  */  
   JournalCode:string,
      /**  The default Invoice Group Prefix that will be used by Centralized Payment process.  */  
   CPayGroupPrefix:string,
      /**  The flag to indicate if invoices flagged for Centralized Payment from external company will be posted automatically.  */  
   CPayAutoPost:boolean,
      /**   This field will indicate how Legal Number will be generated.  The valid options are:
'O'  -  Use Original Legal Number from the source invoice prefixed with the Source Company ID; 
'N'  -  Generate New Legal Number using the current company's Legal Number rules.  */  
   CPayLegalNum:string,
      /**  When receiving global customers, try to create/link the Part without human intervention  */  
   AutoLoadCust:boolean,
      /**  When receiving global vendors, try to create/link a vendor without human intervention  */  
   AutoLoadVend:boolean,
      /**  When receiving Global Parts, try to create/link a Part without human intervention  */  
   AutoLoadPart:boolean,
      /**  Part revisions will be sent.  Init NO (Future USE)  */  
   SendRev:boolean,
      /**  PerCon will be sent.  */  
   SendPerCon:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   AllowAPPurchType:boolean,
      /**  Flag to indicate when to enable the CPay Group Prefix.  */  
   EnableCPayGroup:boolean,
      /**  Flag to indicate when to enable the CPay Legal Number combo  */  
   EnableCPayLegal:boolean,
      /**  Flag to indicate if the External Company is the Central Payment Parent Company.  */  
   DispCPayParent:boolean,
      /**  Flag to indicate when to enable the AR Intercompany Account button.  */  
   EnableARIntercompany:boolean,
      /**  Full Name of external package  */  
   ExtSystemExtSystemName:string,
      /**  Journal  Description.  */  
   JournalCodeJrnlDescription:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   LinkCustomerBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   LinkCustomerCustID:string,
      /**  The full name of the customer.  */  
   LinkCustomerName:string,
      /**  First address line of the Supplier  */  
   LinkVendorAddress1:string,
      /**  City portion of the address of the Supplier  */  
   LinkVendorCity:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   LinkVendorDefaultFOB:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   LinkVendorTermsCode:string,
      /**  Second address line of the Supplier  */  
   LinkVendorAddress2:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   LinkVendorCountry:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   LinkVendorName:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   LinkVendorVendorID:string,
      /**  Third address line of the Supplier  */  
   LinkVendorAddress3:string,
      /**  A unique code that identifies the currency.  */  
   LinkVendorCurrencyCode:string,
      /**  Can be blank.  */  
   LinkVendorState:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   LinkVendorZIP:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ExtCompanyListTableset{
   ExtCompanyList:Erp_Tablesets_ExtCompanyListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ExtCompanyRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Code for the external package to be interfaced with  */  
   ExtSystemID:string,
      /**  The ID of the interfaced company  */  
   ExtCompanyID:string,
      /**  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  */  
   TransferMethod:string,
      /**  CompanyCountryLangNameID  */  
   CompanyCountryLangNameID:string,
      /**  Customers will be sent . CustomerType = "CUS". Init YES  */  
   SendCustomer:boolean,
      /**  Prospects will be sent . CustomerType = "PRO". Init YES  */  
   SendProspect:boolean,
      /**  Suspects  will be sent. CustomerType = "SUS". Init NO  */  
   SendSuspect:boolean,
      /**  Vendors will be sent .  Init YES  */  
   SendVend:boolean,
      /**  Parts will be sent.  Init NO (Future USE)  */  
   SendPart:boolean,
      /**  Shipments will be sent .  Init YES  */  
   SendShip:boolean,
      /**  AR Invoices will be sent .  Init YES  */  
   SendARInv:boolean,
      /**  AR Invoices will be received .  Init YES  */  
   RcvARInv:boolean,
      /**  AP Invoices will be sent .  Init YES  */  
   SendAPInv:boolean,
      /**  AP Invoices will be received .  Init YES  */  
   RcvAPInv:boolean,
      /**  If box is checked, then the AP Invoice system will enable the APInvDtl.PurchCode field for European Financial postings  */  
   APPurchType:boolean,
      /**  For this interface, should acknowledgments be sent back to the interfaced software when a record is received into the intermediate tables?  */  
   SendAckToQue:boolean,
      /**  Indicates if this external company setup supports Inter-Company Trading.  */  
   ICTrading:boolean,
      /**  A  unique integer assigned by the system to identify the Vendor participating in the Inter-Company Trading.  */  
   ICVendorNum:number,
      /**  A  unique integer assigned by the system to identify the Customer participating in the Inter-Company Trading.  */  
   ICCustNum:number,
      /**  A user defined external customer ID.  Identifies the External Customer participating in the Inter-Company Trading.  */  
   ExtCustID:string,
      /**  A user defined external vendor ID.  Identifies the External Vendor participating in the Inter-Company Trading.  */  
   ExtVendorID:string,
      /**  Indicates that the discount amount by line needs to be captured to be sent to the Financials package  */  
   APDiscount:boolean,
      /**  The type of program being called (ProgressProgram or WindowsProgram)  */  
   AuxPrgmType:string,
      /**  Name of Auxiliary program to run to alert external system that there are records ready for processing  */  
   AuxPrgmName:string,
      /**  New PO Suggestions will be sent.  */  
   SendPOSugg:boolean,
      /**  Last date the connection was made successfully  */  
   LastConDate:string,
      /**  Last Time the connection was made successfully  */  
   LastConTime:number,
      /**  last date the connection was attempted and failed  */  
   LastFailedDate:string,
      /**  Last time the connection was tried and failed  */  
   LastFailedTime:number,
      /**  Number of days it will take to transfer an order from one company to the other.  Only for Inter-Company traders.  Will subtract this number from the po need by date to get the correct need by date on the order side.  Controlled on the Order side (po due-date - transfertime = orderdate)  */  
   TransferDays:number,
      /**  Size of blocks for POHeader.PONum to be generated for this Consolidated Purchasing Company.  */  
   PONumBlockSize:number,
      /**  When a Consolidated Purchasing Company requests a new block because their portion of their POHeader.PONum block is less than this Reorder Point, create a new block and send it out.  */  
   PONumBlockReorderPoint:number,
      /**  When a Consolidated Purchasing Company creates a Purchase Order and the number of allocated PONum values drops below this warning point, message the user to inform them.  */  
   PONumBlockWarnPoint:number,
      /**  Establishes the default ExtSite.ExtSiteID to be used as the default for a Site field during creation of a Consolidated Purchase Order Release.  */  
   DefaultPlant:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Send G/L Accounts for Multi-Company Journal.  */  
   SendGLAccounts:boolean,
      /**  Indicates if the current company is allowed to send Multi-Company General Journals to this external company.  */  
   AllowGJAlloc:boolean,
      /**  Indicates if the current company is allowed to send Multi-Company AP G/L entries to this external company.  */  
   AllowAPAlloc:boolean,
      /**  The Journal Group prefix to use when determining the group ID for the Multi-Company Journals coming from this external company.  */  
   JrnGroupPrefix:string,
      /**  Flag to indicate if the Multi-Company Journals coming from this external company needs to be posted automatically.  */  
   AutoPostGJ:boolean,
      /**  The Journal Code to use to enter Multi-Company Journals from this external company.  */  
   JournalCode:string,
      /**  The default Invoice Group Prefix that will be used by Centralized Payment process.  */  
   CPayGroupPrefix:string,
      /**  The flag to indicate if invoices flagged for Centralized Payment from external company will be posted automatically.  */  
   CPayAutoPost:boolean,
      /**   This field will indicate how Legal Number will be generated.  The valid options are:
'O'  -  Use Original Legal Number from the source invoice prefixed with the Source Company ID; 
'N'  -  Generate New Legal Number using the current company's Legal Number rules.  */  
   CPayLegalNum:string,
      /**  When receiving global customers, try to create/link the Part without human intervention  */  
   AutoLoadCust:boolean,
      /**  When receiving global vendors, try to create/link a vendor without human intervention  */  
   AutoLoadVend:boolean,
      /**  When receiving Global Parts, try to create/link a Part without human intervention  */  
   AutoLoadPart:boolean,
      /**  Part revisions will be sent.  Init NO (Future USE)  */  
   SendRev:boolean,
      /**  PerCon will be sent.  */  
   SendPerCon:boolean,
      /**  MCSegOnly  */  
   MCSegOnly:boolean,
      /**  SendConfigurator  */  
   SendConfigurator:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Turns Global COA on  */  
   SendGlobalCOA:boolean,
      /**  Indicates how much of the COA supporting structure to send. seg`Send Segments Only~coa`Send Full COA  */  
   SendGlobalCOAType:string,
      /**  It is used for rules of creation offsetting GL inter-company lines in multi-company process. If it is checked the journal will have an offsetting line with inter-company account for each multi-company line.  */  
   AlwaysUseGLInterComp:boolean,
      /**  The default Invoice Group Prefix that will be used by Centralized Collection process.  */  
   CColGroupPrefix:string,
      /**  This field will indicate how Legal Number will be generated for Central Collection invoices.  The valid options are: 'O'  -  Use Original Legal Number from the source invoice prefixed with the Source Company ID; 'N'  -  Generate New Legal Number using the current company's Legal Number rules.  */  
   CColCPayLegalNum:string,
      /**  Dynamic Attributes will be sent.  Init NO  */  
   SendDynAttr:boolean,
      /**  Dynamic Attributes will be received.  Init NO  */  
   RcvDynAttr:boolean,
      /**  Flag to indicate if the External Company is the Central Payment Parent Company.  */  
   DispCPayParent:boolean,
      /**  Flag to indicate when to enable the AR Intercompany Account button.  */  
   EnableARIntercompany:boolean,
   EnableConvertToDirect:boolean,
   EnableConvertToSonic:boolean,
      /**  Flag to indicate when to enable the CPay Group Prefix.  */  
   EnableCPayGroup:boolean,
      /**  Flag to indicate when to enable the CPay Legal Number combo  */  
   EnableCPayLegal:boolean,
      /**  Name or description of the external company.  */  
   ExtCompanyName:string,
   ExtSystemIDTransferMethod:string,
   AllowAPPurchType:boolean,
      /**  Flag to indicate when to enable the Central Collection Legal Number  */  
   EnableCColCPayLegalNum:boolean,
      /**  Flag to indicate when to enable the Central Collection Group Prefix.  */  
   EnableCColGroupPrefix:boolean,
   BitFlag:number,
   ExtSystemExtSystemName:string,
   JournalCodeJrnlDescription:string,
   LinkCustomerName:string,
   LinkCustomerBTName:string,
   LinkCustomerCustID:string,
   LinkCustomerInactive:boolean,
   LinkVendorAddress1:string,
   LinkVendorCity:string,
   LinkVendorDefaultFOB:string,
   LinkVendorTermsCode:string,
   LinkVendorAddress2:string,
   LinkVendorCountry:string,
   LinkVendorName:string,
   LinkVendorVendorID:string,
   LinkVendorAddress3:string,
   LinkVendorCurrencyCode:string,
   LinkVendorState:string,
   LinkVendorZIP:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ExtCompanyTableset{
   ExtCompany:Erp_Tablesets_ExtCompanyRow[],
   ExtCompanyAttch:Erp_Tablesets_ExtCompanyAttchRow[],
   ExtCompanyECC:Erp_Tablesets_ExtCompanyECCRow[],
   ECCDocType:Erp_Tablesets_ECCDocTypeRow[],
   ECCReportDefaultStyle:Erp_Tablesets_ECCReportDefaultStyleRow[],
   ExtPlant:Erp_Tablesets_ExtPlantRow[],
   ExtWarehouse:Erp_Tablesets_ExtWarehouseRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   ExtCompanyTriggerDef:Erp_Tablesets_ExtCompanyTriggerDefRow[],
   ExtCompanyTriggerConditionGrp:Erp_Tablesets_ExtCompanyTriggerConditionGrpRow[],
   ExtCompanyTriggerAction:Erp_Tablesets_ExtCompanyTriggerActionRow[],
   ExtCompanyTriggerCondition:Erp_Tablesets_ExtCompanyTriggerConditionRow[],
   ExtCompanyTriggerConditionData:Erp_Tablesets_ExtCompanyTriggerConditionDataRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ExtCompanyTriggerActionRow{
      /**  Company  */  
   Company:string,
      /**  ExtSystemID  */  
   ExtSystemID:string,
      /**  ExtCompanyID  */  
   ExtCompanyID:string,
      /**  SchemaName  */  
   SchemaName:string,
      /**  DBTableName  */  
   DBTableName:string,
      /**  TriggerType  */  
   TriggerType:string,
      /**  TriggerActionNum  */  
   TriggerActionNum:number,
      /**  ActionType  */  
   ActionType:string,
      /**  WorkflowName  */  
   WorkflowName:string,
      /**  ActionIsAsynchronous  */  
   ActionIsAsynchronous:boolean,
      /**  ExtCompCharacter01  */  
   ExtCompCharacter01:string,
      /**  ExtCompCharacter02  */  
   ExtCompCharacter02:string,
      /**  ExtCompBoolean01  */  
   ExtCompBoolean01:boolean,
      /**  ExtCompBoolean02  */  
   ExtCompBoolean02:boolean,
      /**  ExtCompDateTime01  */  
   ExtCompDateTime01:string,
      /**  ExtCompDateTime02  */  
   ExtCompDateTime02:string,
      /**  ExtCompInteger01  */  
   ExtCompInteger01:number,
      /**  ExtCompInteger02  */  
   ExtCompInteger02:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   IsUpdatable:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ExtCompanyTriggerConditionDataRow{
      /**  Company  */  
   Company:string,
      /**  ExtSystemID  */  
   ExtSystemID:string,
      /**  ExtCompanyID  */  
   ExtCompanyID:string,
      /**  SchemaName  */  
   SchemaName:string,
      /**  DBTableName  */  
   DBTableName:string,
      /**  TriggerType  */  
   TriggerType:string,
      /**  TriggerConditionGroupNum  */  
   TriggerConditionGroupNum:number,
      /**  TriggerConditionNum  */  
   TriggerConditionNum:number,
      /**  TriggerConditionDataNum  */  
   TriggerConditionDataNum:number,
      /**  Data  */  
   Data:string,
      /**  ExtCompCharacter01  */  
   ExtCompCharacter01:string,
      /**  ExtCompCharacter02  */  
   ExtCompCharacter02:string,
      /**  ExtCompBoolean01  */  
   ExtCompBoolean01:boolean,
      /**  ExtCompBoolean02  */  
   ExtCompBoolean02:boolean,
      /**  ExtCompDateTime01  */  
   ExtCompDateTime01:string,
      /**  ExtCompDateTime02  */  
   ExtCompDateTime02:string,
      /**  ExtCompInteger01  */  
   ExtCompInteger01:number,
      /**  ExtCompInteger02  */  
   ExtCompInteger02:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   IsUpdatable:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ExtCompanyTriggerConditionGrpRow{
      /**  Company  */  
   Company:string,
      /**  ExtSystemID  */  
   ExtSystemID:string,
      /**  ExtCompanyID  */  
   ExtCompanyID:string,
      /**  SchemaName  */  
   SchemaName:string,
      /**  DBTableName  */  
   DBTableName:string,
      /**  TriggerType  */  
   TriggerType:string,
      /**  TriggerConditionGroupNum  */  
   TriggerConditionGroupNum:number,
      /**  TriggerActionNum  */  
   TriggerActionNum:number,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  ExtCompCharacter01  */  
   ExtCompCharacter01:string,
      /**  ExtCompCharacter02  */  
   ExtCompCharacter02:string,
      /**  ExtCompBoolean01  */  
   ExtCompBoolean01:boolean,
      /**  ExtCompBoolean02  */  
   ExtCompBoolean02:boolean,
      /**  ExtCompDateTime01  */  
   ExtCompDateTime01:string,
      /**  ExtCompDateTime02  */  
   ExtCompDateTime02:string,
      /**  ExtCompInteger01  */  
   ExtCompInteger01:number,
      /**  ExtCompInteger02  */  
   ExtCompInteger02:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   IsUpdatable:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ExtCompanyTriggerConditionRow{
      /**  Company  */  
   Company:string,
      /**  ExtSystemID  */  
   ExtSystemID:string,
      /**  ExtCompanyID  */  
   ExtCompanyID:string,
      /**  SchemaName  */  
   SchemaName:string,
      /**  DBTableName  */  
   DBTableName:string,
      /**  TriggerType  */  
   TriggerType:string,
      /**  TriggerConditionGroupNum  */  
   TriggerConditionGroupNum:number,
      /**  TriggerConditionNum  */  
   TriggerConditionNum:number,
      /**  OrderSeq  */  
   OrderSeq:number,
      /**  Operator  */  
   Operator:string,
      /**  Prefix  */  
   Prefix:string,
      /**  ConditionTypeName  */  
   ConditionTypeName:string,
      /**  Postfix  */  
   Postfix:string,
      /**  ExtCompCharacter01  */  
   ExtCompCharacter01:string,
      /**  ExtCompCharacter02  */  
   ExtCompCharacter02:string,
      /**  ExtCompBoolean01  */  
   ExtCompBoolean01:boolean,
      /**  ExtCompBoolean02  */  
   ExtCompBoolean02:boolean,
      /**  ExtCompDateTime01  */  
   ExtCompDateTime01:string,
      /**  ExtCompDateTime02  */  
   ExtCompDateTime02:string,
      /**  ExtCompInteger01  */  
   ExtCompInteger01:number,
      /**  ExtCompInteger02  */  
   ExtCompInteger02:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   IsUpdatable:boolean,
   Data:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ExtCompanyTriggerDefRow{
      /**  Company  */  
   Company:string,
      /**  ExtSystemID  */  
   ExtSystemID:string,
      /**  ExtCompanyID  */  
   ExtCompanyID:string,
      /**  SchemaName  */  
   SchemaName:string,
      /**  DBTableName  */  
   DBTableName:string,
      /**  TriggerType  */  
   TriggerType:string,
      /**  IsEnabled  */  
   IsEnabled:boolean,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  ExtCompCharacter01  */  
   ExtCompCharacter01:string,
      /**  ExtCompCharacter02  */  
   ExtCompCharacter02:string,
      /**  ExtCompBoolean01  */  
   ExtCompBoolean01:boolean,
      /**  ExtCompBoolean02  */  
   ExtCompBoolean02:boolean,
      /**  ExtCompDateTime01  */  
   ExtCompDateTime01:string,
      /**  ExtCompDateTime02  */  
   ExtCompDateTime02:string,
      /**  ExtCompInteger01  */  
   ExtCompInteger01:number,
      /**  ExtCompInteger02  */  
   ExtCompInteger02:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   DeveloperMode:boolean,
   IsUpdatable:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ExtPlantRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Code for the external package to be interfaced with  */  
   ExtSystemID:string,
      /**  Unique identifier of this Site assigned by the user.  */  
   ExtPlantID:string,
      /**  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  */  
   TransferMethod:string,
      /**  The ID of the interfaced company  */  
   ExtCompanyID:string,
      /**  The Site name. Used on shipping reports.  */  
   Name:string,
      /**  Site address line 1.  */  
   Address1:string,
      /**  Site address line 2.  */  
   Address2:string,
      /**  Site address line 3.  */  
   Address3:string,
      /**  City  */  
   City:string,
      /**  State/Province  */  
   State:string,
      /**  Zip/Postal Code  */  
   Zip:string,
      /**  Country part of the address. This field is in sync with the Country.Country field. Must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  Main phone number of the Site.  */  
   PhoneNum:string,
      /**  Main fax number of the Site.  */  
   FaxNum:string,
      /**  ExtWarehouse.ExtWarehouseID as the default external warehouse for this external Site.  */  
   DefaultWhse:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   CountryDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ExtWarehouseRow{
      /**  Company identifier  */  
   Company:string,
      /**  Code for the external package to be interfaced with  */  
   ExtSystemID:string,
      /**  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  */  
   TransferMethod:string,
      /**  The ID of the interfaced company  */  
   ExtCompanyID:string,
      /**  Unique identifier of this external Site assigned by the user.  */  
   ExtPlantID:string,
      /**  Unique identifier of this warehouse assigned by the user.  */  
   ExtWarehouseID:string,
      /**  The Site name. Used on shipping reports.  */  
   Name:string,
      /**  Site address line 1.  */  
   Address1:string,
      /**  Site address line 2.  */  
   Address2:string,
      /**  Site address line 3.  */  
   Address3:string,
      /**  City  */  
   City:string,
      /**  State/Province  */  
   State:string,
      /**  Zip/Postal Code  */  
   Zip:string,
      /**  Country  */  
   Country:string,
      /**  Country part of the address. This field is in sync with the Country.Country field. Must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   CountryDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtExtCompanyTableset{
   ExtCompany:Erp_Tablesets_ExtCompanyRow[],
   ExtCompanyAttch:Erp_Tablesets_ExtCompanyAttchRow[],
   ExtCompanyECC:Erp_Tablesets_ExtCompanyECCRow[],
   ECCDocType:Erp_Tablesets_ECCDocTypeRow[],
   ECCReportDefaultStyle:Erp_Tablesets_ECCReportDefaultStyleRow[],
   ExtPlant:Erp_Tablesets_ExtPlantRow[],
   ExtWarehouse:Erp_Tablesets_ExtWarehouseRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   ExtCompanyTriggerDef:Erp_Tablesets_ExtCompanyTriggerDefRow[],
   ExtCompanyTriggerConditionGrp:Erp_Tablesets_ExtCompanyTriggerConditionGrpRow[],
   ExtCompanyTriggerAction:Erp_Tablesets_ExtCompanyTriggerActionRow[],
   ExtCompanyTriggerCondition:Erp_Tablesets_ExtCompanyTriggerConditionRow[],
   ExtCompanyTriggerConditionData:Erp_Tablesets_ExtCompanyTriggerConditionDataRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface FSA_output{
parameters : {
      /**  output parameters  */  
   disabledList:string,
   checkedList:string,
}
}

export interface Generic_output{
parameters : {
      /**  output parameters  */  
   disabledList:string,
   checkedList:string,
}
}

   /** Required : 
      @param extSystemID
      @param extCompanyID
   */  
export interface GetByID_input{
   extSystemID:string,
   extCompanyID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ExtCompanyTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ExtCompanyTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ExtCompanyTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
   tableName:string,
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

export interface GetECCReportServiceDescList_output{
   returnObj:string,
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_ExtCompanyListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param extCompanyID
      @param extSystemID
      @param ecCID
   */  
export interface GetNewECCDocType_input{
   ds:Erp_Tablesets_ExtCompanyTableset[],
   extCompanyID:string,
   extSystemID:string,
   ecCID:number,
}

export interface GetNewECCDocType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ExtCompanyTableset[],
}
}

   /** Required : 
      @param ds
      @param extCompanyID
      @param extSystemID
      @param ecCID
   */  
export interface GetNewECCReportDefaultStyle_input{
   ds:Erp_Tablesets_ExtCompanyTableset[],
   extCompanyID:string,
   extSystemID:string,
   ecCID:number,
}

export interface GetNewECCReportDefaultStyle_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ExtCompanyTableset[],
}
}

   /** Required : 
      @param ds
      @param relatedToFile
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param key6
   */  
export interface GetNewEntityGLC_input{
   ds:Erp_Tablesets_ExtCompanyTableset[],
   relatedToFile:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   key6:string,
}

export interface GetNewEntityGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ExtCompanyTableset[],
}
}

   /** Required : 
      @param ds
      @param extSystemID
      @param extCompanyID
   */  
export interface GetNewExtCompanyAttch_input{
   ds:Erp_Tablesets_ExtCompanyTableset[],
   extSystemID:string,
   extCompanyID:string,
}

export interface GetNewExtCompanyAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ExtCompanyTableset[],
}
}

   /** Required : 
      @param ds
      @param extCompanyID
      @param extSystemID
   */  
export interface GetNewExtCompanyECC_input{
   ds:Erp_Tablesets_ExtCompanyTableset[],
   extCompanyID:string,
   extSystemID:string,
}

export interface GetNewExtCompanyECC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ExtCompanyTableset[],
}
}

   /** Required : 
      @param ds
      @param extSystemID
      @param extCompanyID
      @param schemaName
      @param dbTableName
      @param triggerType
   */  
export interface GetNewExtCompanyTriggerAction_input{
   ds:Erp_Tablesets_ExtCompanyTableset[],
   extSystemID:string,
   extCompanyID:string,
   schemaName:string,
   dbTableName:string,
   triggerType:string,
}

export interface GetNewExtCompanyTriggerAction_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ExtCompanyTableset[],
}
}

   /** Required : 
      @param ds
      @param extSystemID
      @param extCompanyID
      @param schemaName
      @param dbTableName
      @param triggerType
      @param triggerConditionGroupNum
      @param triggerConditionNum
   */  
export interface GetNewExtCompanyTriggerConditionData_input{
   ds:Erp_Tablesets_ExtCompanyTableset[],
   extSystemID:string,
   extCompanyID:string,
   schemaName:string,
   dbTableName:string,
   triggerType:string,
   triggerConditionGroupNum:number,
   triggerConditionNum:number,
}

export interface GetNewExtCompanyTriggerConditionData_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ExtCompanyTableset[],
}
}

   /** Required : 
      @param ds
      @param extSystemID
      @param extCompanyID
      @param schemaName
      @param dbTableName
      @param triggerType
      @param triggerConditionGroupNum
   */  
export interface GetNewExtCompanyTriggerConditionGrp_input{
   ds:Erp_Tablesets_ExtCompanyTableset[],
   extSystemID:string,
   extCompanyID:string,
   schemaName:string,
   dbTableName:string,
   triggerType:string,
   triggerConditionGroupNum:number,
}

export interface GetNewExtCompanyTriggerConditionGrp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ExtCompanyTableset[],
}
}

   /** Required : 
      @param ds
      @param extSystemID
      @param extCompanyID
      @param schemaName
      @param dbTableName
      @param triggerType
      @param triggerConditionGroupNum
   */  
export interface GetNewExtCompanyTriggerCondition_input{
   ds:Erp_Tablesets_ExtCompanyTableset[],
   extSystemID:string,
   extCompanyID:string,
   schemaName:string,
   dbTableName:string,
   triggerType:string,
   triggerConditionGroupNum:number,
}

export interface GetNewExtCompanyTriggerCondition_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ExtCompanyTableset[],
}
}

   /** Required : 
      @param ds
      @param extSystemID
      @param extCompanyID
      @param schemaName
      @param dbTableName
   */  
export interface GetNewExtCompanyTriggerDef_input{
   ds:Erp_Tablesets_ExtCompanyTableset[],
   extSystemID:string,
   extCompanyID:string,
   schemaName:string,
   dbTableName:string,
}

export interface GetNewExtCompanyTriggerDef_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ExtCompanyTableset[],
}
}

   /** Required : 
      @param ds
      @param extSystemID
   */  
export interface GetNewExtCompany_input{
   ds:Erp_Tablesets_ExtCompanyTableset[],
   extSystemID:string,
}

export interface GetNewExtCompany_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ExtCompanyTableset[],
}
}

   /** Required : 
      @param ds
      @param extSystemID
      @param transferMethod
      @param extCompanyID
   */  
export interface GetNewExtPlant_input{
   ds:Erp_Tablesets_ExtCompanyTableset[],
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface GetNewExtPlant_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ExtCompanyTableset[],
}
}

   /** Required : 
      @param ds
      @param extSystemID
      @param transferMethod
      @param extCompanyID
      @param extPlantID
   */  
export interface GetNewExtWarehouse_input{
   ds:Erp_Tablesets_ExtCompanyTableset[],
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
   extPlantID:string,
}

export interface GetNewExtWarehouse_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ExtCompanyTableset[],
}
}

   /** Required : 
      @param whereClauseExtCompany
      @param whereClauseExtCompanyAttch
      @param whereClauseExtCompanyECC
      @param whereClauseECCDocType
      @param whereClauseECCReportDefaultStyle
      @param whereClauseExtPlant
      @param whereClauseExtWarehouse
      @param whereClauseEntityGLC
      @param whereClauseExtCompanyTriggerDef
      @param whereClauseExtCompanyTriggerConditionGrp
      @param whereClauseExtCompanyTriggerAction
      @param whereClauseExtCompanyTriggerCondition
      @param whereClauseExtCompanyTriggerConditionData
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseExtCompany:string,
   whereClauseExtCompanyAttch:string,
   whereClauseExtCompanyECC:string,
   whereClauseECCDocType:string,
   whereClauseECCReportDefaultStyle:string,
   whereClauseExtPlant:string,
   whereClauseExtWarehouse:string,
   whereClauseEntityGLC:string,
   whereClauseExtCompanyTriggerDef:string,
   whereClauseExtCompanyTriggerConditionGrp:string,
   whereClauseExtCompanyTriggerAction:string,
   whereClauseExtCompanyTriggerCondition:string,
   whereClauseExtCompanyTriggerConditionData:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ExtCompanyTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface Ice_BOUpdErrorRow{
   TableName:string,
   ErrorLevel:string,
   ErrorType:string,
   ErrorText:string,
   ErrorSysRowID:string,
   SysRowID:string,
   RowMod:string,
}

export interface Ice_BOUpdErrorTableset{
   BOUpdError:Ice_BOUpdErrorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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

   /** Required : 
      @param extCompanyID
      @param extTransferMethod
   */  
export interface InitCOA_input{
      /**  The External Company ID  */  
   extCompanyID:string,
      /**  The external Company transfer method  */  
   extTransferMethod:string,
}

export interface InitCOA_output{
parameters : {
      /**  output parameters  */  
   errlog:string,
}
}

   /** Required : 
      @param extCompanyID
      @param extTransferMethod
      @param fromDate
   */  
export interface InitConsolidationMonitor_input{
      /**  The External Company ID  */  
   extCompanyID:string,
      /**  The external Company transfer method  */  
   extTransferMethod:string,
      /**  Filter to skip old consolidations  */  
   fromDate:string,
}

export interface InitConsolidationMonitor_output{
parameters : {
      /**  output parameters  */  
   errlog:string,
}
}

   /** Required : 
      @param extCompanyID
   */  
export interface InitEntprsConf_input{
      /**  The External Company ID  */  
   extCompanyID:string,
}

export interface InitEntprsConf_output{
parameters : {
      /**  output parameters  */  
   errlog:string,
}
}

   /** Required : 
      @param extCompanyID
      @param extTransferMethod
   */  
export interface InitMultiCompany_input{
      /**  The External Company ID  */  
   extCompanyID:string,
      /**  The external Company transfer method  */  
   extTransferMethod:string,
}

export interface InitMultiCompany_output{
parameters : {
      /**  output parameters  */  
   errlog:string,
}
}

export interface Mobile_output{
parameters : {
      /**  output parameters  */  
   disabledList:string,
   checkedList:string,
}
}

export interface MultiCompany_output{
parameters : {
      /**  output parameters  */  
   disabledList:string,
   checkedList:string,
}
}

   /** Required : 
      @param eccSiteName
   */  
export interface OnChangeECCSiteName_input{
   eccSiteName:string,
}

export interface OnChangeECCSiteName_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   warningMsg:string,
}
}

   /** Required : 
      @param proposedLocation
      @param proposedTableName
   */  
export interface OnChangeLocation_input{
   proposedLocation:string,
   proposedTableName:string,
}

export interface OnChangeLocation_output{
parameters : {
      /**  output parameters  */  
   inSchema:string,
   outSchema:string,
}
}

   /** Required : 
      @param proposedTableName
      @param ds
   */  
export interface OnChangeTriggerDefTableName_input{
   proposedTableName:string,
   ds:Erp_Tablesets_ExtCompanyTableset[],
}

export interface OnChangeTriggerDefTableName_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ExtCompanyTableset[],
}
}

export interface PLM_output{
parameters : {
      /**  output parameters  */  
   disabledList:string,
   checkedList:string,
}
}

export interface SupplierConnect_output{
parameters : {
      /**  output parameters  */  
   disabledList:string,
   checkedList:string,
}
}

   /** Required : 
      @param extCompRowid
   */  
export interface TestConnection_input{
      /**  The RowIdent of the record of which to test connection  */  
   extCompRowid:string,
}

export interface TestConnection_output{
}

   /** Required : 
      @param extCompRowid
   */  
export interface TestECCConnection_input{
   extCompRowid:string,
}

export interface TestECCConnection_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   msgConnection:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtExtCompanyTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtExtCompanyTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ExtCompanyTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ExtCompanyTableset[],
}
}

   /** Required : 
      @param extCompanyID
      @param extsystemID
      @param eccID
      @param autoProgram
   */  
export interface ValidateReportService_input{
      /**  extCompanyID  */  
   extCompanyID:string,
      /**  extsystemID  */  
   extsystemID:string,
      /**  eccID  */  
   eccID:number,
      /**  Report Service  */  
   autoProgram:string,
}

export interface ValidateReportService_output{
   returnObj:boolean,
}

   /** Required : 
      @param proposedLocation
      @param specialFolder
      @param proposedTableName
   */  
export interface WriteXSDSchemasToServer_input{
      /**  relative path on the server  */  
   proposedLocation:string,
      /**  the type of the folder location (Report, UserData, Company Data and so on)  */  
   specialFolder:number,
      /**  The name of the table  */  
   proposedTableName:string,
}

export interface WriteXSDSchemasToServer_output{
parameters : {
      /**  output parameters  */  
   inSchemaFileName:string,
   outSchemaFileName:string,
}
}

