import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.InspResultsSvc
// Description: The InspResults business object is used as a front end to call the configuration
entry process for inspection processing and test plans.
            
bo/InspResults/InspResults.p
Brock Mulqueen
08/03/09
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/$metadata", {
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
   Description: Get InspResults items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspResults
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsRow
   */  
export function get_InspResults(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResults", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InspResults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InspResultsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InspResultsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InspResults(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResults", {
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
   Summary: Calls GetByID to retrieve the InspResult item
   Description: Calls GetByID to retrieve the InspResult item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResult
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsRow
   */  
export function get_InspResults_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InspResultsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResults(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InspResultsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update InspResult for the service
   Description: Calls UpdateExt to update InspResult. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InspResult
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InspResultsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_InspResults_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResults(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")", {
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
   Summary: Call UpdateExt to delete InspResult item
   Description: Call UpdateExt to delete InspResult item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InspResult
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_InspResults_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResults(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")", {
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
   Description: Get InspResultsAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_InspResultsAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsAttchRow
   */  
export function get_InspResults_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_InspResultsAttches(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResults(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")/InspResultsAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the InspResultsAttch item
   Description: Calls GetByID to retrieve the InspResultsAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsAttchRow
   */  
export function get_InspResults_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_InspResultsAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InspResultsAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResults(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")/InspResultsAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InspResultsAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get InspResultsAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspResultsAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsAttchRow
   */  
export function get_InspResultsAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InspResultsAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InspResultsAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InspResultsAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InspResultsAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsAttches", {
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
   Summary: Calls GetByID to retrieve the InspResultsAttch item
   Description: Calls GetByID to retrieve the InspResultsAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsAttchRow
   */  
export function get_InspResultsAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InspResultsAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InspResultsAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update InspResultsAttch for the service
   Description: Calls UpdateExt to update InspResultsAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InspResultsAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InspResultsAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_InspResultsAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete InspResultsAttch item
   Description: Call UpdateExt to delete InspResultsAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InspResultsAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_InspResultsAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", {
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
   Description: Get InspResultsChars items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspResultsChars
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsCharRow
   */  
export function get_InspResultsChars(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsCharRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsChars", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsCharRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InspResultsChars
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InspResultsCharRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InspResultsCharRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InspResultsChars(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsChars", {
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
   Summary: Calls GetByID to retrieve the InspResultsChar item
   Description: Calls GetByID to retrieve the InspResultsChar item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsChar
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsCharRow
   */  
export function get_InspResultsChars_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InspResultsCharRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsChars(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InspResultsCharRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update InspResultsChar for the service
   Description: Calls UpdateExt to update InspResultsChar. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InspResultsChar
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InspResultsCharRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_InspResultsChars_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsChars(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")", {
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
   Summary: Call UpdateExt to delete InspResultsChar item
   Description: Call UpdateExt to delete InspResultsChar item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InspResultsChar
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_InspResultsChars_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsChars(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")", {
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
   Description: Get InspResultsCharAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_InspResultsCharAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsCharAttchRow
   */  
export function get_InspResultsChars_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_InspResultsCharAttches(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsCharAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsChars(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")/InspResultsCharAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsCharAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the InspResultsCharAttch item
   Description: Calls GetByID to retrieve the InspResultsCharAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsCharAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsCharAttchRow
   */  
export function get_InspResultsChars_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_InspResultsCharAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InspResultsCharAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsChars(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")/InspResultsCharAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InspResultsCharAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get InspResultsCharAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspResultsCharAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsCharAttchRow
   */  
export function get_InspResultsCharAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsCharAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsCharAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsCharAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InspResultsCharAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InspResultsCharAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InspResultsCharAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InspResultsCharAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsCharAttches", {
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
   Summary: Calls GetByID to retrieve the InspResultsCharAttch item
   Description: Calls GetByID to retrieve the InspResultsCharAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsCharAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsCharAttchRow
   */  
export function get_InspResultsCharAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InspResultsCharAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsCharAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InspResultsCharAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update InspResultsCharAttch for the service
   Description: Calls UpdateExt to update InspResultsCharAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InspResultsCharAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InspResultsCharAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_InspResultsCharAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsCharAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete InspResultsCharAttch item
   Description: Call UpdateExt to delete InspResultsCharAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InspResultsCharAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_InspResultsCharAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsCharAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", {
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
   Description: Get InspResultsCheckBoxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspResultsCheckBoxes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsCheckBoxRow
   */  
export function get_InspResultsCheckBoxes(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsCheckBoxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsCheckBoxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsCheckBoxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InspResultsCheckBoxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InspResultsCheckBoxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InspResultsCheckBoxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InspResultsCheckBoxes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsCheckBoxes", {
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
   Summary: Calls GetByID to retrieve the InspResultsCheckBox item
   Description: Calls GetByID to retrieve the InspResultsCheckBox item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsCheckBox
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsCheckBoxRow
   */  
export function get_InspResultsCheckBoxes_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InspResultsCheckBoxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsCheckBoxes(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InspResultsCheckBoxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update InspResultsCheckBox for the service
   Description: Calls UpdateExt to update InspResultsCheckBox. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InspResultsCheckBox
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InspResultsCheckBoxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_InspResultsCheckBoxes_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsCheckBoxes(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")", {
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
   Summary: Call UpdateExt to delete InspResultsCheckBox item
   Description: Call UpdateExt to delete InspResultsCheckBox item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InspResultsCheckBox
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_InspResultsCheckBoxes_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsCheckBoxes(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")", {
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
   Description: Get InspResultsCheckBoxAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_InspResultsCheckBoxAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsCheckBoxAttchRow
   */  
export function get_InspResultsCheckBoxes_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_InspResultsCheckBoxAttches(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsCheckBoxAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsCheckBoxes(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")/InspResultsCheckBoxAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsCheckBoxAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the InspResultsCheckBoxAttch item
   Description: Calls GetByID to retrieve the InspResultsCheckBoxAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsCheckBoxAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsCheckBoxAttchRow
   */  
export function get_InspResultsCheckBoxes_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_InspResultsCheckBoxAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InspResultsCheckBoxAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsCheckBoxes(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")/InspResultsCheckBoxAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InspResultsCheckBoxAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get InspResultsCheckBoxAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspResultsCheckBoxAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsCheckBoxAttchRow
   */  
export function get_InspResultsCheckBoxAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsCheckBoxAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsCheckBoxAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsCheckBoxAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InspResultsCheckBoxAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InspResultsCheckBoxAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InspResultsCheckBoxAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InspResultsCheckBoxAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsCheckBoxAttches", {
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
   Summary: Calls GetByID to retrieve the InspResultsCheckBoxAttch item
   Description: Calls GetByID to retrieve the InspResultsCheckBoxAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsCheckBoxAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsCheckBoxAttchRow
   */  
export function get_InspResultsCheckBoxAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InspResultsCheckBoxAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsCheckBoxAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InspResultsCheckBoxAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update InspResultsCheckBoxAttch for the service
   Description: Calls UpdateExt to update InspResultsCheckBoxAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InspResultsCheckBoxAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InspResultsCheckBoxAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_InspResultsCheckBoxAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsCheckBoxAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete InspResultsCheckBoxAttch item
   Description: Call UpdateExt to delete InspResultsCheckBoxAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InspResultsCheckBoxAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_InspResultsCheckBoxAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsCheckBoxAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", {
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
   Description: Get InspResultsDates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspResultsDates
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsDateRow
   */  
export function get_InspResultsDates(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsDateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsDates", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsDateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InspResultsDates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InspResultsDateRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InspResultsDateRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InspResultsDates(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsDates", {
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
   Summary: Calls GetByID to retrieve the InspResultsDate item
   Description: Calls GetByID to retrieve the InspResultsDate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsDate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsDateRow
   */  
export function get_InspResultsDates_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InspResultsDateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsDates(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InspResultsDateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update InspResultsDate for the service
   Description: Calls UpdateExt to update InspResultsDate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InspResultsDate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InspResultsDateRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_InspResultsDates_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsDates(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")", {
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
   Summary: Call UpdateExt to delete InspResultsDate item
   Description: Call UpdateExt to delete InspResultsDate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InspResultsDate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_InspResultsDates_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsDates(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")", {
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
   Description: Get InspResultsDateAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_InspResultsDateAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsDateAttchRow
   */  
export function get_InspResultsDates_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_InspResultsDateAttches(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsDateAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsDates(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")/InspResultsDateAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsDateAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the InspResultsDateAttch item
   Description: Calls GetByID to retrieve the InspResultsDateAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsDateAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsDateAttchRow
   */  
export function get_InspResultsDates_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_InspResultsDateAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InspResultsDateAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsDates(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")/InspResultsDateAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InspResultsDateAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get InspResultsDateAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspResultsDateAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsDateAttchRow
   */  
export function get_InspResultsDateAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsDateAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsDateAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsDateAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InspResultsDateAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InspResultsDateAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InspResultsDateAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InspResultsDateAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsDateAttches", {
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
   Summary: Calls GetByID to retrieve the InspResultsDateAttch item
   Description: Calls GetByID to retrieve the InspResultsDateAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsDateAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsDateAttchRow
   */  
export function get_InspResultsDateAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InspResultsDateAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsDateAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InspResultsDateAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update InspResultsDateAttch for the service
   Description: Calls UpdateExt to update InspResultsDateAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InspResultsDateAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InspResultsDateAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_InspResultsDateAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsDateAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete InspResultsDateAttch item
   Description: Call UpdateExt to delete InspResultsDateAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InspResultsDateAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_InspResultsDateAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsDateAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", {
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
   Description: Get InspResultsNums items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspResultsNums
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsNumRow
   */  
export function get_InspResultsNums(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsNumRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsNums", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsNumRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InspResultsNums
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InspResultsNumRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InspResultsNumRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InspResultsNums(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsNums", {
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
   Summary: Calls GetByID to retrieve the InspResultsNum item
   Description: Calls GetByID to retrieve the InspResultsNum item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsNum
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsNumRow
   */  
export function get_InspResultsNums_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InspResultsNumRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsNums(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InspResultsNumRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update InspResultsNum for the service
   Description: Calls UpdateExt to update InspResultsNum. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InspResultsNum
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InspResultsNumRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_InspResultsNums_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsNums(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")", {
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
   Summary: Call UpdateExt to delete InspResultsNum item
   Description: Call UpdateExt to delete InspResultsNum item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InspResultsNum
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_InspResultsNums_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsNums(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")", {
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
   Description: Get InspResultsNumAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_InspResultsNumAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsNumAttchRow
   */  
export function get_InspResultsNums_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_InspResultsNumAttches(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsNumAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsNums(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")/InspResultsNumAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsNumAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the InspResultsNumAttch item
   Description: Calls GetByID to retrieve the InspResultsNumAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsNumAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsNumAttchRow
   */  
export function get_InspResultsNums_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_InspResultsNumAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InspResultsNumAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsNums(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")/InspResultsNumAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InspResultsNumAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get InspResultsNumAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspResultsNumAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsNumAttchRow
   */  
export function get_InspResultsNumAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsNumAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsNumAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsNumAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InspResultsNumAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InspResultsNumAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InspResultsNumAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InspResultsNumAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsNumAttches", {
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
   Summary: Calls GetByID to retrieve the InspResultsNumAttch item
   Description: Calls GetByID to retrieve the InspResultsNumAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsNumAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsNumAttchRow
   */  
export function get_InspResultsNumAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InspResultsNumAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsNumAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InspResultsNumAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update InspResultsNumAttch for the service
   Description: Calls UpdateExt to update InspResultsNumAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InspResultsNumAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InspResultsNumAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_InspResultsNumAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsNumAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete InspResultsNumAttch item
   Description: Call UpdateExt to delete InspResultsNumAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InspResultsNumAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_InspResultsNumAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsNumAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", {
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
   Description: Get InspResultsShortChars items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspResultsShortChars
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsShortCharRow
   */  
export function get_InspResultsShortChars(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsShortCharRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsShortChars", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsShortCharRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InspResultsShortChars
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InspResultsShortCharRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InspResultsShortCharRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InspResultsShortChars(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsShortChars", {
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
   Summary: Calls GetByID to retrieve the InspResultsShortChar item
   Description: Calls GetByID to retrieve the InspResultsShortChar item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsShortChar
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsShortCharRow
   */  
export function get_InspResultsShortChars_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InspResultsShortCharRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsShortChars(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InspResultsShortCharRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update InspResultsShortChar for the service
   Description: Calls UpdateExt to update InspResultsShortChar. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InspResultsShortChar
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InspResultsShortCharRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_InspResultsShortChars_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsShortChars(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")", {
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
   Summary: Call UpdateExt to delete InspResultsShortChar item
   Description: Call UpdateExt to delete InspResultsShortChar item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InspResultsShortChar
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_InspResultsShortChars_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsShortChars(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")", {
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
   Description: Get InspResultsShortCharAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_InspResultsShortCharAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsShortCharAttchRow
   */  
export function get_InspResultsShortChars_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_InspResultsShortCharAttches(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsShortCharAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsShortChars(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")/InspResultsShortCharAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsShortCharAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the InspResultsShortCharAttch item
   Description: Calls GetByID to retrieve the InspResultsShortCharAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsShortCharAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsShortCharAttchRow
   */  
export function get_InspResultsShortChars_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_InspResultsShortCharAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InspResultsShortCharAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsShortChars(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")/InspResultsShortCharAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InspResultsShortCharAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get InspResultsShortCharAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspResultsShortCharAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsShortCharAttchRow
   */  
export function get_InspResultsShortCharAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsShortCharAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsShortCharAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsShortCharAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InspResultsShortCharAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InspResultsShortCharAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InspResultsShortCharAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InspResultsShortCharAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsShortCharAttches", {
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
   Summary: Calls GetByID to retrieve the InspResultsShortCharAttch item
   Description: Calls GetByID to retrieve the InspResultsShortCharAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsShortCharAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsShortCharAttchRow
   */  
export function get_InspResultsShortCharAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InspResultsShortCharAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsShortCharAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InspResultsShortCharAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update InspResultsShortCharAttch for the service
   Description: Calls UpdateExt to update InspResultsShortCharAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InspResultsShortCharAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InspResultsShortCharAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_InspResultsShortCharAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsShortCharAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete InspResultsShortCharAttch item
   Description: Call UpdateExt to delete InspResultsShortCharAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InspResultsShortCharAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InspPlanType Desc: InspPlanType   Required: True   Allow empty value : True
      @param File Desc: File   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param SampleNumber Desc: SampleNumber   Required: True
      @param InspectDate Desc: InspectDate   Required: True   Allow empty value : True
      @param InspectTime Desc: InspectTime   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_InspResultsShortCharAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company:string, InspPlanType:string, File:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, SampleNumber:string, InspectDate:string, InspectTime:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/InspResultsShortCharAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseInspResults:string, whereClauseInspResultsAttch:string, whereClauseInspResultsChar:string, whereClauseInspResultsCharAttch:string, whereClauseInspResultsCheckBox:string, whereClauseInspResultsCheckBoxAttch:string, whereClauseInspResultsDate:string, whereClauseInspResultsDateAttch:string, whereClauseInspResultsNum:string, whereClauseInspResultsNumAttch:string, whereClauseInspResultsShortChar:string, whereClauseInspResultsShortCharAttch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseInspResults!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseInspResults=" + whereClauseInspResults
   }
   if(typeof whereClauseInspResultsAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseInspResultsAttch=" + whereClauseInspResultsAttch
   }
   if(typeof whereClauseInspResultsChar!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseInspResultsChar=" + whereClauseInspResultsChar
   }
   if(typeof whereClauseInspResultsCharAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseInspResultsCharAttch=" + whereClauseInspResultsCharAttch
   }
   if(typeof whereClauseInspResultsCheckBox!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseInspResultsCheckBox=" + whereClauseInspResultsCheckBox
   }
   if(typeof whereClauseInspResultsCheckBoxAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseInspResultsCheckBoxAttch=" + whereClauseInspResultsCheckBoxAttch
   }
   if(typeof whereClauseInspResultsDate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseInspResultsDate=" + whereClauseInspResultsDate
   }
   if(typeof whereClauseInspResultsDateAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseInspResultsDateAttch=" + whereClauseInspResultsDateAttch
   }
   if(typeof whereClauseInspResultsNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseInspResultsNum=" + whereClauseInspResultsNum
   }
   if(typeof whereClauseInspResultsNumAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseInspResultsNumAttch=" + whereClauseInspResultsNumAttch
   }
   if(typeof whereClauseInspResultsShortChar!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseInspResultsShortChar=" + whereClauseInspResultsShortChar
   }
   if(typeof whereClauseInspResultsShortCharAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseInspResultsShortCharAttch=" + whereClauseInspResultsShortCharAttch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(inspPlanType:string, file:string, key1:string, key2:string, key3:string, key4:string, key5:string, sampleNumber:string, inspectDate:string, inspectTime:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof inspPlanType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "inspPlanType=" + inspPlanType
   }
   if(typeof file!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "file=" + file
   }
   if(typeof key1!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key1=" + key1
   }
   if(typeof key2!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key2=" + key2
   }
   if(typeof key3!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key3=" + key3
   }
   if(typeof key4!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key4=" + key4
   }
   if(typeof key5!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key5=" + key5
   }
   if(typeof sampleNumber!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "sampleNumber=" + sampleNumber
   }
   if(typeof inspectDate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "inspectDate=" + inspectDate
   }
   if(typeof inspectTime!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "inspectTime=" + inspectTime
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetList" + params, {
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
   Summary: Invoke method GenerateResults
   Description: Generate Sample List
   OperationID: GenerateResults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateResults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateResults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateResults(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GenerateResults", {
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
   Summary: Invoke method GetInspParams
   Description: Get new ttInspParam record to be populated with InspResulsArgs values
   OperationID: GetInspParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInspParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInspParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInspParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetInspParams", {
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
   Summary: Invoke method IsDecimalValue
   Description: Returns if decimal
   OperationID: IsDecimalValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsDecimalValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsDecimalValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsDecimalValue(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/IsDecimalValue", {
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
   Summary: Invoke method ValidateSerialAfterSelect
   Description: Validates after calling SN selection screen
   OperationID: ValidateSerialAfterSelect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSerialAfterSelect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSerialAfterSelect_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSerialAfterSelect(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/ValidateSerialAfterSelect", {
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
   Summary: Invoke method ConvQtysToBase
   Description: Convert Quantities to base qtys for serial number processing
   OperationID: ConvQtysToBase
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConvQtysToBase_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvQtysToBase_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConvQtysToBase(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/ConvQtysToBase", {
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
   Summary: Invoke method GetInspPlanPartNum
   Description: Purpose: finds the inspection plan part number
   OperationID: GetInspPlanPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInspPlanPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInspPlanPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInspPlanPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetInspPlanPartNum", {
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
   Summary: Invoke method GetInspQty
   Description: Get the inspection quantity for the given quantity
   OperationID: GetInspQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInspQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInspQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInspQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetInspQty", {
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
   Summary: Invoke method GetPassedFailed
   Description: Purpose: Gets the Passed/Failed result after calling configuration entry application
   OperationID: GetPassedFailed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPassedFailed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPassedFailed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPassedFailed(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetPassedFailed", {
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
   Summary: Invoke method GetLaborSelectedSerialNumbers
   Description: This method will populate the SelectedSerialNumber datatable for the InspNonConf RowIdent.
   OperationID: GetLaborSelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLaborSelectedSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLaborSelectedSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLaborSelectedSerialNumbers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetLaborSelectedSerialNumbers", {
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
   Summary: Invoke method GetRMASelectedSerialNumbers
   Description: This method will populate the SelectedSerialNumber datatable
   OperationID: GetRMASelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRMASelectedSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRMASelectedSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRMASelectedSerialNumbers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetRMASelectedSerialNumbers", {
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
   Summary: Invoke method ValidateSerialBeforeSelect
   Description: Call before allowing the select of serial numbers
   OperationID: ValidateSerialBeforeSelect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSerialBeforeSelect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSerialBeforeSelect_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSerialBeforeSelect(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/ValidateSerialBeforeSelect", {
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
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Gets parameters required for launching Select Serial Numbers
   OperationID: GetSelectSerialNumbersParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectSerialNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectSerialNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectSerialNumbersParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetSelectSerialNumbersParams", {
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
   Summary: Invoke method GetRMASelectSerialNumbersParams
   Description: Gets parameters required for launching Select Serial Numbers
   OperationID: GetRMASelectSerialNumbersParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRMASelectSerialNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRMASelectSerialNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRMASelectSerialNumbersParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetRMASelectSerialNumbersParams", {
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
   Summary: Invoke method GetSpecID
   Description: Get the specification ID using the given job, assembly, operation, part number
and revision.
   OperationID: GetSpecID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSpecID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSpecID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSpecID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetSpecID", {
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
   Summary: Invoke method GetNonConformanceQty
   OperationID: GetNonConformanceQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNonConformanceQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNonConformanceQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNonConformanceQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetNonConformanceQty", {
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
   Summary: Invoke method OnChangeInspPlan
   Description: This method validates the Proposed InspPlanPartNum, then updates related fields:
            
This method should be run when the InspPlanSampleLst.InspPlanNum field changes.
   OperationID: OnChangeInspPlan
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeInspPlan_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInspPlan_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeInspPlan(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/OnChangeInspPlan", {
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
   Summary: Invoke method UpdateSelectedSN
   Description: This method updates passed/failed value on selectedserialnumbers.
   OperationID: UpdateSelectedSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateSelectedSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateSelectedSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateSelectedSN(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/UpdateSelectedSN", {
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
   Summary: Invoke method OnChangeInspType
   Description: This method wil assign values depending the inspection type selection
This method should be run when the InspParam.InspType field changes.
   OperationID: OnChangeInspType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeInspType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInspType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeInspType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/OnChangeInspType", {
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
   Summary: Invoke method OnChangeJobAsm
   Description: This method validates the ProposedAssemblySeq, then updates related fields:
            
This method should be run when the InspParam.AssemblySeq field changes.
   OperationID: OnChangeJobAsm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeJobAsm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobAsm_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeJobAsm(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/OnChangeJobAsm", {
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
   Summary: Invoke method OnChangeJobNum
   Description: This method validates the JobNum, then updates related fields:
This method should be run when the InspParam.JobNum field changes.
   OperationID: OnChangeJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeJobNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/OnChangeJobNum", {
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
   Summary: Invoke method OnChangeJobOpr
   Description: This method validates the piProposedOprSeq, then updates related fields:
            
This method should be run when the InspParam.OprSeq field changes.
   OperationID: OnChangeJobOpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeJobOpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobOpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeJobOpr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/OnChangeJobOpr", {
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
   Summary: Invoke method OnChangeNCMID
   Description: This method validates the non conformance transaction ID, then updates related fields
This method should be run when the InspParam.NCMTranID field changes.
   OperationID: OnChangeNCMID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeNCMID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeNCMID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeNCMID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/OnChangeNCMID", {
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
   Summary: Invoke method OnChangePartNum
   Description: This method validates the piProposedPartNum, then updates related fields.
            
This method should be run when the InspParam.PartNum field changes.
   OperationID: OnChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/OnChangePartNum", {
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
   Summary: Invoke method OnChangeSpecID
   Description: This method validates the Proposed Specification ID, then updates related fields:
            
This method should be run when the InspPlanSampleLst.SpecID field changes.
   OperationID: OnChangeSpecID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSpecID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSpecID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSpecID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/OnChangeSpecID", {
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
   Summary: Invoke method OnChangeSpecRev
   Description: This method processes the Proposed Specification Revision, then updates related fields:
            
This method should be run when the InspParam.SpecRev field changes.
   OperationID: OnChangeSpecRev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSpecRev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSpecRev_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSpecRev(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/OnChangeSpecRev", {
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
   Summary: Invoke method PreGenerateResults
   Description: This method should be called prior to calling the GenerateResults method.  It will
validate InspParam data and check for existing InspResults records.
   OperationID: PreGenerateResults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreGenerateResults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreGenerateResults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreGenerateResults(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/PreGenerateResults", {
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
   Summary: Invoke method PreGenerateResultsForSpecification
   Description: This method should be called prior to calling the GenerateResults method.  It will
validate InspParam data and check for existing InspResults records.  This method does
not require an inspection plan to have a configuration.
   OperationID: PreGenerateResultsForSpecification
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreGenerateResultsForSpecification_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreGenerateResultsForSpecification_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreGenerateResultsForSpecification(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/PreGenerateResultsForSpecification", {
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
   Summary: Invoke method GetDisplayColumns
   Description: Generate Columns that will be displayed in the grid
   OperationID: GetDisplayColumns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDisplayColumns_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDisplayColumns_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDisplayColumns(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetDisplayColumns", {
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
   Summary: Invoke method RetrieveValues
   Description: Retrieve records that will be displayed in the grid.
   OperationID: RetrieveValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RetrieveValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RetrieveValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RetrieveValues(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/RetrieveValues", {
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
   Summary: Invoke method GetNewLbrScrapSerialNumbers
   Description: Gets a new LbrScrapSerialNumbers record for current InspParam
   OperationID: GetNewLbrScrapSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLbrScrapSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLbrScrapSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLbrScrapSerialNumbers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetNewLbrScrapSerialNumbers", {
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
   Summary: Invoke method GetCodeDescList
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetCodeDescList", {
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
   Summary: Invoke method buildRetrieveValues
   Description: Retrieve created dataset for Kinetic
   OperationID: buildRetrieveValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/buildRetrieveValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/buildRetrieveValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_buildRetrieveValues(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/buildRetrieveValues", {
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
   Summary: Invoke method CreateLbrScrapSerialNumbersFromList
   Description: Create LbrScrapSerialNumbers dataset records from a list of selected serial numbers
   OperationID: CreateLbrScrapSerialNumbersFromList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateLbrScrapSerialNumbersFromList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateLbrScrapSerialNumbersFromList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateLbrScrapSerialNumbersFromList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/CreateLbrScrapSerialNumbersFromList", {
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
   Summary: Invoke method GetResults
   Description: Gets inspection results for entry
   OperationID: GetResults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetResults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetResults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetResults(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetResults", {
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
   Summary: Invoke method UpdateDynamicResults
   Description: Update inspection results
   OperationID: UpdateDynamicResults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateDynamicResults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateDynamicResults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateDynamicResults(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/UpdateDynamicResults", {
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
   Summary: Invoke method GetNewInspResults
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInspResults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInspResults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInspResults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewInspResults(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetNewInspResults", {
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
   Summary: Invoke method GetNewInspResultsAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInspResultsAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInspResultsAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInspResultsAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewInspResultsAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetNewInspResultsAttch", {
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
   Summary: Invoke method GetNewInspResultsChar
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInspResultsChar
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInspResultsChar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInspResultsChar_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewInspResultsChar(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetNewInspResultsChar", {
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
   Summary: Invoke method GetNewInspResultsCharAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInspResultsCharAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInspResultsCharAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInspResultsCharAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewInspResultsCharAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetNewInspResultsCharAttch", {
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
   Summary: Invoke method GetNewInspResultsCheckBox
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInspResultsCheckBox
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInspResultsCheckBox_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInspResultsCheckBox_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewInspResultsCheckBox(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetNewInspResultsCheckBox", {
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
   Summary: Invoke method GetNewInspResultsCheckBoxAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInspResultsCheckBoxAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInspResultsCheckBoxAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInspResultsCheckBoxAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewInspResultsCheckBoxAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetNewInspResultsCheckBoxAttch", {
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
   Summary: Invoke method GetNewInspResultsDate
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInspResultsDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInspResultsDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInspResultsDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewInspResultsDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetNewInspResultsDate", {
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
   Summary: Invoke method GetNewInspResultsDateAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInspResultsDateAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInspResultsDateAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInspResultsDateAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewInspResultsDateAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetNewInspResultsDateAttch", {
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
   Summary: Invoke method GetNewInspResultsNum
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInspResultsNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInspResultsNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInspResultsNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewInspResultsNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetNewInspResultsNum", {
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
   Summary: Invoke method GetNewInspResultsNumAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInspResultsNumAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInspResultsNumAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInspResultsNumAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewInspResultsNumAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetNewInspResultsNumAttch", {
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
   Summary: Invoke method GetNewInspResultsShortChar
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInspResultsShortChar
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInspResultsShortChar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInspResultsShortChar_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewInspResultsShortChar(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetNewInspResultsShortChar", {
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
   Summary: Invoke method GetNewInspResultsShortCharAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInspResultsShortCharAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInspResultsShortCharAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInspResultsShortCharAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewInspResultsShortCharAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetNewInspResultsShortCharAttch", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InspResultsSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InspResultsAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsCharAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InspResultsCharAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsCharRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InspResultsCharRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsCheckBoxAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InspResultsCheckBoxAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsCheckBoxRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InspResultsCheckBoxRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsDateAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InspResultsDateAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsDateRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InspResultsDateRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InspResultsListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsNumAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InspResultsNumAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsNumRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InspResultsNumRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InspResultsRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsShortCharAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InspResultsShortCharAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsShortCharRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InspResultsShortCharRow[],
}

export interface Erp_Tablesets_InspResultsAttchRow{
   "Company":string,
   "InspPlanType":string,
   "File":string,
   "Key1":string,
   "Key2":string,
   "Key3":string,
   "Key4":string,
   "Key5":string,
   "SampleNumber":number,
   "InspectDate":string,
   "InspectTime":number,
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

export interface Erp_Tablesets_InspResultsCharAttchRow{
   "Company":string,
   "InspPlanType":string,
   "File":string,
   "Key1":string,
   "Key2":string,
   "Key3":string,
   "Key4":string,
   "Key5":string,
   "SampleNumber":number,
   "InspectDate":string,
   "InspectTime":number,
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

export interface Erp_Tablesets_InspResultsCharRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Inspection Plan Type - Inspection, Audit, or Survey  */  
   "InspPlanType":string,
      /**  The name of the table that this record pertains to.  */  
   "File":string,
      /**  Major component of the primary key to the record.  */  
   "Key1":string,
      /**   2nd component of the primary key to the related record.
For example: For a "OrderDtl"   this field would contain the OrderLine # of the related Order detail record.  The usage of this field is dependant on the type of record.  For example "Part" references do not use this field while PartRev  would.  */  
   "Key2":string,
      /**   3rd component of the primary key to the related record.
For example: For a "OrderRel"   this field would contain the Order Line Release # of the related Order Release record.  The usage of this field is dependant on the type of record referenced.  */  
   "Key3":string,
      /**  4th component of the primary key to the related record.  */  
   "Key4":string,
      /**  5th component of the primary key to the related record.  */  
   "Key5":string,
      /**  A sequential number up to the total in the Inspection Quantity field.  */  
   "SampleNumber":number,
      /**  Date the inspection data was saved  */  
   "InspectDate":string,
      /**  System time (seconds since midnight) of when the inspection data was saved  */  
   "InspectTime":number,
      /**  Character001  */  
   "Character001":string,
      /**  Character002  */  
   "Character002":string,
      /**  Character003  */  
   "Character003":string,
      /**  Character004  */  
   "Character004":string,
      /**  Character005  */  
   "Character005":string,
      /**  Character006  */  
   "Character006":string,
      /**  Character007  */  
   "Character007":string,
      /**  Character008  */  
   "Character008":string,
      /**  Character009  */  
   "Character009":string,
      /**  Character010  */  
   "Character010":string,
      /**  Character011  */  
   "Character011":string,
      /**  Character012  */  
   "Character012":string,
      /**  Character013  */  
   "Character013":string,
      /**  Character014  */  
   "Character014":string,
      /**  Character015  */  
   "Character015":string,
      /**  Character016  */  
   "Character016":string,
      /**  Character017  */  
   "Character017":string,
      /**  Character018  */  
   "Character018":string,
      /**  Character019  */  
   "Character019":string,
      /**  Character020  */  
   "Character020":string,
      /**  Character021  */  
   "Character021":string,
      /**  Character022  */  
   "Character022":string,
      /**  Character023  */  
   "Character023":string,
      /**  Character024  */  
   "Character024":string,
      /**  Character025  */  
   "Character025":string,
      /**  Character026  */  
   "Character026":string,
      /**  Character027  */  
   "Character027":string,
      /**  Character028  */  
   "Character028":string,
      /**  Character029  */  
   "Character029":string,
      /**  Character030  */  
   "Character030":string,
      /**  Character031  */  
   "Character031":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_InspResultsCheckBoxAttchRow{
   "Company":string,
   "InspPlanType":string,
   "File":string,
   "Key1":string,
   "Key2":string,
   "Key3":string,
   "Key4":string,
   "Key5":string,
   "SampleNumber":number,
   "InspectDate":string,
   "InspectTime":number,
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

export interface Erp_Tablesets_InspResultsCheckBoxRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Inspection Plan Type - Inspection, Audit, Survey  */  
   "InspPlanType":string,
      /**  The name of the table that this record pertains to.  */  
   "File":string,
      /**  Major component of the primary key to the record.  */  
   "Key1":string,
      /**   2nd component of the primary key to the related record.
For example: For a "OrderDtl"   this field would contain the OrderLine # of the related Order detail record.  The usage of this field is dependant on the type of record.  For example "Part" references do not use this field while PartRev  would.  */  
   "Key2":string,
      /**   3rd component of the primary key to the related record.
For example: For a "OrderRel"   this field would contain the Order Line Release # of the related Order Release record.  The usage of this field is dependant on the type of record referenced.  */  
   "Key3":string,
      /**  4th component of the primary key to the related record.  */  
   "Key4":string,
      /**  5th component of the primary key to the related record.  */  
   "Key5":string,
      /**  A sequential number up to the total in the Inspection Quantity field.  */  
   "SampleNumber":number,
      /**  Date the inspection data was saved  */  
   "InspectDate":string,
      /**  System time (seconds since midnight) of when the inspection data was saved  */  
   "InspectTime":number,
      /**  CheckBox001  */  
   "CheckBox001":boolean,
      /**  CheckBox002  */  
   "CheckBox002":boolean,
      /**  CheckBox003  */  
   "CheckBox003":boolean,
      /**  CheckBox004  */  
   "CheckBox004":boolean,
      /**  CheckBox005  */  
   "CheckBox005":boolean,
      /**  CheckBox006  */  
   "CheckBox006":boolean,
      /**  CheckBox007  */  
   "CheckBox007":boolean,
      /**  CheckBox008  */  
   "CheckBox008":boolean,
      /**  CheckBox009  */  
   "CheckBox009":boolean,
      /**  CheckBox010  */  
   "CheckBox010":boolean,
      /**  CheckBox011  */  
   "CheckBox011":boolean,
      /**  CheckBox012  */  
   "CheckBox012":boolean,
      /**  CheckBox013  */  
   "CheckBox013":boolean,
      /**  CheckBox014  */  
   "CheckBox014":boolean,
      /**  CheckBox015  */  
   "CheckBox015":boolean,
      /**  CheckBox016  */  
   "CheckBox016":boolean,
      /**  CheckBox017  */  
   "CheckBox017":boolean,
      /**  CheckBox018  */  
   "CheckBox018":boolean,
      /**  CheckBox019  */  
   "CheckBox019":boolean,
      /**  CheckBox020  */  
   "CheckBox020":boolean,
      /**  CheckBox021  */  
   "CheckBox021":boolean,
      /**  CheckBox022  */  
   "CheckBox022":boolean,
      /**  CheckBox023  */  
   "CheckBox023":boolean,
      /**  CheckBox024  */  
   "CheckBox024":boolean,
      /**  CheckBox025  */  
   "CheckBox025":boolean,
      /**  CheckBox026  */  
   "CheckBox026":boolean,
      /**  CheckBox027  */  
   "CheckBox027":boolean,
      /**  CheckBox028  */  
   "CheckBox028":boolean,
      /**  CheckBox029  */  
   "CheckBox029":boolean,
      /**  CheckBox030  */  
   "CheckBox030":boolean,
      /**  CheckBox031  */  
   "CheckBox031":boolean,
      /**  CheckBox032  */  
   "CheckBox032":boolean,
      /**  CheckBox033  */  
   "CheckBox033":boolean,
      /**  CheckBox034  */  
   "CheckBox034":boolean,
      /**  CheckBox035  */  
   "CheckBox035":boolean,
      /**  CheckBox036  */  
   "CheckBox036":boolean,
      /**  CheckBox037  */  
   "CheckBox037":boolean,
      /**  CheckBox038  */  
   "CheckBox038":boolean,
      /**  CheckBox039  */  
   "CheckBox039":boolean,
      /**  CheckBox040  */  
   "CheckBox040":boolean,
      /**  CheckBox041  */  
   "CheckBox041":boolean,
      /**  CheckBox042  */  
   "CheckBox042":boolean,
      /**  CheckBox043  */  
   "CheckBox043":boolean,
      /**  CheckBox044  */  
   "CheckBox044":boolean,
      /**  CheckBox045  */  
   "CheckBox045":boolean,
      /**  CheckBox046  */  
   "CheckBox046":boolean,
      /**  CheckBox047  */  
   "CheckBox047":boolean,
      /**  CheckBox048  */  
   "CheckBox048":boolean,
      /**  CheckBox049  */  
   "CheckBox049":boolean,
      /**  CheckBox050  */  
   "CheckBox050":boolean,
      /**  CheckBox051  */  
   "CheckBox051":boolean,
      /**  CheckBox052  */  
   "CheckBox052":boolean,
      /**  CheckBox053  */  
   "CheckBox053":boolean,
      /**  CheckBox054  */  
   "CheckBox054":boolean,
      /**  CheckBox055  */  
   "CheckBox055":boolean,
      /**  CheckBox056  */  
   "CheckBox056":boolean,
      /**  CheckBox057  */  
   "CheckBox057":boolean,
      /**  CheckBox058  */  
   "CheckBox058":boolean,
      /**  CheckBox059  */  
   "CheckBox059":boolean,
      /**  CheckBox060  */  
   "CheckBox060":boolean,
      /**  CheckBox061  */  
   "CheckBox061":boolean,
      /**  CheckBox062  */  
   "CheckBox062":boolean,
      /**  CheckBox063  */  
   "CheckBox063":boolean,
      /**  CheckBox064  */  
   "CheckBox064":boolean,
      /**  CheckBox065  */  
   "CheckBox065":boolean,
      /**  CheckBox066  */  
   "CheckBox066":boolean,
      /**  CheckBox067  */  
   "CheckBox067":boolean,
      /**  CheckBox068  */  
   "CheckBox068":boolean,
      /**  CheckBox069  */  
   "CheckBox069":boolean,
      /**  CheckBox070  */  
   "CheckBox070":boolean,
      /**  CheckBox071  */  
   "CheckBox071":boolean,
      /**  CheckBox072  */  
   "CheckBox072":boolean,
      /**  CheckBox073  */  
   "CheckBox073":boolean,
      /**  CheckBox074  */  
   "CheckBox074":boolean,
      /**  CheckBox075  */  
   "CheckBox075":boolean,
      /**  CheckBox076  */  
   "CheckBox076":boolean,
      /**  CheckBox077  */  
   "CheckBox077":boolean,
      /**  CheckBox078  */  
   "CheckBox078":boolean,
      /**  CheckBox079  */  
   "CheckBox079":boolean,
      /**  CheckBox080  */  
   "CheckBox080":boolean,
      /**  CheckBox081  */  
   "CheckBox081":boolean,
      /**  CheckBox082  */  
   "CheckBox082":boolean,
      /**  CheckBox083  */  
   "CheckBox083":boolean,
      /**  CheckBox084  */  
   "CheckBox084":boolean,
      /**  CheckBox085  */  
   "CheckBox085":boolean,
      /**  CheckBox086  */  
   "CheckBox086":boolean,
      /**  CheckBox087  */  
   "CheckBox087":boolean,
      /**  CheckBox088  */  
   "CheckBox088":boolean,
      /**  CheckBox089  */  
   "CheckBox089":boolean,
      /**  CheckBox090  */  
   "CheckBox090":boolean,
      /**  CheckBox091  */  
   "CheckBox091":boolean,
      /**  CheckBox092  */  
   "CheckBox092":boolean,
      /**  CheckBox093  */  
   "CheckBox093":boolean,
      /**  CheckBox094  */  
   "CheckBox094":boolean,
      /**  CheckBox095  */  
   "CheckBox095":boolean,
      /**  CheckBox096  */  
   "CheckBox096":boolean,
      /**  CheckBox097  */  
   "CheckBox097":boolean,
      /**  CheckBox098  */  
   "CheckBox098":boolean,
      /**  CheckBox099  */  
   "CheckBox099":boolean,
      /**  CheckBox100  */  
   "CheckBox100":boolean,
      /**  CheckBox101  */  
   "CheckBox101":boolean,
      /**  CheckBox102  */  
   "CheckBox102":boolean,
      /**  CheckBox103  */  
   "CheckBox103":boolean,
      /**  CheckBox104  */  
   "CheckBox104":boolean,
      /**  CheckBox105  */  
   "CheckBox105":boolean,
      /**  CheckBox106  */  
   "CheckBox106":boolean,
      /**  CheckBox107  */  
   "CheckBox107":boolean,
      /**  CheckBox108  */  
   "CheckBox108":boolean,
      /**  CheckBox109  */  
   "CheckBox109":boolean,
      /**  CheckBox110  */  
   "CheckBox110":boolean,
      /**  CheckBox111  */  
   "CheckBox111":boolean,
      /**  CheckBox112  */  
   "CheckBox112":boolean,
      /**  CheckBox113  */  
   "CheckBox113":boolean,
      /**  CheckBox114  */  
   "CheckBox114":boolean,
      /**  CheckBox115  */  
   "CheckBox115":boolean,
      /**  CheckBox116  */  
   "CheckBox116":boolean,
      /**  CheckBox117  */  
   "CheckBox117":boolean,
      /**  CheckBox118  */  
   "CheckBox118":boolean,
      /**  CheckBox119  */  
   "CheckBox119":boolean,
      /**  CheckBox120  */  
   "CheckBox120":boolean,
      /**  CheckBox121  */  
   "CheckBox121":boolean,
      /**  CheckBox122  */  
   "CheckBox122":boolean,
      /**  CheckBox123  */  
   "CheckBox123":boolean,
      /**  CheckBox124  */  
   "CheckBox124":boolean,
      /**  CheckBox125  */  
   "CheckBox125":boolean,
      /**  CheckBox126  */  
   "CheckBox126":boolean,
      /**  CheckBox127  */  
   "CheckBox127":boolean,
      /**  CheckBox128  */  
   "CheckBox128":boolean,
      /**  CheckBox129  */  
   "CheckBox129":boolean,
      /**  CheckBox130  */  
   "CheckBox130":boolean,
      /**  CheckBox131  */  
   "CheckBox131":boolean,
      /**  CheckBox132  */  
   "CheckBox132":boolean,
      /**  CheckBox133  */  
   "CheckBox133":boolean,
      /**  CheckBox134  */  
   "CheckBox134":boolean,
      /**  CheckBox135  */  
   "CheckBox135":boolean,
      /**  CheckBox136  */  
   "CheckBox136":boolean,
      /**  CheckBox137  */  
   "CheckBox137":boolean,
      /**  CheckBox138  */  
   "CheckBox138":boolean,
      /**  CheckBox139  */  
   "CheckBox139":boolean,
      /**  CheckBox140  */  
   "CheckBox140":boolean,
      /**  CheckBox141  */  
   "CheckBox141":boolean,
      /**  CheckBox142  */  
   "CheckBox142":boolean,
      /**  CheckBox143  */  
   "CheckBox143":boolean,
      /**  CheckBox144  */  
   "CheckBox144":boolean,
      /**  CheckBox145  */  
   "CheckBox145":boolean,
      /**  CheckBox146  */  
   "CheckBox146":boolean,
      /**  CheckBox147  */  
   "CheckBox147":boolean,
      /**  CheckBox148  */  
   "CheckBox148":boolean,
      /**  CheckBox149  */  
   "CheckBox149":boolean,
      /**  CheckBox150  */  
   "CheckBox150":boolean,
      /**  CheckBox151  */  
   "CheckBox151":boolean,
      /**  CheckBox152  */  
   "CheckBox152":boolean,
      /**  CheckBox153  */  
   "CheckBox153":boolean,
      /**  CheckBox154  */  
   "CheckBox154":boolean,
      /**  CheckBox155  */  
   "CheckBox155":boolean,
      /**  CheckBox156  */  
   "CheckBox156":boolean,
      /**  CheckBox157  */  
   "CheckBox157":boolean,
      /**  CheckBox158  */  
   "CheckBox158":boolean,
      /**  CheckBox159  */  
   "CheckBox159":boolean,
      /**  CheckBox160  */  
   "CheckBox160":boolean,
      /**  CheckBox161  */  
   "CheckBox161":boolean,
      /**  CheckBox162  */  
   "CheckBox162":boolean,
      /**  CheckBox163  */  
   "CheckBox163":boolean,
      /**  CheckBox164  */  
   "CheckBox164":boolean,
      /**  CheckBox165  */  
   "CheckBox165":boolean,
      /**  CheckBox166  */  
   "CheckBox166":boolean,
      /**  CheckBox167  */  
   "CheckBox167":boolean,
      /**  CheckBox168  */  
   "CheckBox168":boolean,
      /**  CheckBox169  */  
   "CheckBox169":boolean,
      /**  CheckBox170  */  
   "CheckBox170":boolean,
      /**  CheckBox171  */  
   "CheckBox171":boolean,
      /**  CheckBox172  */  
   "CheckBox172":boolean,
      /**  CheckBox173  */  
   "CheckBox173":boolean,
      /**  CheckBox174  */  
   "CheckBox174":boolean,
      /**  CheckBox175  */  
   "CheckBox175":boolean,
      /**  CheckBox176  */  
   "CheckBox176":boolean,
      /**  CheckBox177  */  
   "CheckBox177":boolean,
      /**  CheckBox178  */  
   "CheckBox178":boolean,
      /**  CheckBox179  */  
   "CheckBox179":boolean,
      /**  CheckBox180  */  
   "CheckBox180":boolean,
      /**  CheckBox181  */  
   "CheckBox181":boolean,
      /**  CheckBox182  */  
   "CheckBox182":boolean,
      /**  CheckBox183  */  
   "CheckBox183":boolean,
      /**  CheckBox184  */  
   "CheckBox184":boolean,
      /**  CheckBox185  */  
   "CheckBox185":boolean,
      /**  CheckBox186  */  
   "CheckBox186":boolean,
      /**  CheckBox187  */  
   "CheckBox187":boolean,
      /**  CheckBox188  */  
   "CheckBox188":boolean,
      /**  CheckBox189  */  
   "CheckBox189":boolean,
      /**  CheckBox190  */  
   "CheckBox190":boolean,
      /**  CheckBox191  */  
   "CheckBox191":boolean,
      /**  CheckBox192  */  
   "CheckBox192":boolean,
      /**  CheckBox193  */  
   "CheckBox193":boolean,
      /**  CheckBox194  */  
   "CheckBox194":boolean,
      /**  CheckBox195  */  
   "CheckBox195":boolean,
      /**  CheckBox196  */  
   "CheckBox196":boolean,
      /**  CheckBox197  */  
   "CheckBox197":boolean,
      /**  CheckBox198  */  
   "CheckBox198":boolean,
      /**  CheckBox199  */  
   "CheckBox199":boolean,
      /**  CheckBox200  */  
   "CheckBox200":boolean,
      /**  CheckBox201  */  
   "CheckBox201":boolean,
      /**  CheckBox202  */  
   "CheckBox202":boolean,
      /**  CheckBox203  */  
   "CheckBox203":boolean,
      /**  CheckBox204  */  
   "CheckBox204":boolean,
      /**  CheckBox205  */  
   "CheckBox205":boolean,
      /**  CheckBox206  */  
   "CheckBox206":boolean,
      /**  CheckBox207  */  
   "CheckBox207":boolean,
      /**  CheckBox208  */  
   "CheckBox208":boolean,
      /**  CheckBox209  */  
   "CheckBox209":boolean,
      /**  CheckBox210  */  
   "CheckBox210":boolean,
      /**  CheckBox211  */  
   "CheckBox211":boolean,
      /**  CheckBox212  */  
   "CheckBox212":boolean,
      /**  CheckBox213  */  
   "CheckBox213":boolean,
      /**  CheckBox214  */  
   "CheckBox214":boolean,
      /**  CheckBox215  */  
   "CheckBox215":boolean,
      /**  CheckBox216  */  
   "CheckBox216":boolean,
      /**  CheckBox217  */  
   "CheckBox217":boolean,
      /**  CheckBox218  */  
   "CheckBox218":boolean,
      /**  CheckBox219  */  
   "CheckBox219":boolean,
      /**  CheckBox220  */  
   "CheckBox220":boolean,
      /**  CheckBox221  */  
   "CheckBox221":boolean,
      /**  CheckBox222  */  
   "CheckBox222":boolean,
      /**  CheckBox223  */  
   "CheckBox223":boolean,
      /**  CheckBox224  */  
   "CheckBox224":boolean,
      /**  CheckBox225  */  
   "CheckBox225":boolean,
      /**  CheckBox226  */  
   "CheckBox226":boolean,
      /**  CheckBox227  */  
   "CheckBox227":boolean,
      /**  CheckBox228  */  
   "CheckBox228":boolean,
      /**  CheckBox229  */  
   "CheckBox229":boolean,
      /**  CheckBox230  */  
   "CheckBox230":boolean,
      /**  CheckBox231  */  
   "CheckBox231":boolean,
      /**  CheckBox232  */  
   "CheckBox232":boolean,
      /**  CheckBox233  */  
   "CheckBox233":boolean,
      /**  CheckBox234  */  
   "CheckBox234":boolean,
      /**  CheckBox235  */  
   "CheckBox235":boolean,
      /**  CheckBox236  */  
   "CheckBox236":boolean,
      /**  CheckBox237  */  
   "CheckBox237":boolean,
      /**  CheckBox238  */  
   "CheckBox238":boolean,
      /**  CheckBox239  */  
   "CheckBox239":boolean,
      /**  CheckBox240  */  
   "CheckBox240":boolean,
      /**  CheckBox241  */  
   "CheckBox241":boolean,
      /**  CheckBox242  */  
   "CheckBox242":boolean,
      /**  CheckBox243  */  
   "CheckBox243":boolean,
      /**  CheckBox244  */  
   "CheckBox244":boolean,
      /**  CheckBox245  */  
   "CheckBox245":boolean,
      /**  CheckBox246  */  
   "CheckBox246":boolean,
      /**  CheckBox247  */  
   "CheckBox247":boolean,
      /**  CheckBox248  */  
   "CheckBox248":boolean,
      /**  CheckBox249  */  
   "CheckBox249":boolean,
      /**  CheckBox250  */  
   "CheckBox250":boolean,
      /**  CheckBox251  */  
   "CheckBox251":boolean,
      /**  CheckBox252  */  
   "CheckBox252":boolean,
      /**  CheckBox253  */  
   "CheckBox253":boolean,
      /**  CheckBox254  */  
   "CheckBox254":boolean,
      /**  CheckBox255  */  
   "CheckBox255":boolean,
      /**  CheckBox256  */  
   "CheckBox256":boolean,
      /**  CheckBox257  */  
   "CheckBox257":boolean,
      /**  CheckBox258  */  
   "CheckBox258":boolean,
      /**  CheckBox259  */  
   "CheckBox259":boolean,
      /**  CheckBox260  */  
   "CheckBox260":boolean,
      /**  CheckBox261  */  
   "CheckBox261":boolean,
      /**  CheckBox262  */  
   "CheckBox262":boolean,
      /**  CheckBox263  */  
   "CheckBox263":boolean,
      /**  CheckBox264  */  
   "CheckBox264":boolean,
      /**  CheckBox265  */  
   "CheckBox265":boolean,
      /**  CheckBox266  */  
   "CheckBox266":boolean,
      /**  CheckBox267  */  
   "CheckBox267":boolean,
      /**  CheckBox268  */  
   "CheckBox268":boolean,
      /**  CheckBox269  */  
   "CheckBox269":boolean,
      /**  CheckBox270  */  
   "CheckBox270":boolean,
      /**  CheckBox271  */  
   "CheckBox271":boolean,
      /**  CheckBox272  */  
   "CheckBox272":boolean,
      /**  CheckBox273  */  
   "CheckBox273":boolean,
      /**  CheckBox274  */  
   "CheckBox274":boolean,
      /**  CheckBox275  */  
   "CheckBox275":boolean,
      /**  CheckBox276  */  
   "CheckBox276":boolean,
      /**  CheckBox277  */  
   "CheckBox277":boolean,
      /**  CheckBox278  */  
   "CheckBox278":boolean,
      /**  CheckBox279  */  
   "CheckBox279":boolean,
      /**  CheckBox280  */  
   "CheckBox280":boolean,
      /**  CheckBox281  */  
   "CheckBox281":boolean,
      /**  CheckBox282  */  
   "CheckBox282":boolean,
      /**  CheckBox283  */  
   "CheckBox283":boolean,
      /**  CheckBox284  */  
   "CheckBox284":boolean,
      /**  CheckBox285  */  
   "CheckBox285":boolean,
      /**  CheckBox286  */  
   "CheckBox286":boolean,
      /**  CheckBox287  */  
   "CheckBox287":boolean,
      /**  CheckBox288  */  
   "CheckBox288":boolean,
      /**  CheckBox289  */  
   "CheckBox289":boolean,
      /**  CheckBox290  */  
   "CheckBox290":boolean,
      /**  CheckBox291  */  
   "CheckBox291":boolean,
      /**  CheckBox292  */  
   "CheckBox292":boolean,
      /**  CheckBox293  */  
   "CheckBox293":boolean,
      /**  CheckBox294  */  
   "CheckBox294":boolean,
      /**  CheckBox295  */  
   "CheckBox295":boolean,
      /**  CheckBox296  */  
   "CheckBox296":boolean,
      /**  CheckBox297  */  
   "CheckBox297":boolean,
      /**  CheckBox298  */  
   "CheckBox298":boolean,
      /**  CheckBox299  */  
   "CheckBox299":boolean,
      /**  CheckBox300  */  
   "CheckBox300":boolean,
      /**  CheckBox301  */  
   "CheckBox301":boolean,
      /**  CheckBox302  */  
   "CheckBox302":boolean,
      /**  CheckBox303  */  
   "CheckBox303":boolean,
      /**  CheckBox304  */  
   "CheckBox304":boolean,
      /**  CheckBox305  */  
   "CheckBox305":boolean,
      /**  CheckBox306  */  
   "CheckBox306":boolean,
      /**  CheckBox307  */  
   "CheckBox307":boolean,
      /**  CheckBox308  */  
   "CheckBox308":boolean,
      /**  CheckBox309  */  
   "CheckBox309":boolean,
      /**  CheckBox310  */  
   "CheckBox310":boolean,
      /**  CheckBox311  */  
   "CheckBox311":boolean,
      /**  CheckBox312  */  
   "CheckBox312":boolean,
      /**  CheckBox313  */  
   "CheckBox313":boolean,
      /**  CheckBox314  */  
   "CheckBox314":boolean,
      /**  CheckBox315  */  
   "CheckBox315":boolean,
      /**  CheckBox316  */  
   "CheckBox316":boolean,
      /**  CheckBox317  */  
   "CheckBox317":boolean,
      /**  CheckBox318  */  
   "CheckBox318":boolean,
      /**  CheckBox319  */  
   "CheckBox319":boolean,
      /**  CheckBox320  */  
   "CheckBox320":boolean,
      /**  CheckBox321  */  
   "CheckBox321":boolean,
      /**  CheckBox322  */  
   "CheckBox322":boolean,
      /**  CheckBox323  */  
   "CheckBox323":boolean,
      /**  CheckBox324  */  
   "CheckBox324":boolean,
      /**  CheckBox325  */  
   "CheckBox325":boolean,
      /**  CheckBox326  */  
   "CheckBox326":boolean,
      /**  CheckBox327  */  
   "CheckBox327":boolean,
      /**  CheckBox328  */  
   "CheckBox328":boolean,
      /**  CheckBox329  */  
   "CheckBox329":boolean,
      /**  CheckBox330  */  
   "CheckBox330":boolean,
      /**  CheckBox331  */  
   "CheckBox331":boolean,
      /**  CheckBox332  */  
   "CheckBox332":boolean,
      /**  CheckBox333  */  
   "CheckBox333":boolean,
      /**  CheckBox334  */  
   "CheckBox334":boolean,
      /**  CheckBox335  */  
   "CheckBox335":boolean,
      /**  CheckBox336  */  
   "CheckBox336":boolean,
      /**  CheckBox337  */  
   "CheckBox337":boolean,
      /**  CheckBox338  */  
   "CheckBox338":boolean,
      /**  CheckBox339  */  
   "CheckBox339":boolean,
      /**  CheckBox340  */  
   "CheckBox340":boolean,
      /**  CheckBox341  */  
   "CheckBox341":boolean,
      /**  CheckBox342  */  
   "CheckBox342":boolean,
      /**  CheckBox343  */  
   "CheckBox343":boolean,
      /**  CheckBox344  */  
   "CheckBox344":boolean,
      /**  CheckBox345  */  
   "CheckBox345":boolean,
      /**  CheckBox346  */  
   "CheckBox346":boolean,
      /**  CheckBox347  */  
   "CheckBox347":boolean,
      /**  CheckBox348  */  
   "CheckBox348":boolean,
      /**  CheckBox349  */  
   "CheckBox349":boolean,
      /**  CheckBox350  */  
   "CheckBox350":boolean,
      /**  CheckBox351  */  
   "CheckBox351":boolean,
      /**  CheckBox352  */  
   "CheckBox352":boolean,
      /**  CheckBox353  */  
   "CheckBox353":boolean,
      /**  CheckBox354  */  
   "CheckBox354":boolean,
      /**  CheckBox355  */  
   "CheckBox355":boolean,
      /**  CheckBox356  */  
   "CheckBox356":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_InspResultsDateAttchRow{
   "Company":string,
   "InspPlanType":string,
   "File":string,
   "Key1":string,
   "Key2":string,
   "Key3":string,
   "Key4":string,
   "Key5":string,
   "SampleNumber":number,
   "InspectDate":string,
   "InspectTime":number,
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

export interface Erp_Tablesets_InspResultsDateRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Inspection Plan Type - Inspection, Audit, or Survey  */  
   "InspPlanType":string,
      /**  The name of the table that this record pertains to.  */  
   "File":string,
      /**  Major component of the primary key to the record.  */  
   "Key1":string,
      /**   2nd component of the primary key to the related record.
For example: For a "OrderDtl"   this field would contain the OrderLine # of the related Order detail record.  The usage of this field is dependant on the type of record.  For example "Part" references do not use this field while PartRev  would.  */  
   "Key2":string,
      /**   3rd component of the primary key to the related record.
For example: For a "OrderRel"   this field would contain the Order Line Release # of the related Order Release record.  The usage of this field is dependant on the type of record referenced.  */  
   "Key3":string,
      /**  4th component of the primary key to the related record.  */  
   "Key4":string,
      /**  5th component of the primary key to the related record.  */  
   "Key5":string,
      /**  A sequential number up to the total in the Inspection Quantity field.  */  
   "SampleNumber":number,
      /**  Date the inspection data was saved  */  
   "InspectDate":string,
      /**  System time (seconds since midnight) of when the inspection data was saved  */  
   "InspectTime":number,
      /**  Date001  */  
   "Date001":string,
      /**  Date002  */  
   "Date002":string,
      /**  Date003  */  
   "Date003":string,
      /**  Date004  */  
   "Date004":string,
      /**  Date005  */  
   "Date005":string,
      /**  Date006  */  
   "Date006":string,
      /**  Date007  */  
   "Date007":string,
      /**  Date008  */  
   "Date008":string,
      /**  Date009  */  
   "Date009":string,
      /**  Date010  */  
   "Date010":string,
      /**  Date011  */  
   "Date011":string,
      /**  Date012  */  
   "Date012":string,
      /**  Date013  */  
   "Date013":string,
      /**  Date014  */  
   "Date014":string,
      /**  Date015  */  
   "Date015":string,
      /**  Date016  */  
   "Date016":string,
      /**  Date017  */  
   "Date017":string,
      /**  Date018  */  
   "Date018":string,
      /**  Date019  */  
   "Date019":string,
      /**  Date020  */  
   "Date020":string,
      /**  Date021  */  
   "Date021":string,
      /**  Date022  */  
   "Date022":string,
      /**  Date023  */  
   "Date023":string,
      /**  Date024  */  
   "Date024":string,
      /**  Date025  */  
   "Date025":string,
      /**  Date026  */  
   "Date026":string,
      /**  Date027  */  
   "Date027":string,
      /**  Date028  */  
   "Date028":string,
      /**  Date029  */  
   "Date029":string,
      /**  Date030  */  
   "Date030":string,
      /**  Date031  */  
   "Date031":string,
      /**  Date032  */  
   "Date032":string,
      /**  Date033  */  
   "Date033":string,
      /**  Date034  */  
   "Date034":string,
      /**  Date035  */  
   "Date035":string,
      /**  Date036  */  
   "Date036":string,
      /**  Date037  */  
   "Date037":string,
      /**  Date038  */  
   "Date038":string,
      /**  Date039  */  
   "Date039":string,
      /**  Date040  */  
   "Date040":string,
      /**  Date041  */  
   "Date041":string,
      /**  Date042  */  
   "Date042":string,
      /**  Date043  */  
   "Date043":string,
      /**  Date044  */  
   "Date044":string,
      /**  Date045  */  
   "Date045":string,
      /**  Date046  */  
   "Date046":string,
      /**  Date047  */  
   "Date047":string,
      /**  Date051  */  
   "Date051":string,
      /**  Date052  */  
   "Date052":string,
      /**  Date053  */  
   "Date053":string,
      /**  Date054  */  
   "Date054":string,
      /**  Date055  */  
   "Date055":string,
      /**  Date056  */  
   "Date056":string,
      /**  Date057  */  
   "Date057":string,
      /**  Date058  */  
   "Date058":string,
      /**  Date059  */  
   "Date059":string,
      /**  Date060  */  
   "Date060":string,
      /**  Date061  */  
   "Date061":string,
      /**  Date062  */  
   "Date062":string,
      /**  Date063  */  
   "Date063":string,
      /**  Date064  */  
   "Date064":string,
      /**  Date065  */  
   "Date065":string,
      /**  Date066  */  
   "Date066":string,
      /**  Date067  */  
   "Date067":string,
      /**  Date068  */  
   "Date068":string,
      /**  Date069  */  
   "Date069":string,
      /**  Date070  */  
   "Date070":string,
      /**  Date071  */  
   "Date071":string,
      /**  Date072  */  
   "Date072":string,
      /**  Date073  */  
   "Date073":string,
      /**  Date074  */  
   "Date074":string,
      /**  Date075  */  
   "Date075":string,
      /**  Date076  */  
   "Date076":string,
      /**  Date077  */  
   "Date077":string,
      /**  Date078  */  
   "Date078":string,
      /**  Date079  */  
   "Date079":string,
      /**  Date080  */  
   "Date080":string,
      /**  Date081  */  
   "Date081":string,
      /**  Date082  */  
   "Date082":string,
      /**  Date083  */  
   "Date083":string,
      /**  Date084  */  
   "Date084":string,
      /**  Date085  */  
   "Date085":string,
      /**  Date086  */  
   "Date086":string,
      /**  Date087  */  
   "Date087":string,
      /**  Date088  */  
   "Date088":string,
      /**  Date089  */  
   "Date089":string,
      /**  Date090  */  
   "Date090":string,
      /**  Date091  */  
   "Date091":string,
      /**  Date092  */  
   "Date092":string,
      /**  Date093  */  
   "Date093":string,
      /**  Date094  */  
   "Date094":string,
      /**  Date095  */  
   "Date095":string,
      /**  Date096  */  
   "Date096":string,
      /**  Date097  */  
   "Date097":string,
      /**  Date101  */  
   "Date101":string,
      /**  Date102  */  
   "Date102":string,
      /**  Date103  */  
   "Date103":string,
      /**  Date104  */  
   "Date104":string,
      /**  Date105  */  
   "Date105":string,
      /**  Date106  */  
   "Date106":string,
      /**  Date107  */  
   "Date107":string,
      /**  Date108  */  
   "Date108":string,
      /**  Date109  */  
   "Date109":string,
      /**  Date110  */  
   "Date110":string,
      /**  Date111  */  
   "Date111":string,
      /**  Date112  */  
   "Date112":string,
      /**  Date113  */  
   "Date113":string,
      /**  Date114  */  
   "Date114":string,
      /**  Date115  */  
   "Date115":string,
      /**  Date116  */  
   "Date116":string,
      /**  Date117  */  
   "Date117":string,
      /**  Date118  */  
   "Date118":string,
      /**  Date119  */  
   "Date119":string,
      /**  Date120  */  
   "Date120":string,
      /**  Date121  */  
   "Date121":string,
      /**  Date122  */  
   "Date122":string,
      /**  Date123  */  
   "Date123":string,
      /**  Date124  */  
   "Date124":string,
      /**  Date125  */  
   "Date125":string,
      /**  Date126  */  
   "Date126":string,
      /**  Date127  */  
   "Date127":string,
      /**  Date128  */  
   "Date128":string,
      /**  Date129  */  
   "Date129":string,
      /**  Date130  */  
   "Date130":string,
      /**  Date131  */  
   "Date131":string,
      /**  Date132  */  
   "Date132":string,
      /**  Date133  */  
   "Date133":string,
      /**  Date134  */  
   "Date134":string,
      /**  Date135  */  
   "Date135":string,
      /**  Date136  */  
   "Date136":string,
      /**  Date137  */  
   "Date137":string,
      /**  Date138  */  
   "Date138":string,
      /**  Date139  */  
   "Date139":string,
      /**  Date140  */  
   "Date140":string,
      /**  Date141  */  
   "Date141":string,
      /**  Date142  */  
   "Date142":string,
      /**  Date143  */  
   "Date143":string,
      /**  Date144  */  
   "Date144":string,
      /**  Date145  */  
   "Date145":string,
      /**  Date146  */  
   "Date146":string,
      /**  Date147  */  
   "Date147":string,
      /**  Date151  */  
   "Date151":string,
      /**  Date152  */  
   "Date152":string,
      /**  Date153  */  
   "Date153":string,
      /**  Date154  */  
   "Date154":string,
      /**  Date155  */  
   "Date155":string,
      /**  Date156  */  
   "Date156":string,
      /**  Date157  */  
   "Date157":string,
      /**  Date158  */  
   "Date158":string,
      /**  Date159  */  
   "Date159":string,
      /**  Date160  */  
   "Date160":string,
      /**  Date161  */  
   "Date161":string,
      /**  Date162  */  
   "Date162":string,
      /**  Date163  */  
   "Date163":string,
      /**  Date164  */  
   "Date164":string,
      /**  Date165  */  
   "Date165":string,
      /**  Date166  */  
   "Date166":string,
      /**  Date167  */  
   "Date167":string,
      /**  Date168  */  
   "Date168":string,
      /**  Date169  */  
   "Date169":string,
      /**  Date170  */  
   "Date170":string,
      /**  Date171  */  
   "Date171":string,
      /**  Date172  */  
   "Date172":string,
      /**  Date173  */  
   "Date173":string,
      /**  Date174  */  
   "Date174":string,
      /**  Date175  */  
   "Date175":string,
      /**  Date176  */  
   "Date176":string,
      /**  Date177  */  
   "Date177":string,
      /**  Date178  */  
   "Date178":string,
      /**  Date179  */  
   "Date179":string,
      /**  Date180  */  
   "Date180":string,
      /**  Date181  */  
   "Date181":string,
      /**  Date182  */  
   "Date182":string,
      /**  Date183  */  
   "Date183":string,
      /**  Date184  */  
   "Date184":string,
      /**  Date185  */  
   "Date185":string,
      /**  Date186  */  
   "Date186":string,
      /**  Date187  */  
   "Date187":string,
      /**  Date188  */  
   "Date188":string,
      /**  Date189  */  
   "Date189":string,
      /**  Date190  */  
   "Date190":string,
      /**  Date191  */  
   "Date191":string,
      /**  Date192  */  
   "Date192":string,
      /**  Date193  */  
   "Date193":string,
      /**  Date194  */  
   "Date194":string,
      /**  Date195  */  
   "Date195":string,
      /**  Date196  */  
   "Date196":string,
      /**  Date197  */  
   "Date197":string,
      /**  Date048  */  
   "Date048":string,
      /**  Date049  */  
   "Date049":string,
      /**  Date050  */  
   "Date050":string,
      /**  Date098  */  
   "Date098":string,
      /**  Date099  */  
   "Date099":string,
      /**  Date100  */  
   "Date100":string,
      /**  Date148  */  
   "Date148":string,
      /**  Date149  */  
   "Date149":string,
      /**  Date150  */  
   "Date150":string,
      /**  Date198  */  
   "Date198":string,
      /**  Date199  */  
   "Date199":string,
      /**  Date200  */  
   "Date200":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_InspResultsListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Inspection Plan Type.  Valid plan type values - I (Inspection Plan),  C (Calibration Plan).  */  
   "InspPlanType":string,
      /**  The name of the table that this record pertains to. Field not currently used.  */  
   "File":string,
      /**  Major component of the primary key to the record. Depending on the context in which the inspection was done: for RMA, it would be the RMANum; for Receipts it would be the PackSlip; for FirstArt it would be the JobNum; for Materials, it would be the LaborHedSeq; for Inventory it would be the NCMTranID; JobNum or PartNum when no more information.  */  
   "Key1":string,
      /**  2nd component of the primary key to the related record. The usage of this field is dependent on the type of record.  For example:  for a RMA, it would be the RMALine; for a Receipt it would be the PackLine; for FirstArt it would be the AssemblySeq; for Materials, it would be the LaborDtlSeq; in other cases would be the AssemblySeq or the RevisionNum of a PartNum.  */  
   "Key2":string,
      /**  3rd component of the primary key to the related record. The usage of this field is dependent on the type of record referenced. The usage of this field is dependent on the type of record referenced. For example: for a RMA, it would be the RMAReceipt; for a Receipt it would be the VendorNum; for FirstArt it would be the OprSeq; in other cases it would be the OprSeq.  */  
   "Key3":string,
      /**  4th component of the primary key to the related record.  For Example: for a RMA it would be the RMADisp.  */  
   "Key4":string,
      /**  5th component of the primary key to the related record. For future use.  */  
   "Key5":string,
      /**  A sequential number up to the total in the Inspection Quantity field.  */  
   "SampleNumber":number,
      /**  Date the inspection data was saved  */  
   "InspectDate":string,
      /**  System time (seconds since midnight) of when the inspection data was saved  */  
   "InspectTime":number,
      /**  Site Identifier. This field cannot be blank.  */  
   "Plant":string,
      /**  Part number inspected  */  
   "PartNum":string,
      /**  Revision Number Inspected  */  
   "RevisionNum":string,
      /**  Contains the Job Number related to the job or non-conformance being inspected.  */  
   "JobNum":string,
      /**  Contain the assembly sequence of the job being inspected  */  
   "AssemblySeq":number,
      /**  Contains the operation sequence of the job operation being inspected.  */  
   "OprSeq":number,
      /**  Contains the Non-Conformance (NonConf) TranID if inspecting Non-Conformance  */  
   "NCMTranID":number,
      /**  Contains the inspection plan part number (configurator part number)  */  
   "InspPlanPartNum":string,
      /**  Contains the inspection plan revision number (configurator revision number)  */  
   "InspPlanRevNum":string,
      /**  Contains the specification ID that was used in the inspection plan.  */  
   "SpecID":string,
      /**  Contains the specification revision number that was used in the inspection process.  */  
   "SpecRevNum":string,
      /**  Contains Return Material Authorization number if inspecting for an RMA  */  
   "RMANum":number,
      /**  Contains Line number of the RMA if inspecting for an RMA.  */  
   "RMALine":number,
      /**  Contain the ResourceGrpID when inspected via Fixed Asset Calibration or Preventative Maintenance Calibration  */  
   "ResourceGrpID":string,
      /**  Contain the ResourceID when inspected via Fixed Asset Calibration or Preventative Maintenance Calibration  */  
   "ResourceID":string,
      /**  Contains the PO Packing Slip number.  */  
   "PackSlip":string,
      /**  Contains the PO Packing Slip line number.  */  
   "PackLine":number,
      /**  Contains the VendorNum when inspected via Skip Lot processing  */  
   "VendorNum":number,
      /**  Contains the serial number of the part inspected  */  
   "SerialNum":string,
      /**  Contains the lot number of the part inspected  */  
   "LotNum":string,
      /**  True if passed  */  
   "Passed":boolean,
      /**  Text describing why the inspection result failed  */  
   "FailedCmtText":string,
      /**  True if the results were saved in product configuration  */  
   "TestDataEntered":boolean,
      /**  This is a unique reference number that is assigned by the system for each audit record.  */  
   "AuditRefNum":number,
      /**  Purchase point from Vendor.  */  
   "PurPoint":string,
      /**  Shows how the audit was created - Scheduled or Manual  */  
   "AuditType":string,
      /**  User defined Audit ID  */  
   "AuditID":string,
      /**  Supplier Audit Revision Number  */  
   "AuditRevNum":string,
      /**  Auditor.  Valid auditor values - E (Employee),  R (Role), S (Supplier)  */  
   "Auditor":string,
   "AuditSchedDate":string,
      /**  Date the audit reference was created  */  
   "AuditCreateDate":string,
      /**  Employee ID.  If an employee code is entered, it must be valid in the EmpBasic table.  */  
   "EmpID":string,
      /**  Auditor Supplier Number.  If a supplier number is entered, it must be valid in the Vendor table.  */  
   "AuditVendNum":number,
      /**  Date the audit was completed  */  
   "AuditCompDate":string,
      /**  Planned, Scheduled, In Progress, Complete  */  
   "AuditStatus":string,
      /**  Passed, Failed, Unspecified  */  
   "AuditResult":string,
      /**  Supplier Contact number.  If entered, it must be valid in the VendCnt record.  */  
   "AuditConNum":number,
      /**  Code that identifies the role of the audit contact.  */  
   "AuditConRole":string,
      /**  This is the cost of performing the audit.  */  
   "AuditCost":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "Description":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_InspResultsNumAttchRow{
   "Company":string,
   "InspPlanType":string,
   "File":string,
   "Key1":string,
   "Key2":string,
   "Key3":string,
   "Key4":string,
   "Key5":string,
   "SampleNumber":number,
   "InspectDate":string,
   "InspectTime":number,
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

export interface Erp_Tablesets_InspResultsNumRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Inspection Plan Type - Inspection, Audit, or Survey  */  
   "InspPlanType":string,
      /**  The name of the table that this record pertains to.  */  
   "File":string,
      /**  Major component of the primary key to the record.  */  
   "Key1":string,
      /**   2nd component of the primary key to the related record.
For example: For a "OrderDtl"   this field would contain the OrderLine # of the related Order detail record.  The usage of this field is dependant on the type of record.  For example "Part" references do not use this field while PartRev  would.  */  
   "Key2":string,
      /**   3rd component of the primary key to the related record.
For example: For a "OrderRel"   this field would contain the Order Line Release # of the related Order Release record.  The usage of this field is dependant on the type of record referenced.  */  
   "Key3":string,
      /**  4th component of the primary key to the related record.  */  
   "Key4":string,
      /**  5th component of the primary key to the related record.  */  
   "Key5":string,
      /**  A sequential number up to the total in the Inspection Quantity field.  */  
   "SampleNumber":number,
      /**  Date the inspection data was saved  */  
   "InspectDate":string,
      /**  System time (seconds since midnight) of when the inspection data was saved  */  
   "InspectTime":number,
      /**  Number001  */  
   "Number001":number,
      /**  Number002  */  
   "Number002":number,
      /**  Number003  */  
   "Number003":number,
      /**  Number004  */  
   "Number004":number,
      /**  Number005  */  
   "Number005":number,
      /**  Number006  */  
   "Number006":number,
      /**  Number007  */  
   "Number007":number,
      /**  Number008  */  
   "Number008":number,
      /**  Number009  */  
   "Number009":number,
      /**  Number010  */  
   "Number010":number,
      /**  Number011  */  
   "Number011":number,
      /**  Number012  */  
   "Number012":number,
      /**  Number013  */  
   "Number013":number,
      /**  Number014  */  
   "Number014":number,
      /**  Number015  */  
   "Number015":number,
      /**  Number016  */  
   "Number016":number,
      /**  Number017  */  
   "Number017":number,
      /**  Number018  */  
   "Number018":number,
      /**  Number019  */  
   "Number019":number,
      /**  Number020  */  
   "Number020":number,
      /**  Number021  */  
   "Number021":number,
      /**  Number022  */  
   "Number022":number,
      /**  Number023  */  
   "Number023":number,
      /**  Number024  */  
   "Number024":number,
      /**  Number025  */  
   "Number025":number,
      /**  Number026  */  
   "Number026":number,
      /**  Number027  */  
   "Number027":number,
      /**  Number028  */  
   "Number028":number,
      /**  Number029  */  
   "Number029":number,
      /**  Number030  */  
   "Number030":number,
      /**  Number031  */  
   "Number031":number,
      /**  Number032  */  
   "Number032":number,
      /**  Number033  */  
   "Number033":number,
      /**  Number034  */  
   "Number034":number,
      /**  Number035  */  
   "Number035":number,
      /**  Number036  */  
   "Number036":number,
      /**  Number037  */  
   "Number037":number,
      /**  Number038  */  
   "Number038":number,
      /**  Number039  */  
   "Number039":number,
      /**  Number040  */  
   "Number040":number,
      /**  Number041  */  
   "Number041":number,
      /**  Number042  */  
   "Number042":number,
      /**  Number043  */  
   "Number043":number,
      /**  Number044  */  
   "Number044":number,
      /**  Number045  */  
   "Number045":number,
      /**  Number046  */  
   "Number046":number,
      /**  Number047  */  
   "Number047":number,
      /**  Number048  */  
   "Number048":number,
      /**  Number049  */  
   "Number049":number,
      /**  Number050  */  
   "Number050":number,
      /**  Number051  */  
   "Number051":number,
      /**  Number052  */  
   "Number052":number,
      /**  Number053  */  
   "Number053":number,
      /**  Number054  */  
   "Number054":number,
      /**  Number055  */  
   "Number055":number,
      /**  Number056  */  
   "Number056":number,
      /**  Number057  */  
   "Number057":number,
      /**  Number058  */  
   "Number058":number,
      /**  Number059  */  
   "Number059":number,
      /**  Number060  */  
   "Number060":number,
      /**  Number061  */  
   "Number061":number,
      /**  Number062  */  
   "Number062":number,
      /**  Number063  */  
   "Number063":number,
      /**  Number064  */  
   "Number064":number,
      /**  Number065  */  
   "Number065":number,
      /**  Number066  */  
   "Number066":number,
      /**  Number067  */  
   "Number067":number,
      /**  Number068  */  
   "Number068":number,
      /**  Number069  */  
   "Number069":number,
      /**  Number070  */  
   "Number070":number,
      /**  Number071  */  
   "Number071":number,
      /**  Number072  */  
   "Number072":number,
      /**  Number073  */  
   "Number073":number,
      /**  Number074  */  
   "Number074":number,
      /**  Number075  */  
   "Number075":number,
      /**  Number076  */  
   "Number076":number,
      /**  Number077  */  
   "Number077":number,
      /**  Number078  */  
   "Number078":number,
      /**  Number079  */  
   "Number079":number,
      /**  Number080  */  
   "Number080":number,
      /**  Number081  */  
   "Number081":number,
      /**  Number082  */  
   "Number082":number,
      /**  Number083  */  
   "Number083":number,
      /**  Number084  */  
   "Number084":number,
      /**  Number085  */  
   "Number085":number,
      /**  Number086  */  
   "Number086":number,
      /**  Number087  */  
   "Number087":number,
      /**  Number088  */  
   "Number088":number,
      /**  Number089  */  
   "Number089":number,
      /**  Number090  */  
   "Number090":number,
      /**  Number091  */  
   "Number091":number,
      /**  Number092  */  
   "Number092":number,
      /**  Number093  */  
   "Number093":number,
      /**  Number094  */  
   "Number094":number,
      /**  Number095  */  
   "Number095":number,
      /**  Number096  */  
   "Number096":number,
      /**  Number097  */  
   "Number097":number,
      /**  Number098  */  
   "Number098":number,
      /**  Number099  */  
   "Number099":number,
      /**  Number100  */  
   "Number100":number,
      /**  Number101  */  
   "Number101":number,
      /**  Number102  */  
   "Number102":number,
      /**  Number103  */  
   "Number103":number,
      /**  Number104  */  
   "Number104":number,
      /**  Number105  */  
   "Number105":number,
      /**  Number106  */  
   "Number106":number,
      /**  Number107  */  
   "Number107":number,
      /**  Number108  */  
   "Number108":number,
      /**  Number109  */  
   "Number109":number,
      /**  Number110  */  
   "Number110":number,
      /**  Number111  */  
   "Number111":number,
      /**  Number112  */  
   "Number112":number,
      /**  Number113  */  
   "Number113":number,
      /**  Number114  */  
   "Number114":number,
      /**  Number115  */  
   "Number115":number,
      /**  Number116  */  
   "Number116":number,
      /**  Number117  */  
   "Number117":number,
      /**  Number118  */  
   "Number118":number,
      /**  Number119  */  
   "Number119":number,
      /**  Number120  */  
   "Number120":number,
      /**  Number121  */  
   "Number121":number,
      /**  Number122  */  
   "Number122":number,
      /**  Number123  */  
   "Number123":number,
      /**  Number124  */  
   "Number124":number,
      /**  Number125  */  
   "Number125":number,
      /**  Number126  */  
   "Number126":number,
      /**  Number127  */  
   "Number127":number,
      /**  Number128  */  
   "Number128":number,
      /**  Number129  */  
   "Number129":number,
      /**  Number130  */  
   "Number130":number,
      /**  Number131  */  
   "Number131":number,
      /**  Number132  */  
   "Number132":number,
      /**  Number133  */  
   "Number133":number,
      /**  Number134  */  
   "Number134":number,
      /**  Number135  */  
   "Number135":number,
      /**  Number136  */  
   "Number136":number,
      /**  Number137  */  
   "Number137":number,
      /**  Number138  */  
   "Number138":number,
      /**  Number139  */  
   "Number139":number,
      /**  Number140  */  
   "Number140":number,
      /**  Number141  */  
   "Number141":number,
      /**  Number142  */  
   "Number142":number,
      /**  Number143  */  
   "Number143":number,
      /**  Number144  */  
   "Number144":number,
      /**  Number145  */  
   "Number145":number,
      /**  Number146  */  
   "Number146":number,
      /**  Number147  */  
   "Number147":number,
      /**  Number148  */  
   "Number148":number,
      /**  Number149  */  
   "Number149":number,
      /**  Number150  */  
   "Number150":number,
      /**  Number151  */  
   "Number151":number,
      /**  Number152  */  
   "Number152":number,
      /**  Number153  */  
   "Number153":number,
      /**  Number154  */  
   "Number154":number,
      /**  Number155  */  
   "Number155":number,
      /**  Number156  */  
   "Number156":number,
      /**  Number157  */  
   "Number157":number,
      /**  Number158  */  
   "Number158":number,
      /**  Number159  */  
   "Number159":number,
      /**  Number160  */  
   "Number160":number,
      /**  Number161  */  
   "Number161":number,
      /**  Number162  */  
   "Number162":number,
      /**  Number163  */  
   "Number163":number,
      /**  Number164  */  
   "Number164":number,
      /**  Number165  */  
   "Number165":number,
      /**  Number166  */  
   "Number166":number,
      /**  Number167  */  
   "Number167":number,
      /**  Number168  */  
   "Number168":number,
      /**  Number169  */  
   "Number169":number,
      /**  Number170  */  
   "Number170":number,
      /**  Number171  */  
   "Number171":number,
      /**  Number172  */  
   "Number172":number,
      /**  Number173  */  
   "Number173":number,
      /**  Number174  */  
   "Number174":number,
      /**  Number175  */  
   "Number175":number,
      /**  Number176  */  
   "Number176":number,
      /**  Number177  */  
   "Number177":number,
      /**  Number178  */  
   "Number178":number,
      /**  Number179  */  
   "Number179":number,
      /**  Number180  */  
   "Number180":number,
      /**  Number181  */  
   "Number181":number,
      /**  Number182  */  
   "Number182":number,
      /**  Number183  */  
   "Number183":number,
      /**  Number184  */  
   "Number184":number,
      /**  Number185  */  
   "Number185":number,
      /**  Number186  */  
   "Number186":number,
      /**  Number187  */  
   "Number187":number,
      /**  Number188  */  
   "Number188":number,
      /**  Number189  */  
   "Number189":number,
      /**  Number190  */  
   "Number190":number,
      /**  Number191  */  
   "Number191":number,
      /**  Number192  */  
   "Number192":number,
      /**  Number193  */  
   "Number193":number,
      /**  Number194  */  
   "Number194":number,
      /**  Number195  */  
   "Number195":number,
      /**  Number196  */  
   "Number196":number,
      /**  Number197  */  
   "Number197":number,
      /**  Number198  */  
   "Number198":number,
      /**  Number199  */  
   "Number199":number,
      /**  Number200  */  
   "Number200":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_InspResultsRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Inspection Plan Type.  Valid plan type values - I (Inspection Plan),  C (Calibration Plan).  */  
   "InspPlanType":string,
      /**  The name of the table that this record pertains to. Field not currently used.  */  
   "File":string,
      /**  Major component of the primary key to the record. Depending on the context in which the inspection was done: for RMA, it would be the RMANum; for Receipts it would be the PackSlip; for FirstArt it would be the JobNum; for Materials, it would be the LaborHedSeq; for Inventory it would be the NCMTranID; JobNum or PartNum when no more information.  */  
   "Key1":string,
      /**  2nd component of the primary key to the related record. The usage of this field is dependent on the type of record.  For example:  for a RMA, it would be the RMALine; for a Receipt it would be the PackLine; for FirstArt it would be the AssemblySeq; for Materials, it would be the LaborDtlSeq; in other cases would be the AssemblySeq or the RevisionNum of a PartNum.  */  
   "Key2":string,
      /**  3rd component of the primary key to the related record. The usage of this field is dependent on the type of record referenced. The usage of this field is dependent on the type of record referenced. For example: for a RMA, it would be the RMAReceipt; for a Receipt it would be the VendorNum; for FirstArt it would be the OprSeq; in other cases it would be the OprSeq.  */  
   "Key3":string,
      /**  4th component of the primary key to the related record.  For Example: for a RMA it would be the RMADisp.  */  
   "Key4":string,
      /**  5th component of the primary key to the related record. For future use.  */  
   "Key5":string,
      /**  A sequential number up to the total in the Inspection Quantity field.  */  
   "SampleNumber":number,
      /**  Date the inspection data was saved  */  
   "InspectDate":string,
      /**  System time (seconds since midnight) of when the inspection data was saved  */  
   "InspectTime":number,
      /**  Site Identifier. This field cannot be blank.  */  
   "Plant":string,
      /**  Part number inspected  */  
   "PartNum":string,
      /**  Revision Number Inspected  */  
   "RevisionNum":string,
      /**  Contains the Job Number related to the job or non-conformance being inspected.  */  
   "JobNum":string,
      /**  Contain the assembly sequence of the job being inspected  */  
   "AssemblySeq":number,
      /**  Contains the operation sequence of the job operation being inspected.  */  
   "OprSeq":number,
      /**  Contains the Non-Conformance (NonConf) TranID if inspecting Non-Conformance  */  
   "NCMTranID":number,
      /**  Contains the inspection plan part number (configurator part number)  */  
   "InspPlanPartNum":string,
      /**  Contains the inspection plan revision number (configurator revision number)  */  
   "InspPlanRevNum":string,
      /**  Contains the specification ID that was used in the inspection plan.  */  
   "SpecID":string,
      /**  Contains the specification revision number that was used in the inspection process.  */  
   "SpecRevNum":string,
      /**  Contains Return Material Authorization number if inspecting for an RMA  */  
   "RMANum":number,
      /**  Contains Line number of the RMA if inspecting for an RMA.  */  
   "RMALine":number,
      /**  Contain the ResourceGrpID when inspected via Fixed Asset Calibration or Preventative Maintenance Calibration  */  
   "ResourceGrpID":string,
      /**  Contain the ResourceID when inspected via Fixed Asset Calibration or Preventative Maintenance Calibration  */  
   "ResourceID":string,
      /**  Contains the PO Packing Slip number.  */  
   "PackSlip":string,
      /**  Contains the PO Packing Slip line number.  */  
   "PackLine":number,
      /**  Contains the VendorNum when inspected via Skip Lot processing  */  
   "VendorNum":number,
      /**  Contains the serial number of the part inspected  */  
   "SerialNum":string,
      /**  Contains the lot number of the part inspected  */  
   "LotNum":string,
      /**  True if passed  */  
   "Passed":boolean,
      /**  Text describing why the inspection result failed  */  
   "FailedCmtText":string,
      /**  True if the results were saved in product configuration  */  
   "TestDataEntered":boolean,
      /**  This is a unique reference number that is assigned by the system for each audit record.  */  
   "AuditRefNum":number,
      /**  Purchase point from Vendor.  */  
   "PurPoint":string,
      /**  Shows how the audit was created - Scheduled or Manual  */  
   "AuditType":string,
      /**  User defined Audit ID  */  
   "AuditID":string,
      /**  Supplier Audit Revision Number  */  
   "AuditRevNum":string,
      /**  Auditor.  Valid auditor values - E (Employee),  R (Role), S (Supplier)  */  
   "Auditor":string,
   "AuditSchedDate":string,
      /**  Date the audit reference was created  */  
   "AuditCreateDate":string,
      /**  Employee ID.  If an employee code is entered, it must be valid in the EmpBasic table.  */  
   "EmpID":string,
      /**  Auditor Supplier Number.  If a supplier number is entered, it must be valid in the Vendor table.  */  
   "AuditVendNum":number,
      /**  Date the audit was completed  */  
   "AuditCompDate":string,
      /**  Planned, Scheduled, In Progress, Complete  */  
   "AuditStatus":string,
      /**  Passed, Failed, Unspecified  */  
   "AuditResult":string,
      /**  Supplier Contact number.  If entered, it must be valid in the VendCnt record.  */  
   "AuditConNum":number,
      /**  Code that identifies the role of the audit contact.  */  
   "AuditConRole":string,
      /**  This is the cost of performing the audit.  */  
   "AuditCost":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
   "Description":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_InspResultsShortCharAttchRow{
   "Company":string,
   "InspPlanType":string,
   "File":string,
   "Key1":string,
   "Key2":string,
   "Key3":string,
   "Key4":string,
   "Key5":string,
   "SampleNumber":number,
   "InspectDate":string,
   "InspectTime":number,
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

export interface Erp_Tablesets_InspResultsShortCharRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Inspection Plan Type - Inspection, Audit, or Survey  */  
   "InspPlanType":string,
      /**  The name of the table that this record pertains to.  */  
   "File":string,
      /**  Major component of the primary key to the record.  */  
   "Key1":string,
      /**   2nd component of the primary key to the related record.
For example: For a "OrderDtl"   this field would contain the OrderLine # of the related Order detail record.  The usage of this field is dependant on the type of record.  For example "Part" references do not use this field while PartRev  would.  */  
   "Key2":string,
      /**   3rd component of the primary key to the related record.
For example: For a "OrderRel"   this field would contain the Order Line Release # of the related Order Release record.  The usage of this field is dependant on the type of record referenced.  */  
   "Key3":string,
      /**  4th component of the primary key to the related record.  */  
   "Key4":string,
      /**  5th component of the primary key to the related record.  */  
   "Key5":string,
      /**  A sequential number up to the total in the Inspection Quantity field.  */  
   "SampleNumber":number,
      /**  Date the inspection data was saved  */  
   "InspectDate":string,
      /**  System time (seconds since midnight) of when the inspection data was saved  */  
   "InspectTime":number,
      /**  ShortChar001  */  
   "ShortChar001":string,
      /**  ShortChar002  */  
   "ShortChar002":string,
      /**  ShortChar003  */  
   "ShortChar003":string,
      /**  ShortChar004  */  
   "ShortChar004":string,
      /**  ShortChar005  */  
   "ShortChar005":string,
      /**  ShortChar006  */  
   "ShortChar006":string,
      /**  ShortChar007  */  
   "ShortChar007":string,
      /**  ShortChar008  */  
   "ShortChar008":string,
      /**  ShortChar009  */  
   "ShortChar009":string,
      /**  ShortChar010  */  
   "ShortChar010":string,
      /**  ShortChar011  */  
   "ShortChar011":string,
      /**  ShortChar012  */  
   "ShortChar012":string,
      /**  ShortChar013  */  
   "ShortChar013":string,
      /**  ShortChar014  */  
   "ShortChar014":string,
      /**  ShortChar015  */  
   "ShortChar015":string,
      /**  ShortChar016  */  
   "ShortChar016":string,
      /**  ShortChar017  */  
   "ShortChar017":string,
      /**  ShortChar018  */  
   "ShortChar018":string,
      /**  ShortChar019  */  
   "ShortChar019":string,
      /**  ShortChar020  */  
   "ShortChar020":string,
      /**  ShortChar021  */  
   "ShortChar021":string,
      /**  ShortChar022  */  
   "ShortChar022":string,
      /**  ShortChar023  */  
   "ShortChar023":string,
      /**  ShortChar024  */  
   "ShortChar024":string,
      /**  ShortChar025  */  
   "ShortChar025":string,
      /**  ShortChar026  */  
   "ShortChar026":string,
      /**  ShortChar027  */  
   "ShortChar027":string,
      /**  ShortChar028  */  
   "ShortChar028":string,
      /**  ShortChar029  */  
   "ShortChar029":string,
      /**  ShortChar030  */  
   "ShortChar030":string,
      /**  ShortChar031  */  
   "ShortChar031":string,
      /**  ShortChar032  */  
   "ShortChar032":string,
      /**  ShortChar033  */  
   "ShortChar033":string,
      /**  ShortChar034  */  
   "ShortChar034":string,
      /**  ShortChar035  */  
   "ShortChar035":string,
      /**  ShortChar036  */  
   "ShortChar036":string,
      /**  ShortChar037  */  
   "ShortChar037":string,
      /**  ShortChar038  */  
   "ShortChar038":string,
      /**  ShortChar039  */  
   "ShortChar039":string,
      /**  ShortChar040  */  
   "ShortChar040":string,
      /**  ShortChar041  */  
   "ShortChar041":string,
      /**  ShortChar042  */  
   "ShortChar042":string,
      /**  ShortChar043  */  
   "ShortChar043":string,
      /**  ShortChar044  */  
   "ShortChar044":string,
      /**  ShortChar045  */  
   "ShortChar045":string,
      /**  ShortChar046  */  
   "ShortChar046":string,
      /**  ShortChar047  */  
   "ShortChar047":string,
      /**  ShortChar048  */  
   "ShortChar048":string,
      /**  ShortChar049  */  
   "ShortChar049":string,
      /**  ShortChar050  */  
   "ShortChar050":string,
      /**  ShortChar051  */  
   "ShortChar051":string,
      /**  ShortChar052  */  
   "ShortChar052":string,
      /**  ShortChar053  */  
   "ShortChar053":string,
      /**  ShortChar054  */  
   "ShortChar054":string,
      /**  ShortChar055  */  
   "ShortChar055":string,
      /**  ShortChar056  */  
   "ShortChar056":string,
      /**  ShortChar057  */  
   "ShortChar057":string,
      /**  ShortChar058  */  
   "ShortChar058":string,
      /**  ShortChar059  */  
   "ShortChar059":string,
      /**  ShortChar060  */  
   "ShortChar060":string,
      /**  ShortChar061  */  
   "ShortChar061":string,
      /**  ShortChar062  */  
   "ShortChar062":string,
      /**  ShortChar063  */  
   "ShortChar063":string,
      /**  ShortChar064  */  
   "ShortChar064":string,
      /**  ShortChar065  */  
   "ShortChar065":string,
      /**  ShortChar066  */  
   "ShortChar066":string,
      /**  ShortChar067  */  
   "ShortChar067":string,
      /**  ShortChar068  */  
   "ShortChar068":string,
      /**  ShortChar069  */  
   "ShortChar069":string,
      /**  ShortChar070  */  
   "ShortChar070":string,
      /**  ShortChar071  */  
   "ShortChar071":string,
      /**  ShortChar072  */  
   "ShortChar072":string,
      /**  ShortChar073  */  
   "ShortChar073":string,
      /**  ShortChar074  */  
   "ShortChar074":string,
      /**  ShortChar075  */  
   "ShortChar075":string,
      /**  ShortChar076  */  
   "ShortChar076":string,
      /**  ShortChar077  */  
   "ShortChar077":string,
      /**  ShortChar078  */  
   "ShortChar078":string,
      /**  ShortChar079  */  
   "ShortChar079":string,
      /**  ShortChar080  */  
   "ShortChar080":string,
      /**  ShortChar081  */  
   "ShortChar081":string,
      /**  ShortChar082  */  
   "ShortChar082":string,
      /**  ShortChar083  */  
   "ShortChar083":string,
      /**  ShortChar084  */  
   "ShortChar084":string,
      /**  ShortChar085  */  
   "ShortChar085":string,
      /**  ShortChar086  */  
   "ShortChar086":string,
      /**  ShortChar087  */  
   "ShortChar087":string,
      /**  ShortChar088  */  
   "ShortChar088":string,
      /**  ShortChar089  */  
   "ShortChar089":string,
      /**  ShortChar090  */  
   "ShortChar090":string,
      /**  ShortChar091  */  
   "ShortChar091":string,
      /**  ShortChar092  */  
   "ShortChar092":string,
      /**  ShortChar093  */  
   "ShortChar093":string,
      /**  ShortChar094  */  
   "ShortChar094":string,
      /**  ShortChar095  */  
   "ShortChar095":string,
      /**  ShortChar096  */  
   "ShortChar096":string,
      /**  ShortChar097  */  
   "ShortChar097":string,
      /**  ShortChar098  */  
   "ShortChar098":string,
      /**  ShortChar099  */  
   "ShortChar099":string,
      /**  ShortChar100  */  
   "ShortChar100":string,
      /**  ShortChar101  */  
   "ShortChar101":string,
      /**  ShortChar102  */  
   "ShortChar102":string,
      /**  ShortChar103  */  
   "ShortChar103":string,
      /**  ShortChar104  */  
   "ShortChar104":string,
      /**  ShortChar105  */  
   "ShortChar105":string,
      /**  ShortChar106  */  
   "ShortChar106":string,
      /**  ShortChar107  */  
   "ShortChar107":string,
      /**  ShortChar108  */  
   "ShortChar108":string,
      /**  ShortChar109  */  
   "ShortChar109":string,
      /**  ShortChar110  */  
   "ShortChar110":string,
      /**  ShortChar111  */  
   "ShortChar111":string,
      /**  ShortChar112  */  
   "ShortChar112":string,
      /**  ShortChar113  */  
   "ShortChar113":string,
      /**  ShortChar114  */  
   "ShortChar114":string,
      /**  ShortChar115  */  
   "ShortChar115":string,
      /**  ShortChar116  */  
   "ShortChar116":string,
      /**  ShortChar117  */  
   "ShortChar117":string,
      /**  ShortChar118  */  
   "ShortChar118":string,
      /**  ShortChar119  */  
   "ShortChar119":string,
      /**  ShortChar120  */  
   "ShortChar120":string,
      /**  ShortChar121  */  
   "ShortChar121":string,
      /**  ShortChar122  */  
   "ShortChar122":string,
      /**  ShortChar123  */  
   "ShortChar123":string,
      /**  ShortChar124  */  
   "ShortChar124":string,
      /**  ShortChar125  */  
   "ShortChar125":string,
      /**  ShortChar126  */  
   "ShortChar126":string,
      /**  ShortChar127  */  
   "ShortChar127":string,
      /**  ShortChar128  */  
   "ShortChar128":string,
      /**  ShortChar129  */  
   "ShortChar129":string,
      /**  ShortChar130  */  
   "ShortChar130":string,
      /**  ShortChar131  */  
   "ShortChar131":string,
      /**  ShortChar132  */  
   "ShortChar132":string,
      /**  ShortChar133  */  
   "ShortChar133":string,
      /**  ShortChar134  */  
   "ShortChar134":string,
      /**  ShortChar135  */  
   "ShortChar135":string,
      /**  ShortChar136  */  
   "ShortChar136":string,
      /**  ShortChar137  */  
   "ShortChar137":string,
      /**  ShortChar138  */  
   "ShortChar138":string,
      /**  ShortChar139  */  
   "ShortChar139":string,
      /**  ShortChar140  */  
   "ShortChar140":string,
      /**  ShortChar141  */  
   "ShortChar141":string,
      /**  ShortChar142  */  
   "ShortChar142":string,
      /**  ShortChar143  */  
   "ShortChar143":string,
      /**  ShortChar144  */  
   "ShortChar144":string,
      /**  ShortChar145  */  
   "ShortChar145":string,
      /**  ShortChar146  */  
   "ShortChar146":string,
      /**  ShortChar147  */  
   "ShortChar147":string,
      /**  ShortChar148  */  
   "ShortChar148":string,
      /**  ShortChar149  */  
   "ShortChar149":string,
      /**  ShortChar150  */  
   "ShortChar150":string,
      /**  ShortChar151  */  
   "ShortChar151":string,
      /**  ShortChar152  */  
   "ShortChar152":string,
      /**  ShortChar153  */  
   "ShortChar153":string,
      /**  ShortChar154  */  
   "ShortChar154":string,
      /**  ShortChar155  */  
   "ShortChar155":string,
      /**  ShortChar156  */  
   "ShortChar156":string,
      /**  ShortChar157  */  
   "ShortChar157":string,
      /**  ShortChar158  */  
   "ShortChar158":string,
      /**  ShortChar159  */  
   "ShortChar159":string,
      /**  ShortChar160  */  
   "ShortChar160":string,
      /**  ShortChar161  */  
   "ShortChar161":string,
      /**  ShortChar162  */  
   "ShortChar162":string,
      /**  ShortChar163  */  
   "ShortChar163":string,
      /**  ShortChar164  */  
   "ShortChar164":string,
      /**  ShortChar165  */  
   "ShortChar165":string,
      /**  ShortChar166  */  
   "ShortChar166":string,
      /**  ShortChar167  */  
   "ShortChar167":string,
      /**  ShortChar168  */  
   "ShortChar168":string,
      /**  ShortChar169  */  
   "ShortChar169":string,
      /**  ShortChar170  */  
   "ShortChar170":string,
      /**  ShortChar171  */  
   "ShortChar171":string,
      /**  ShortChar172  */  
   "ShortChar172":string,
      /**  ShortChar173  */  
   "ShortChar173":string,
      /**  ShortChar174  */  
   "ShortChar174":string,
      /**  ShortChar175  */  
   "ShortChar175":string,
      /**  ShortChar176  */  
   "ShortChar176":string,
      /**  ShortChar177  */  
   "ShortChar177":string,
      /**  ShortChar178  */  
   "ShortChar178":string,
      /**  ShortChar179  */  
   "ShortChar179":string,
      /**  ShortChar180  */  
   "ShortChar180":string,
      /**  ShortChar181  */  
   "ShortChar181":string,
      /**  ShortChar182  */  
   "ShortChar182":string,
      /**  ShortChar183  */  
   "ShortChar183":string,
      /**  ShortChar184  */  
   "ShortChar184":string,
      /**  ShortChar185  */  
   "ShortChar185":string,
      /**  ShortChar186  */  
   "ShortChar186":string,
      /**  ShortChar187  */  
   "ShortChar187":string,
      /**  ShortChar188  */  
   "ShortChar188":string,
      /**  ShortChar189  */  
   "ShortChar189":string,
      /**  ShortChar190  */  
   "ShortChar190":string,
      /**  ShortChar191  */  
   "ShortChar191":string,
      /**  ShortChar192  */  
   "ShortChar192":string,
      /**  ShortChar193  */  
   "ShortChar193":string,
      /**  ShortChar194  */  
   "ShortChar194":string,
      /**  ShortChar195  */  
   "ShortChar195":string,
      /**  ShortChar196  */  
   "ShortChar196":string,
      /**  ShortChar197  */  
   "ShortChar197":string,
      /**  ShortChar198  */  
   "ShortChar198":string,
      /**  ShortChar199  */  
   "ShortChar199":string,
      /**  ShortChar200  */  
   "ShortChar200":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param pcPartNum
      @param piQuantity
      @param piPassedQty
      @param piFailedQty
      @param pcAcceptUM
   */  
export interface ConvQtysToBase_input{
      /**  AcceptUM.  */  
   pcPartNum:string,
      /**  dimQuantity.  */  
   piQuantity:number,
      /**  dimPassedQty.  */  
   piPassedQty:number,
      /**  dimFailedQty.  */  
   piFailedQty:number,
      /**  AcceptUM.  */  
   pcAcceptUM:string,
}

export interface ConvQtysToBase_output{
parameters : {
      /**  output parameters  */  
   piBaseQty:number,
   piBasePassQty:number,
   piBaseFailQty:number,
}
}

   /** Required : 
      @param serialNumberList
      @param partNumList
      @param ds
   */  
export interface CreateLbrScrapSerialNumbersFromList_input{
      /**  Serial Number List  */  
   serialNumberList:string,
      /**  Part Number List  */  
   partNumList:string,
   ds:Erp_Tablesets_InspParamTableset[],
}

export interface CreateLbrScrapSerialNumbersFromList_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspParamTableset[],
}
}

   /** Required : 
      @param inspPlanType
      @param file
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param sampleNumber
      @param inspectDate
      @param inspectTime
   */  
export interface DeleteByID_input{
   inspPlanType:string,
   file:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   sampleNumber:number,
   inspectDate:string,
   inspectTime:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_DynFieldAttributesRow{
   SystemCode:string,
   DataTableID:string,
   FieldName:string,
   DataType:string,
   Required:boolean,
   ReadOnly:boolean,
   FieldFormat:string,
   FieldLabel:string,
   LikeDataFieldSystemCode:string,
   LikeDataFieldTableID:string,
   LikeDataFieldName:string,
   CurrencyCodeColumn:string,
   CurrencyType:string,
   CurrencySource:string,
   BizType:string,
   CGCCode:string,
   UomColumn:string,
   CodeDescriptionList:string,
   Seq:number,
   IsHidden:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynFieldHelpRow{
   SystemCode:string,
   DataTableID:string,
   FieldName:string,
   Description:string,
   DBTableName:string,
   DBFieldName:string,
   External:boolean,
   InitialValue:string,
   IsDescriptionField:boolean,
   SystemFlag:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynTableAttributesRow{
   SystemCode:string,
      /**  The actual generic table name used by the BL  */  
   DataTableID:string,
      /**  Unique identifier for the virtual schema  */  
   UniqueTableID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynamicMetadataTableset{
   DynTableAttributes:Erp_Tablesets_DynTableAttributesRow[],
   DynFieldAttributes:Erp_Tablesets_DynFieldAttributesRow[],
   DynFieldHelp:Erp_Tablesets_DynFieldHelpRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_InspDisplayColumnsRow{
   ColumnName:string,
   ColumnType:string,
   AttributeID:string,
   ColumnFormat:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InspDisplayColumnsTableset{
   InspDisplayColumns:Erp_Tablesets_InspDisplayColumnsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_InspParamRow{
   CallProgram:string,
   CallInspType:string,
   NCMTranID:number,
   NCMTranType:string,
   JobNum:string,
   AssemblySeq:number,
   OprSeq:number,
   PartNum:string,
   RevisionNum:string,
   RMANum:number,
   RMALine:number,
   VendorNum:number,
   PackSlip:string,
   PackLine:number,
   SerialNum:string,
   LotNum:string,
   Quantity:number,
   SeqNum:number,
   PartDesc:string,
   PartNumTrackLots:boolean,
   Sequence:number,
   EntOprInfo:boolean,
   PartNumTrackSN:boolean,
   dataEntered:boolean,
   PurPoint:string,
   MtlSeq:number,
   RcvJobSeqType:string,
   RcvJobSeq:number,
   PONum:number,
   POLine:number,
   InspType:string,
   AltMethod:string,
   FARSeqNum:number,
   ResourceID:string,
   LastView:string,
   AcceptUM:string,
   TrnTyp:string,
   LaborHedSeq:number,
   LaborDtlSeq:number,
   Company:string,
   RMAReceipt:number,
   RMADisp:number,
   RMADispType:string,
   WarehouseCode:string,
      /**  Equipment ID  */  
   EquipID:string,
      /**  Asset ID  */  
   AssetID:string,
      /**  Resource ID  */  
   ResourceSelectID:string,
      /**  Description for Resorce, Asset or Qqupment based on the valuse ot InspType  */  
   InspTypeDesc:string,
      /**  Is Quantity Decimal  */  
   IsQuantityDecimal:boolean,
   EmpID:string,
   AttributeSetID:number,
   AttributeSetShortDescription:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InspParamTableset{
   InspParam:Erp_Tablesets_InspParamRow[],
   InspPlanSampleLst:Erp_Tablesets_InspPlanSampleLstRow[],
   LbrScrapSerialNumbers:Erp_Tablesets_LbrScrapSerialNumbersRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_InspPlanSampleLstRow{
   InspPlanNum:string,
   InspPlanRevNum:string,
   InspPlanDesc:string,
   SpecID:string,
   SpecRevNum:string,
   InspQty:number,
   SpecDoc:boolean,
   SpecRevDoc:boolean,
   SpecDocDisplay:boolean,
   PartInspDoc:boolean,
   SeqPlan:string,
   SpecDesc:string,
   AltMethod:string,
   PartNumTrackSN:boolean,
   PartNumTrackLots:boolean,
      /**  Returns the isDefault from PartRevInspPlan table.  */  
   DefaultPlanPos:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InspResultsAttchRow{
   Company:string,
   InspPlanType:string,
   File:string,
   Key1:string,
   Key2:string,
   Key3:string,
   Key4:string,
   Key5:string,
   SampleNumber:number,
   InspectDate:string,
   InspectTime:number,
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

export interface Erp_Tablesets_InspResultsCharAttchRow{
   Company:string,
   InspPlanType:string,
   File:string,
   Key1:string,
   Key2:string,
   Key3:string,
   Key4:string,
   Key5:string,
   SampleNumber:number,
   InspectDate:string,
   InspectTime:number,
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

export interface Erp_Tablesets_InspResultsCharRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Inspection Plan Type - Inspection, Audit, or Survey  */  
   InspPlanType:string,
      /**  The name of the table that this record pertains to.  */  
   File:string,
      /**  Major component of the primary key to the record.  */  
   Key1:string,
      /**   2nd component of the primary key to the related record.
For example: For a "OrderDtl"   this field would contain the OrderLine # of the related Order detail record.  The usage of this field is dependant on the type of record.  For example "Part" references do not use this field while PartRev  would.  */  
   Key2:string,
      /**   3rd component of the primary key to the related record.
For example: For a "OrderRel"   this field would contain the Order Line Release # of the related Order Release record.  The usage of this field is dependant on the type of record referenced.  */  
   Key3:string,
      /**  4th component of the primary key to the related record.  */  
   Key4:string,
      /**  5th component of the primary key to the related record.  */  
   Key5:string,
      /**  A sequential number up to the total in the Inspection Quantity field.  */  
   SampleNumber:number,
      /**  Date the inspection data was saved  */  
   InspectDate:string,
      /**  System time (seconds since midnight) of when the inspection data was saved  */  
   InspectTime:number,
      /**  Character001  */  
   Character001:string,
      /**  Character002  */  
   Character002:string,
      /**  Character003  */  
   Character003:string,
      /**  Character004  */  
   Character004:string,
      /**  Character005  */  
   Character005:string,
      /**  Character006  */  
   Character006:string,
      /**  Character007  */  
   Character007:string,
      /**  Character008  */  
   Character008:string,
      /**  Character009  */  
   Character009:string,
      /**  Character010  */  
   Character010:string,
      /**  Character011  */  
   Character011:string,
      /**  Character012  */  
   Character012:string,
      /**  Character013  */  
   Character013:string,
      /**  Character014  */  
   Character014:string,
      /**  Character015  */  
   Character015:string,
      /**  Character016  */  
   Character016:string,
      /**  Character017  */  
   Character017:string,
      /**  Character018  */  
   Character018:string,
      /**  Character019  */  
   Character019:string,
      /**  Character020  */  
   Character020:string,
      /**  Character021  */  
   Character021:string,
      /**  Character022  */  
   Character022:string,
      /**  Character023  */  
   Character023:string,
      /**  Character024  */  
   Character024:string,
      /**  Character025  */  
   Character025:string,
      /**  Character026  */  
   Character026:string,
      /**  Character027  */  
   Character027:string,
      /**  Character028  */  
   Character028:string,
      /**  Character029  */  
   Character029:string,
      /**  Character030  */  
   Character030:string,
      /**  Character031  */  
   Character031:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InspResultsCheckBoxAttchRow{
   Company:string,
   InspPlanType:string,
   File:string,
   Key1:string,
   Key2:string,
   Key3:string,
   Key4:string,
   Key5:string,
   SampleNumber:number,
   InspectDate:string,
   InspectTime:number,
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

export interface Erp_Tablesets_InspResultsCheckBoxRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Inspection Plan Type - Inspection, Audit, Survey  */  
   InspPlanType:string,
      /**  The name of the table that this record pertains to.  */  
   File:string,
      /**  Major component of the primary key to the record.  */  
   Key1:string,
      /**   2nd component of the primary key to the related record.
For example: For a "OrderDtl"   this field would contain the OrderLine # of the related Order detail record.  The usage of this field is dependant on the type of record.  For example "Part" references do not use this field while PartRev  would.  */  
   Key2:string,
      /**   3rd component of the primary key to the related record.
For example: For a "OrderRel"   this field would contain the Order Line Release # of the related Order Release record.  The usage of this field is dependant on the type of record referenced.  */  
   Key3:string,
      /**  4th component of the primary key to the related record.  */  
   Key4:string,
      /**  5th component of the primary key to the related record.  */  
   Key5:string,
      /**  A sequential number up to the total in the Inspection Quantity field.  */  
   SampleNumber:number,
      /**  Date the inspection data was saved  */  
   InspectDate:string,
      /**  System time (seconds since midnight) of when the inspection data was saved  */  
   InspectTime:number,
      /**  CheckBox001  */  
   CheckBox001:boolean,
      /**  CheckBox002  */  
   CheckBox002:boolean,
      /**  CheckBox003  */  
   CheckBox003:boolean,
      /**  CheckBox004  */  
   CheckBox004:boolean,
      /**  CheckBox005  */  
   CheckBox005:boolean,
      /**  CheckBox006  */  
   CheckBox006:boolean,
      /**  CheckBox007  */  
   CheckBox007:boolean,
      /**  CheckBox008  */  
   CheckBox008:boolean,
      /**  CheckBox009  */  
   CheckBox009:boolean,
      /**  CheckBox010  */  
   CheckBox010:boolean,
      /**  CheckBox011  */  
   CheckBox011:boolean,
      /**  CheckBox012  */  
   CheckBox012:boolean,
      /**  CheckBox013  */  
   CheckBox013:boolean,
      /**  CheckBox014  */  
   CheckBox014:boolean,
      /**  CheckBox015  */  
   CheckBox015:boolean,
      /**  CheckBox016  */  
   CheckBox016:boolean,
      /**  CheckBox017  */  
   CheckBox017:boolean,
      /**  CheckBox018  */  
   CheckBox018:boolean,
      /**  CheckBox019  */  
   CheckBox019:boolean,
      /**  CheckBox020  */  
   CheckBox020:boolean,
      /**  CheckBox021  */  
   CheckBox021:boolean,
      /**  CheckBox022  */  
   CheckBox022:boolean,
      /**  CheckBox023  */  
   CheckBox023:boolean,
      /**  CheckBox024  */  
   CheckBox024:boolean,
      /**  CheckBox025  */  
   CheckBox025:boolean,
      /**  CheckBox026  */  
   CheckBox026:boolean,
      /**  CheckBox027  */  
   CheckBox027:boolean,
      /**  CheckBox028  */  
   CheckBox028:boolean,
      /**  CheckBox029  */  
   CheckBox029:boolean,
      /**  CheckBox030  */  
   CheckBox030:boolean,
      /**  CheckBox031  */  
   CheckBox031:boolean,
      /**  CheckBox032  */  
   CheckBox032:boolean,
      /**  CheckBox033  */  
   CheckBox033:boolean,
      /**  CheckBox034  */  
   CheckBox034:boolean,
      /**  CheckBox035  */  
   CheckBox035:boolean,
      /**  CheckBox036  */  
   CheckBox036:boolean,
      /**  CheckBox037  */  
   CheckBox037:boolean,
      /**  CheckBox038  */  
   CheckBox038:boolean,
      /**  CheckBox039  */  
   CheckBox039:boolean,
      /**  CheckBox040  */  
   CheckBox040:boolean,
      /**  CheckBox041  */  
   CheckBox041:boolean,
      /**  CheckBox042  */  
   CheckBox042:boolean,
      /**  CheckBox043  */  
   CheckBox043:boolean,
      /**  CheckBox044  */  
   CheckBox044:boolean,
      /**  CheckBox045  */  
   CheckBox045:boolean,
      /**  CheckBox046  */  
   CheckBox046:boolean,
      /**  CheckBox047  */  
   CheckBox047:boolean,
      /**  CheckBox048  */  
   CheckBox048:boolean,
      /**  CheckBox049  */  
   CheckBox049:boolean,
      /**  CheckBox050  */  
   CheckBox050:boolean,
      /**  CheckBox051  */  
   CheckBox051:boolean,
      /**  CheckBox052  */  
   CheckBox052:boolean,
      /**  CheckBox053  */  
   CheckBox053:boolean,
      /**  CheckBox054  */  
   CheckBox054:boolean,
      /**  CheckBox055  */  
   CheckBox055:boolean,
      /**  CheckBox056  */  
   CheckBox056:boolean,
      /**  CheckBox057  */  
   CheckBox057:boolean,
      /**  CheckBox058  */  
   CheckBox058:boolean,
      /**  CheckBox059  */  
   CheckBox059:boolean,
      /**  CheckBox060  */  
   CheckBox060:boolean,
      /**  CheckBox061  */  
   CheckBox061:boolean,
      /**  CheckBox062  */  
   CheckBox062:boolean,
      /**  CheckBox063  */  
   CheckBox063:boolean,
      /**  CheckBox064  */  
   CheckBox064:boolean,
      /**  CheckBox065  */  
   CheckBox065:boolean,
      /**  CheckBox066  */  
   CheckBox066:boolean,
      /**  CheckBox067  */  
   CheckBox067:boolean,
      /**  CheckBox068  */  
   CheckBox068:boolean,
      /**  CheckBox069  */  
   CheckBox069:boolean,
      /**  CheckBox070  */  
   CheckBox070:boolean,
      /**  CheckBox071  */  
   CheckBox071:boolean,
      /**  CheckBox072  */  
   CheckBox072:boolean,
      /**  CheckBox073  */  
   CheckBox073:boolean,
      /**  CheckBox074  */  
   CheckBox074:boolean,
      /**  CheckBox075  */  
   CheckBox075:boolean,
      /**  CheckBox076  */  
   CheckBox076:boolean,
      /**  CheckBox077  */  
   CheckBox077:boolean,
      /**  CheckBox078  */  
   CheckBox078:boolean,
      /**  CheckBox079  */  
   CheckBox079:boolean,
      /**  CheckBox080  */  
   CheckBox080:boolean,
      /**  CheckBox081  */  
   CheckBox081:boolean,
      /**  CheckBox082  */  
   CheckBox082:boolean,
      /**  CheckBox083  */  
   CheckBox083:boolean,
      /**  CheckBox084  */  
   CheckBox084:boolean,
      /**  CheckBox085  */  
   CheckBox085:boolean,
      /**  CheckBox086  */  
   CheckBox086:boolean,
      /**  CheckBox087  */  
   CheckBox087:boolean,
      /**  CheckBox088  */  
   CheckBox088:boolean,
      /**  CheckBox089  */  
   CheckBox089:boolean,
      /**  CheckBox090  */  
   CheckBox090:boolean,
      /**  CheckBox091  */  
   CheckBox091:boolean,
      /**  CheckBox092  */  
   CheckBox092:boolean,
      /**  CheckBox093  */  
   CheckBox093:boolean,
      /**  CheckBox094  */  
   CheckBox094:boolean,
      /**  CheckBox095  */  
   CheckBox095:boolean,
      /**  CheckBox096  */  
   CheckBox096:boolean,
      /**  CheckBox097  */  
   CheckBox097:boolean,
      /**  CheckBox098  */  
   CheckBox098:boolean,
      /**  CheckBox099  */  
   CheckBox099:boolean,
      /**  CheckBox100  */  
   CheckBox100:boolean,
      /**  CheckBox101  */  
   CheckBox101:boolean,
      /**  CheckBox102  */  
   CheckBox102:boolean,
      /**  CheckBox103  */  
   CheckBox103:boolean,
      /**  CheckBox104  */  
   CheckBox104:boolean,
      /**  CheckBox105  */  
   CheckBox105:boolean,
      /**  CheckBox106  */  
   CheckBox106:boolean,
      /**  CheckBox107  */  
   CheckBox107:boolean,
      /**  CheckBox108  */  
   CheckBox108:boolean,
      /**  CheckBox109  */  
   CheckBox109:boolean,
      /**  CheckBox110  */  
   CheckBox110:boolean,
      /**  CheckBox111  */  
   CheckBox111:boolean,
      /**  CheckBox112  */  
   CheckBox112:boolean,
      /**  CheckBox113  */  
   CheckBox113:boolean,
      /**  CheckBox114  */  
   CheckBox114:boolean,
      /**  CheckBox115  */  
   CheckBox115:boolean,
      /**  CheckBox116  */  
   CheckBox116:boolean,
      /**  CheckBox117  */  
   CheckBox117:boolean,
      /**  CheckBox118  */  
   CheckBox118:boolean,
      /**  CheckBox119  */  
   CheckBox119:boolean,
      /**  CheckBox120  */  
   CheckBox120:boolean,
      /**  CheckBox121  */  
   CheckBox121:boolean,
      /**  CheckBox122  */  
   CheckBox122:boolean,
      /**  CheckBox123  */  
   CheckBox123:boolean,
      /**  CheckBox124  */  
   CheckBox124:boolean,
      /**  CheckBox125  */  
   CheckBox125:boolean,
      /**  CheckBox126  */  
   CheckBox126:boolean,
      /**  CheckBox127  */  
   CheckBox127:boolean,
      /**  CheckBox128  */  
   CheckBox128:boolean,
      /**  CheckBox129  */  
   CheckBox129:boolean,
      /**  CheckBox130  */  
   CheckBox130:boolean,
      /**  CheckBox131  */  
   CheckBox131:boolean,
      /**  CheckBox132  */  
   CheckBox132:boolean,
      /**  CheckBox133  */  
   CheckBox133:boolean,
      /**  CheckBox134  */  
   CheckBox134:boolean,
      /**  CheckBox135  */  
   CheckBox135:boolean,
      /**  CheckBox136  */  
   CheckBox136:boolean,
      /**  CheckBox137  */  
   CheckBox137:boolean,
      /**  CheckBox138  */  
   CheckBox138:boolean,
      /**  CheckBox139  */  
   CheckBox139:boolean,
      /**  CheckBox140  */  
   CheckBox140:boolean,
      /**  CheckBox141  */  
   CheckBox141:boolean,
      /**  CheckBox142  */  
   CheckBox142:boolean,
      /**  CheckBox143  */  
   CheckBox143:boolean,
      /**  CheckBox144  */  
   CheckBox144:boolean,
      /**  CheckBox145  */  
   CheckBox145:boolean,
      /**  CheckBox146  */  
   CheckBox146:boolean,
      /**  CheckBox147  */  
   CheckBox147:boolean,
      /**  CheckBox148  */  
   CheckBox148:boolean,
      /**  CheckBox149  */  
   CheckBox149:boolean,
      /**  CheckBox150  */  
   CheckBox150:boolean,
      /**  CheckBox151  */  
   CheckBox151:boolean,
      /**  CheckBox152  */  
   CheckBox152:boolean,
      /**  CheckBox153  */  
   CheckBox153:boolean,
      /**  CheckBox154  */  
   CheckBox154:boolean,
      /**  CheckBox155  */  
   CheckBox155:boolean,
      /**  CheckBox156  */  
   CheckBox156:boolean,
      /**  CheckBox157  */  
   CheckBox157:boolean,
      /**  CheckBox158  */  
   CheckBox158:boolean,
      /**  CheckBox159  */  
   CheckBox159:boolean,
      /**  CheckBox160  */  
   CheckBox160:boolean,
      /**  CheckBox161  */  
   CheckBox161:boolean,
      /**  CheckBox162  */  
   CheckBox162:boolean,
      /**  CheckBox163  */  
   CheckBox163:boolean,
      /**  CheckBox164  */  
   CheckBox164:boolean,
      /**  CheckBox165  */  
   CheckBox165:boolean,
      /**  CheckBox166  */  
   CheckBox166:boolean,
      /**  CheckBox167  */  
   CheckBox167:boolean,
      /**  CheckBox168  */  
   CheckBox168:boolean,
      /**  CheckBox169  */  
   CheckBox169:boolean,
      /**  CheckBox170  */  
   CheckBox170:boolean,
      /**  CheckBox171  */  
   CheckBox171:boolean,
      /**  CheckBox172  */  
   CheckBox172:boolean,
      /**  CheckBox173  */  
   CheckBox173:boolean,
      /**  CheckBox174  */  
   CheckBox174:boolean,
      /**  CheckBox175  */  
   CheckBox175:boolean,
      /**  CheckBox176  */  
   CheckBox176:boolean,
      /**  CheckBox177  */  
   CheckBox177:boolean,
      /**  CheckBox178  */  
   CheckBox178:boolean,
      /**  CheckBox179  */  
   CheckBox179:boolean,
      /**  CheckBox180  */  
   CheckBox180:boolean,
      /**  CheckBox181  */  
   CheckBox181:boolean,
      /**  CheckBox182  */  
   CheckBox182:boolean,
      /**  CheckBox183  */  
   CheckBox183:boolean,
      /**  CheckBox184  */  
   CheckBox184:boolean,
      /**  CheckBox185  */  
   CheckBox185:boolean,
      /**  CheckBox186  */  
   CheckBox186:boolean,
      /**  CheckBox187  */  
   CheckBox187:boolean,
      /**  CheckBox188  */  
   CheckBox188:boolean,
      /**  CheckBox189  */  
   CheckBox189:boolean,
      /**  CheckBox190  */  
   CheckBox190:boolean,
      /**  CheckBox191  */  
   CheckBox191:boolean,
      /**  CheckBox192  */  
   CheckBox192:boolean,
      /**  CheckBox193  */  
   CheckBox193:boolean,
      /**  CheckBox194  */  
   CheckBox194:boolean,
      /**  CheckBox195  */  
   CheckBox195:boolean,
      /**  CheckBox196  */  
   CheckBox196:boolean,
      /**  CheckBox197  */  
   CheckBox197:boolean,
      /**  CheckBox198  */  
   CheckBox198:boolean,
      /**  CheckBox199  */  
   CheckBox199:boolean,
      /**  CheckBox200  */  
   CheckBox200:boolean,
      /**  CheckBox201  */  
   CheckBox201:boolean,
      /**  CheckBox202  */  
   CheckBox202:boolean,
      /**  CheckBox203  */  
   CheckBox203:boolean,
      /**  CheckBox204  */  
   CheckBox204:boolean,
      /**  CheckBox205  */  
   CheckBox205:boolean,
      /**  CheckBox206  */  
   CheckBox206:boolean,
      /**  CheckBox207  */  
   CheckBox207:boolean,
      /**  CheckBox208  */  
   CheckBox208:boolean,
      /**  CheckBox209  */  
   CheckBox209:boolean,
      /**  CheckBox210  */  
   CheckBox210:boolean,
      /**  CheckBox211  */  
   CheckBox211:boolean,
      /**  CheckBox212  */  
   CheckBox212:boolean,
      /**  CheckBox213  */  
   CheckBox213:boolean,
      /**  CheckBox214  */  
   CheckBox214:boolean,
      /**  CheckBox215  */  
   CheckBox215:boolean,
      /**  CheckBox216  */  
   CheckBox216:boolean,
      /**  CheckBox217  */  
   CheckBox217:boolean,
      /**  CheckBox218  */  
   CheckBox218:boolean,
      /**  CheckBox219  */  
   CheckBox219:boolean,
      /**  CheckBox220  */  
   CheckBox220:boolean,
      /**  CheckBox221  */  
   CheckBox221:boolean,
      /**  CheckBox222  */  
   CheckBox222:boolean,
      /**  CheckBox223  */  
   CheckBox223:boolean,
      /**  CheckBox224  */  
   CheckBox224:boolean,
      /**  CheckBox225  */  
   CheckBox225:boolean,
      /**  CheckBox226  */  
   CheckBox226:boolean,
      /**  CheckBox227  */  
   CheckBox227:boolean,
      /**  CheckBox228  */  
   CheckBox228:boolean,
      /**  CheckBox229  */  
   CheckBox229:boolean,
      /**  CheckBox230  */  
   CheckBox230:boolean,
      /**  CheckBox231  */  
   CheckBox231:boolean,
      /**  CheckBox232  */  
   CheckBox232:boolean,
      /**  CheckBox233  */  
   CheckBox233:boolean,
      /**  CheckBox234  */  
   CheckBox234:boolean,
      /**  CheckBox235  */  
   CheckBox235:boolean,
      /**  CheckBox236  */  
   CheckBox236:boolean,
      /**  CheckBox237  */  
   CheckBox237:boolean,
      /**  CheckBox238  */  
   CheckBox238:boolean,
      /**  CheckBox239  */  
   CheckBox239:boolean,
      /**  CheckBox240  */  
   CheckBox240:boolean,
      /**  CheckBox241  */  
   CheckBox241:boolean,
      /**  CheckBox242  */  
   CheckBox242:boolean,
      /**  CheckBox243  */  
   CheckBox243:boolean,
      /**  CheckBox244  */  
   CheckBox244:boolean,
      /**  CheckBox245  */  
   CheckBox245:boolean,
      /**  CheckBox246  */  
   CheckBox246:boolean,
      /**  CheckBox247  */  
   CheckBox247:boolean,
      /**  CheckBox248  */  
   CheckBox248:boolean,
      /**  CheckBox249  */  
   CheckBox249:boolean,
      /**  CheckBox250  */  
   CheckBox250:boolean,
      /**  CheckBox251  */  
   CheckBox251:boolean,
      /**  CheckBox252  */  
   CheckBox252:boolean,
      /**  CheckBox253  */  
   CheckBox253:boolean,
      /**  CheckBox254  */  
   CheckBox254:boolean,
      /**  CheckBox255  */  
   CheckBox255:boolean,
      /**  CheckBox256  */  
   CheckBox256:boolean,
      /**  CheckBox257  */  
   CheckBox257:boolean,
      /**  CheckBox258  */  
   CheckBox258:boolean,
      /**  CheckBox259  */  
   CheckBox259:boolean,
      /**  CheckBox260  */  
   CheckBox260:boolean,
      /**  CheckBox261  */  
   CheckBox261:boolean,
      /**  CheckBox262  */  
   CheckBox262:boolean,
      /**  CheckBox263  */  
   CheckBox263:boolean,
      /**  CheckBox264  */  
   CheckBox264:boolean,
      /**  CheckBox265  */  
   CheckBox265:boolean,
      /**  CheckBox266  */  
   CheckBox266:boolean,
      /**  CheckBox267  */  
   CheckBox267:boolean,
      /**  CheckBox268  */  
   CheckBox268:boolean,
      /**  CheckBox269  */  
   CheckBox269:boolean,
      /**  CheckBox270  */  
   CheckBox270:boolean,
      /**  CheckBox271  */  
   CheckBox271:boolean,
      /**  CheckBox272  */  
   CheckBox272:boolean,
      /**  CheckBox273  */  
   CheckBox273:boolean,
      /**  CheckBox274  */  
   CheckBox274:boolean,
      /**  CheckBox275  */  
   CheckBox275:boolean,
      /**  CheckBox276  */  
   CheckBox276:boolean,
      /**  CheckBox277  */  
   CheckBox277:boolean,
      /**  CheckBox278  */  
   CheckBox278:boolean,
      /**  CheckBox279  */  
   CheckBox279:boolean,
      /**  CheckBox280  */  
   CheckBox280:boolean,
      /**  CheckBox281  */  
   CheckBox281:boolean,
      /**  CheckBox282  */  
   CheckBox282:boolean,
      /**  CheckBox283  */  
   CheckBox283:boolean,
      /**  CheckBox284  */  
   CheckBox284:boolean,
      /**  CheckBox285  */  
   CheckBox285:boolean,
      /**  CheckBox286  */  
   CheckBox286:boolean,
      /**  CheckBox287  */  
   CheckBox287:boolean,
      /**  CheckBox288  */  
   CheckBox288:boolean,
      /**  CheckBox289  */  
   CheckBox289:boolean,
      /**  CheckBox290  */  
   CheckBox290:boolean,
      /**  CheckBox291  */  
   CheckBox291:boolean,
      /**  CheckBox292  */  
   CheckBox292:boolean,
      /**  CheckBox293  */  
   CheckBox293:boolean,
      /**  CheckBox294  */  
   CheckBox294:boolean,
      /**  CheckBox295  */  
   CheckBox295:boolean,
      /**  CheckBox296  */  
   CheckBox296:boolean,
      /**  CheckBox297  */  
   CheckBox297:boolean,
      /**  CheckBox298  */  
   CheckBox298:boolean,
      /**  CheckBox299  */  
   CheckBox299:boolean,
      /**  CheckBox300  */  
   CheckBox300:boolean,
      /**  CheckBox301  */  
   CheckBox301:boolean,
      /**  CheckBox302  */  
   CheckBox302:boolean,
      /**  CheckBox303  */  
   CheckBox303:boolean,
      /**  CheckBox304  */  
   CheckBox304:boolean,
      /**  CheckBox305  */  
   CheckBox305:boolean,
      /**  CheckBox306  */  
   CheckBox306:boolean,
      /**  CheckBox307  */  
   CheckBox307:boolean,
      /**  CheckBox308  */  
   CheckBox308:boolean,
      /**  CheckBox309  */  
   CheckBox309:boolean,
      /**  CheckBox310  */  
   CheckBox310:boolean,
      /**  CheckBox311  */  
   CheckBox311:boolean,
      /**  CheckBox312  */  
   CheckBox312:boolean,
      /**  CheckBox313  */  
   CheckBox313:boolean,
      /**  CheckBox314  */  
   CheckBox314:boolean,
      /**  CheckBox315  */  
   CheckBox315:boolean,
      /**  CheckBox316  */  
   CheckBox316:boolean,
      /**  CheckBox317  */  
   CheckBox317:boolean,
      /**  CheckBox318  */  
   CheckBox318:boolean,
      /**  CheckBox319  */  
   CheckBox319:boolean,
      /**  CheckBox320  */  
   CheckBox320:boolean,
      /**  CheckBox321  */  
   CheckBox321:boolean,
      /**  CheckBox322  */  
   CheckBox322:boolean,
      /**  CheckBox323  */  
   CheckBox323:boolean,
      /**  CheckBox324  */  
   CheckBox324:boolean,
      /**  CheckBox325  */  
   CheckBox325:boolean,
      /**  CheckBox326  */  
   CheckBox326:boolean,
      /**  CheckBox327  */  
   CheckBox327:boolean,
      /**  CheckBox328  */  
   CheckBox328:boolean,
      /**  CheckBox329  */  
   CheckBox329:boolean,
      /**  CheckBox330  */  
   CheckBox330:boolean,
      /**  CheckBox331  */  
   CheckBox331:boolean,
      /**  CheckBox332  */  
   CheckBox332:boolean,
      /**  CheckBox333  */  
   CheckBox333:boolean,
      /**  CheckBox334  */  
   CheckBox334:boolean,
      /**  CheckBox335  */  
   CheckBox335:boolean,
      /**  CheckBox336  */  
   CheckBox336:boolean,
      /**  CheckBox337  */  
   CheckBox337:boolean,
      /**  CheckBox338  */  
   CheckBox338:boolean,
      /**  CheckBox339  */  
   CheckBox339:boolean,
      /**  CheckBox340  */  
   CheckBox340:boolean,
      /**  CheckBox341  */  
   CheckBox341:boolean,
      /**  CheckBox342  */  
   CheckBox342:boolean,
      /**  CheckBox343  */  
   CheckBox343:boolean,
      /**  CheckBox344  */  
   CheckBox344:boolean,
      /**  CheckBox345  */  
   CheckBox345:boolean,
      /**  CheckBox346  */  
   CheckBox346:boolean,
      /**  CheckBox347  */  
   CheckBox347:boolean,
      /**  CheckBox348  */  
   CheckBox348:boolean,
      /**  CheckBox349  */  
   CheckBox349:boolean,
      /**  CheckBox350  */  
   CheckBox350:boolean,
      /**  CheckBox351  */  
   CheckBox351:boolean,
      /**  CheckBox352  */  
   CheckBox352:boolean,
      /**  CheckBox353  */  
   CheckBox353:boolean,
      /**  CheckBox354  */  
   CheckBox354:boolean,
      /**  CheckBox355  */  
   CheckBox355:boolean,
      /**  CheckBox356  */  
   CheckBox356:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InspResultsDateAttchRow{
   Company:string,
   InspPlanType:string,
   File:string,
   Key1:string,
   Key2:string,
   Key3:string,
   Key4:string,
   Key5:string,
   SampleNumber:number,
   InspectDate:string,
   InspectTime:number,
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

export interface Erp_Tablesets_InspResultsDateRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Inspection Plan Type - Inspection, Audit, or Survey  */  
   InspPlanType:string,
      /**  The name of the table that this record pertains to.  */  
   File:string,
      /**  Major component of the primary key to the record.  */  
   Key1:string,
      /**   2nd component of the primary key to the related record.
For example: For a "OrderDtl"   this field would contain the OrderLine # of the related Order detail record.  The usage of this field is dependant on the type of record.  For example "Part" references do not use this field while PartRev  would.  */  
   Key2:string,
      /**   3rd component of the primary key to the related record.
For example: For a "OrderRel"   this field would contain the Order Line Release # of the related Order Release record.  The usage of this field is dependant on the type of record referenced.  */  
   Key3:string,
      /**  4th component of the primary key to the related record.  */  
   Key4:string,
      /**  5th component of the primary key to the related record.  */  
   Key5:string,
      /**  A sequential number up to the total in the Inspection Quantity field.  */  
   SampleNumber:number,
      /**  Date the inspection data was saved  */  
   InspectDate:string,
      /**  System time (seconds since midnight) of when the inspection data was saved  */  
   InspectTime:number,
      /**  Date001  */  
   Date001:string,
      /**  Date002  */  
   Date002:string,
      /**  Date003  */  
   Date003:string,
      /**  Date004  */  
   Date004:string,
      /**  Date005  */  
   Date005:string,
      /**  Date006  */  
   Date006:string,
      /**  Date007  */  
   Date007:string,
      /**  Date008  */  
   Date008:string,
      /**  Date009  */  
   Date009:string,
      /**  Date010  */  
   Date010:string,
      /**  Date011  */  
   Date011:string,
      /**  Date012  */  
   Date012:string,
      /**  Date013  */  
   Date013:string,
      /**  Date014  */  
   Date014:string,
      /**  Date015  */  
   Date015:string,
      /**  Date016  */  
   Date016:string,
      /**  Date017  */  
   Date017:string,
      /**  Date018  */  
   Date018:string,
      /**  Date019  */  
   Date019:string,
      /**  Date020  */  
   Date020:string,
      /**  Date021  */  
   Date021:string,
      /**  Date022  */  
   Date022:string,
      /**  Date023  */  
   Date023:string,
      /**  Date024  */  
   Date024:string,
      /**  Date025  */  
   Date025:string,
      /**  Date026  */  
   Date026:string,
      /**  Date027  */  
   Date027:string,
      /**  Date028  */  
   Date028:string,
      /**  Date029  */  
   Date029:string,
      /**  Date030  */  
   Date030:string,
      /**  Date031  */  
   Date031:string,
      /**  Date032  */  
   Date032:string,
      /**  Date033  */  
   Date033:string,
      /**  Date034  */  
   Date034:string,
      /**  Date035  */  
   Date035:string,
      /**  Date036  */  
   Date036:string,
      /**  Date037  */  
   Date037:string,
      /**  Date038  */  
   Date038:string,
      /**  Date039  */  
   Date039:string,
      /**  Date040  */  
   Date040:string,
      /**  Date041  */  
   Date041:string,
      /**  Date042  */  
   Date042:string,
      /**  Date043  */  
   Date043:string,
      /**  Date044  */  
   Date044:string,
      /**  Date045  */  
   Date045:string,
      /**  Date046  */  
   Date046:string,
      /**  Date047  */  
   Date047:string,
      /**  Date051  */  
   Date051:string,
      /**  Date052  */  
   Date052:string,
      /**  Date053  */  
   Date053:string,
      /**  Date054  */  
   Date054:string,
      /**  Date055  */  
   Date055:string,
      /**  Date056  */  
   Date056:string,
      /**  Date057  */  
   Date057:string,
      /**  Date058  */  
   Date058:string,
      /**  Date059  */  
   Date059:string,
      /**  Date060  */  
   Date060:string,
      /**  Date061  */  
   Date061:string,
      /**  Date062  */  
   Date062:string,
      /**  Date063  */  
   Date063:string,
      /**  Date064  */  
   Date064:string,
      /**  Date065  */  
   Date065:string,
      /**  Date066  */  
   Date066:string,
      /**  Date067  */  
   Date067:string,
      /**  Date068  */  
   Date068:string,
      /**  Date069  */  
   Date069:string,
      /**  Date070  */  
   Date070:string,
      /**  Date071  */  
   Date071:string,
      /**  Date072  */  
   Date072:string,
      /**  Date073  */  
   Date073:string,
      /**  Date074  */  
   Date074:string,
      /**  Date075  */  
   Date075:string,
      /**  Date076  */  
   Date076:string,
      /**  Date077  */  
   Date077:string,
      /**  Date078  */  
   Date078:string,
      /**  Date079  */  
   Date079:string,
      /**  Date080  */  
   Date080:string,
      /**  Date081  */  
   Date081:string,
      /**  Date082  */  
   Date082:string,
      /**  Date083  */  
   Date083:string,
      /**  Date084  */  
   Date084:string,
      /**  Date085  */  
   Date085:string,
      /**  Date086  */  
   Date086:string,
      /**  Date087  */  
   Date087:string,
      /**  Date088  */  
   Date088:string,
      /**  Date089  */  
   Date089:string,
      /**  Date090  */  
   Date090:string,
      /**  Date091  */  
   Date091:string,
      /**  Date092  */  
   Date092:string,
      /**  Date093  */  
   Date093:string,
      /**  Date094  */  
   Date094:string,
      /**  Date095  */  
   Date095:string,
      /**  Date096  */  
   Date096:string,
      /**  Date097  */  
   Date097:string,
      /**  Date101  */  
   Date101:string,
      /**  Date102  */  
   Date102:string,
      /**  Date103  */  
   Date103:string,
      /**  Date104  */  
   Date104:string,
      /**  Date105  */  
   Date105:string,
      /**  Date106  */  
   Date106:string,
      /**  Date107  */  
   Date107:string,
      /**  Date108  */  
   Date108:string,
      /**  Date109  */  
   Date109:string,
      /**  Date110  */  
   Date110:string,
      /**  Date111  */  
   Date111:string,
      /**  Date112  */  
   Date112:string,
      /**  Date113  */  
   Date113:string,
      /**  Date114  */  
   Date114:string,
      /**  Date115  */  
   Date115:string,
      /**  Date116  */  
   Date116:string,
      /**  Date117  */  
   Date117:string,
      /**  Date118  */  
   Date118:string,
      /**  Date119  */  
   Date119:string,
      /**  Date120  */  
   Date120:string,
      /**  Date121  */  
   Date121:string,
      /**  Date122  */  
   Date122:string,
      /**  Date123  */  
   Date123:string,
      /**  Date124  */  
   Date124:string,
      /**  Date125  */  
   Date125:string,
      /**  Date126  */  
   Date126:string,
      /**  Date127  */  
   Date127:string,
      /**  Date128  */  
   Date128:string,
      /**  Date129  */  
   Date129:string,
      /**  Date130  */  
   Date130:string,
      /**  Date131  */  
   Date131:string,
      /**  Date132  */  
   Date132:string,
      /**  Date133  */  
   Date133:string,
      /**  Date134  */  
   Date134:string,
      /**  Date135  */  
   Date135:string,
      /**  Date136  */  
   Date136:string,
      /**  Date137  */  
   Date137:string,
      /**  Date138  */  
   Date138:string,
      /**  Date139  */  
   Date139:string,
      /**  Date140  */  
   Date140:string,
      /**  Date141  */  
   Date141:string,
      /**  Date142  */  
   Date142:string,
      /**  Date143  */  
   Date143:string,
      /**  Date144  */  
   Date144:string,
      /**  Date145  */  
   Date145:string,
      /**  Date146  */  
   Date146:string,
      /**  Date147  */  
   Date147:string,
      /**  Date151  */  
   Date151:string,
      /**  Date152  */  
   Date152:string,
      /**  Date153  */  
   Date153:string,
      /**  Date154  */  
   Date154:string,
      /**  Date155  */  
   Date155:string,
      /**  Date156  */  
   Date156:string,
      /**  Date157  */  
   Date157:string,
      /**  Date158  */  
   Date158:string,
      /**  Date159  */  
   Date159:string,
      /**  Date160  */  
   Date160:string,
      /**  Date161  */  
   Date161:string,
      /**  Date162  */  
   Date162:string,
      /**  Date163  */  
   Date163:string,
      /**  Date164  */  
   Date164:string,
      /**  Date165  */  
   Date165:string,
      /**  Date166  */  
   Date166:string,
      /**  Date167  */  
   Date167:string,
      /**  Date168  */  
   Date168:string,
      /**  Date169  */  
   Date169:string,
      /**  Date170  */  
   Date170:string,
      /**  Date171  */  
   Date171:string,
      /**  Date172  */  
   Date172:string,
      /**  Date173  */  
   Date173:string,
      /**  Date174  */  
   Date174:string,
      /**  Date175  */  
   Date175:string,
      /**  Date176  */  
   Date176:string,
      /**  Date177  */  
   Date177:string,
      /**  Date178  */  
   Date178:string,
      /**  Date179  */  
   Date179:string,
      /**  Date180  */  
   Date180:string,
      /**  Date181  */  
   Date181:string,
      /**  Date182  */  
   Date182:string,
      /**  Date183  */  
   Date183:string,
      /**  Date184  */  
   Date184:string,
      /**  Date185  */  
   Date185:string,
      /**  Date186  */  
   Date186:string,
      /**  Date187  */  
   Date187:string,
      /**  Date188  */  
   Date188:string,
      /**  Date189  */  
   Date189:string,
      /**  Date190  */  
   Date190:string,
      /**  Date191  */  
   Date191:string,
      /**  Date192  */  
   Date192:string,
      /**  Date193  */  
   Date193:string,
      /**  Date194  */  
   Date194:string,
      /**  Date195  */  
   Date195:string,
      /**  Date196  */  
   Date196:string,
      /**  Date197  */  
   Date197:string,
      /**  Date048  */  
   Date048:string,
      /**  Date049  */  
   Date049:string,
      /**  Date050  */  
   Date050:string,
      /**  Date098  */  
   Date098:string,
      /**  Date099  */  
   Date099:string,
      /**  Date100  */  
   Date100:string,
      /**  Date148  */  
   Date148:string,
      /**  Date149  */  
   Date149:string,
      /**  Date150  */  
   Date150:string,
      /**  Date198  */  
   Date198:string,
      /**  Date199  */  
   Date199:string,
      /**  Date200  */  
   Date200:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InspResultsListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Inspection Plan Type.  Valid plan type values - I (Inspection Plan),  C (Calibration Plan).  */  
   InspPlanType:string,
      /**  The name of the table that this record pertains to. Field not currently used.  */  
   File:string,
      /**  Major component of the primary key to the record. Depending on the context in which the inspection was done: for RMA, it would be the RMANum; for Receipts it would be the PackSlip; for FirstArt it would be the JobNum; for Materials, it would be the LaborHedSeq; for Inventory it would be the NCMTranID; JobNum or PartNum when no more information.  */  
   Key1:string,
      /**  2nd component of the primary key to the related record. The usage of this field is dependent on the type of record.  For example:  for a RMA, it would be the RMALine; for a Receipt it would be the PackLine; for FirstArt it would be the AssemblySeq; for Materials, it would be the LaborDtlSeq; in other cases would be the AssemblySeq or the RevisionNum of a PartNum.  */  
   Key2:string,
      /**  3rd component of the primary key to the related record. The usage of this field is dependent on the type of record referenced. The usage of this field is dependent on the type of record referenced. For example: for a RMA, it would be the RMAReceipt; for a Receipt it would be the VendorNum; for FirstArt it would be the OprSeq; in other cases it would be the OprSeq.  */  
   Key3:string,
      /**  4th component of the primary key to the related record.  For Example: for a RMA it would be the RMADisp.  */  
   Key4:string,
      /**  5th component of the primary key to the related record. For future use.  */  
   Key5:string,
      /**  A sequential number up to the total in the Inspection Quantity field.  */  
   SampleNumber:number,
      /**  Date the inspection data was saved  */  
   InspectDate:string,
      /**  System time (seconds since midnight) of when the inspection data was saved  */  
   InspectTime:number,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  Part number inspected  */  
   PartNum:string,
      /**  Revision Number Inspected  */  
   RevisionNum:string,
      /**  Contains the Job Number related to the job or non-conformance being inspected.  */  
   JobNum:string,
      /**  Contain the assembly sequence of the job being inspected  */  
   AssemblySeq:number,
      /**  Contains the operation sequence of the job operation being inspected.  */  
   OprSeq:number,
      /**  Contains the Non-Conformance (NonConf) TranID if inspecting Non-Conformance  */  
   NCMTranID:number,
      /**  Contains the inspection plan part number (configurator part number)  */  
   InspPlanPartNum:string,
      /**  Contains the inspection plan revision number (configurator revision number)  */  
   InspPlanRevNum:string,
      /**  Contains the specification ID that was used in the inspection plan.  */  
   SpecID:string,
      /**  Contains the specification revision number that was used in the inspection process.  */  
   SpecRevNum:string,
      /**  Contains Return Material Authorization number if inspecting for an RMA  */  
   RMANum:number,
      /**  Contains Line number of the RMA if inspecting for an RMA.  */  
   RMALine:number,
      /**  Contain the ResourceGrpID when inspected via Fixed Asset Calibration or Preventative Maintenance Calibration  */  
   ResourceGrpID:string,
      /**  Contain the ResourceID when inspected via Fixed Asset Calibration or Preventative Maintenance Calibration  */  
   ResourceID:string,
      /**  Contains the PO Packing Slip number.  */  
   PackSlip:string,
      /**  Contains the PO Packing Slip line number.  */  
   PackLine:number,
      /**  Contains the VendorNum when inspected via Skip Lot processing  */  
   VendorNum:number,
      /**  Contains the serial number of the part inspected  */  
   SerialNum:string,
      /**  Contains the lot number of the part inspected  */  
   LotNum:string,
      /**  True if passed  */  
   Passed:boolean,
      /**  Text describing why the inspection result failed  */  
   FailedCmtText:string,
      /**  True if the results were saved in product configuration  */  
   TestDataEntered:boolean,
      /**  This is a unique reference number that is assigned by the system for each audit record.  */  
   AuditRefNum:number,
      /**  Purchase point from Vendor.  */  
   PurPoint:string,
      /**  Shows how the audit was created - Scheduled or Manual  */  
   AuditType:string,
      /**  User defined Audit ID  */  
   AuditID:string,
      /**  Supplier Audit Revision Number  */  
   AuditRevNum:string,
      /**  Auditor.  Valid auditor values - E (Employee),  R (Role), S (Supplier)  */  
   Auditor:string,
   AuditSchedDate:string,
      /**  Date the audit reference was created  */  
   AuditCreateDate:string,
      /**  Employee ID.  If an employee code is entered, it must be valid in the EmpBasic table.  */  
   EmpID:string,
      /**  Auditor Supplier Number.  If a supplier number is entered, it must be valid in the Vendor table.  */  
   AuditVendNum:number,
      /**  Date the audit was completed  */  
   AuditCompDate:string,
      /**  Planned, Scheduled, In Progress, Complete  */  
   AuditStatus:string,
      /**  Passed, Failed, Unspecified  */  
   AuditResult:string,
      /**  Supplier Contact number.  If entered, it must be valid in the VendCnt record.  */  
   AuditConNum:number,
      /**  Code that identifies the role of the audit contact.  */  
   AuditConRole:string,
      /**  This is the cost of performing the audit.  */  
   AuditCost:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   Description:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InspResultsListTableset{
   InspResultsList:Erp_Tablesets_InspResultsListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_InspResultsNumAttchRow{
   Company:string,
   InspPlanType:string,
   File:string,
   Key1:string,
   Key2:string,
   Key3:string,
   Key4:string,
   Key5:string,
   SampleNumber:number,
   InspectDate:string,
   InspectTime:number,
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

export interface Erp_Tablesets_InspResultsNumRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Inspection Plan Type - Inspection, Audit, or Survey  */  
   InspPlanType:string,
      /**  The name of the table that this record pertains to.  */  
   File:string,
      /**  Major component of the primary key to the record.  */  
   Key1:string,
      /**   2nd component of the primary key to the related record.
For example: For a "OrderDtl"   this field would contain the OrderLine # of the related Order detail record.  The usage of this field is dependant on the type of record.  For example "Part" references do not use this field while PartRev  would.  */  
   Key2:string,
      /**   3rd component of the primary key to the related record.
For example: For a "OrderRel"   this field would contain the Order Line Release # of the related Order Release record.  The usage of this field is dependant on the type of record referenced.  */  
   Key3:string,
      /**  4th component of the primary key to the related record.  */  
   Key4:string,
      /**  5th component of the primary key to the related record.  */  
   Key5:string,
      /**  A sequential number up to the total in the Inspection Quantity field.  */  
   SampleNumber:number,
      /**  Date the inspection data was saved  */  
   InspectDate:string,
      /**  System time (seconds since midnight) of when the inspection data was saved  */  
   InspectTime:number,
      /**  Number001  */  
   Number001:number,
      /**  Number002  */  
   Number002:number,
      /**  Number003  */  
   Number003:number,
      /**  Number004  */  
   Number004:number,
      /**  Number005  */  
   Number005:number,
      /**  Number006  */  
   Number006:number,
      /**  Number007  */  
   Number007:number,
      /**  Number008  */  
   Number008:number,
      /**  Number009  */  
   Number009:number,
      /**  Number010  */  
   Number010:number,
      /**  Number011  */  
   Number011:number,
      /**  Number012  */  
   Number012:number,
      /**  Number013  */  
   Number013:number,
      /**  Number014  */  
   Number014:number,
      /**  Number015  */  
   Number015:number,
      /**  Number016  */  
   Number016:number,
      /**  Number017  */  
   Number017:number,
      /**  Number018  */  
   Number018:number,
      /**  Number019  */  
   Number019:number,
      /**  Number020  */  
   Number020:number,
      /**  Number021  */  
   Number021:number,
      /**  Number022  */  
   Number022:number,
      /**  Number023  */  
   Number023:number,
      /**  Number024  */  
   Number024:number,
      /**  Number025  */  
   Number025:number,
      /**  Number026  */  
   Number026:number,
      /**  Number027  */  
   Number027:number,
      /**  Number028  */  
   Number028:number,
      /**  Number029  */  
   Number029:number,
      /**  Number030  */  
   Number030:number,
      /**  Number031  */  
   Number031:number,
      /**  Number032  */  
   Number032:number,
      /**  Number033  */  
   Number033:number,
      /**  Number034  */  
   Number034:number,
      /**  Number035  */  
   Number035:number,
      /**  Number036  */  
   Number036:number,
      /**  Number037  */  
   Number037:number,
      /**  Number038  */  
   Number038:number,
      /**  Number039  */  
   Number039:number,
      /**  Number040  */  
   Number040:number,
      /**  Number041  */  
   Number041:number,
      /**  Number042  */  
   Number042:number,
      /**  Number043  */  
   Number043:number,
      /**  Number044  */  
   Number044:number,
      /**  Number045  */  
   Number045:number,
      /**  Number046  */  
   Number046:number,
      /**  Number047  */  
   Number047:number,
      /**  Number048  */  
   Number048:number,
      /**  Number049  */  
   Number049:number,
      /**  Number050  */  
   Number050:number,
      /**  Number051  */  
   Number051:number,
      /**  Number052  */  
   Number052:number,
      /**  Number053  */  
   Number053:number,
      /**  Number054  */  
   Number054:number,
      /**  Number055  */  
   Number055:number,
      /**  Number056  */  
   Number056:number,
      /**  Number057  */  
   Number057:number,
      /**  Number058  */  
   Number058:number,
      /**  Number059  */  
   Number059:number,
      /**  Number060  */  
   Number060:number,
      /**  Number061  */  
   Number061:number,
      /**  Number062  */  
   Number062:number,
      /**  Number063  */  
   Number063:number,
      /**  Number064  */  
   Number064:number,
      /**  Number065  */  
   Number065:number,
      /**  Number066  */  
   Number066:number,
      /**  Number067  */  
   Number067:number,
      /**  Number068  */  
   Number068:number,
      /**  Number069  */  
   Number069:number,
      /**  Number070  */  
   Number070:number,
      /**  Number071  */  
   Number071:number,
      /**  Number072  */  
   Number072:number,
      /**  Number073  */  
   Number073:number,
      /**  Number074  */  
   Number074:number,
      /**  Number075  */  
   Number075:number,
      /**  Number076  */  
   Number076:number,
      /**  Number077  */  
   Number077:number,
      /**  Number078  */  
   Number078:number,
      /**  Number079  */  
   Number079:number,
      /**  Number080  */  
   Number080:number,
      /**  Number081  */  
   Number081:number,
      /**  Number082  */  
   Number082:number,
      /**  Number083  */  
   Number083:number,
      /**  Number084  */  
   Number084:number,
      /**  Number085  */  
   Number085:number,
      /**  Number086  */  
   Number086:number,
      /**  Number087  */  
   Number087:number,
      /**  Number088  */  
   Number088:number,
      /**  Number089  */  
   Number089:number,
      /**  Number090  */  
   Number090:number,
      /**  Number091  */  
   Number091:number,
      /**  Number092  */  
   Number092:number,
      /**  Number093  */  
   Number093:number,
      /**  Number094  */  
   Number094:number,
      /**  Number095  */  
   Number095:number,
      /**  Number096  */  
   Number096:number,
      /**  Number097  */  
   Number097:number,
      /**  Number098  */  
   Number098:number,
      /**  Number099  */  
   Number099:number,
      /**  Number100  */  
   Number100:number,
      /**  Number101  */  
   Number101:number,
      /**  Number102  */  
   Number102:number,
      /**  Number103  */  
   Number103:number,
      /**  Number104  */  
   Number104:number,
      /**  Number105  */  
   Number105:number,
      /**  Number106  */  
   Number106:number,
      /**  Number107  */  
   Number107:number,
      /**  Number108  */  
   Number108:number,
      /**  Number109  */  
   Number109:number,
      /**  Number110  */  
   Number110:number,
      /**  Number111  */  
   Number111:number,
      /**  Number112  */  
   Number112:number,
      /**  Number113  */  
   Number113:number,
      /**  Number114  */  
   Number114:number,
      /**  Number115  */  
   Number115:number,
      /**  Number116  */  
   Number116:number,
      /**  Number117  */  
   Number117:number,
      /**  Number118  */  
   Number118:number,
      /**  Number119  */  
   Number119:number,
      /**  Number120  */  
   Number120:number,
      /**  Number121  */  
   Number121:number,
      /**  Number122  */  
   Number122:number,
      /**  Number123  */  
   Number123:number,
      /**  Number124  */  
   Number124:number,
      /**  Number125  */  
   Number125:number,
      /**  Number126  */  
   Number126:number,
      /**  Number127  */  
   Number127:number,
      /**  Number128  */  
   Number128:number,
      /**  Number129  */  
   Number129:number,
      /**  Number130  */  
   Number130:number,
      /**  Number131  */  
   Number131:number,
      /**  Number132  */  
   Number132:number,
      /**  Number133  */  
   Number133:number,
      /**  Number134  */  
   Number134:number,
      /**  Number135  */  
   Number135:number,
      /**  Number136  */  
   Number136:number,
      /**  Number137  */  
   Number137:number,
      /**  Number138  */  
   Number138:number,
      /**  Number139  */  
   Number139:number,
      /**  Number140  */  
   Number140:number,
      /**  Number141  */  
   Number141:number,
      /**  Number142  */  
   Number142:number,
      /**  Number143  */  
   Number143:number,
      /**  Number144  */  
   Number144:number,
      /**  Number145  */  
   Number145:number,
      /**  Number146  */  
   Number146:number,
      /**  Number147  */  
   Number147:number,
      /**  Number148  */  
   Number148:number,
      /**  Number149  */  
   Number149:number,
      /**  Number150  */  
   Number150:number,
      /**  Number151  */  
   Number151:number,
      /**  Number152  */  
   Number152:number,
      /**  Number153  */  
   Number153:number,
      /**  Number154  */  
   Number154:number,
      /**  Number155  */  
   Number155:number,
      /**  Number156  */  
   Number156:number,
      /**  Number157  */  
   Number157:number,
      /**  Number158  */  
   Number158:number,
      /**  Number159  */  
   Number159:number,
      /**  Number160  */  
   Number160:number,
      /**  Number161  */  
   Number161:number,
      /**  Number162  */  
   Number162:number,
      /**  Number163  */  
   Number163:number,
      /**  Number164  */  
   Number164:number,
      /**  Number165  */  
   Number165:number,
      /**  Number166  */  
   Number166:number,
      /**  Number167  */  
   Number167:number,
      /**  Number168  */  
   Number168:number,
      /**  Number169  */  
   Number169:number,
      /**  Number170  */  
   Number170:number,
      /**  Number171  */  
   Number171:number,
      /**  Number172  */  
   Number172:number,
      /**  Number173  */  
   Number173:number,
      /**  Number174  */  
   Number174:number,
      /**  Number175  */  
   Number175:number,
      /**  Number176  */  
   Number176:number,
      /**  Number177  */  
   Number177:number,
      /**  Number178  */  
   Number178:number,
      /**  Number179  */  
   Number179:number,
      /**  Number180  */  
   Number180:number,
      /**  Number181  */  
   Number181:number,
      /**  Number182  */  
   Number182:number,
      /**  Number183  */  
   Number183:number,
      /**  Number184  */  
   Number184:number,
      /**  Number185  */  
   Number185:number,
      /**  Number186  */  
   Number186:number,
      /**  Number187  */  
   Number187:number,
      /**  Number188  */  
   Number188:number,
      /**  Number189  */  
   Number189:number,
      /**  Number190  */  
   Number190:number,
      /**  Number191  */  
   Number191:number,
      /**  Number192  */  
   Number192:number,
      /**  Number193  */  
   Number193:number,
      /**  Number194  */  
   Number194:number,
      /**  Number195  */  
   Number195:number,
      /**  Number196  */  
   Number196:number,
      /**  Number197  */  
   Number197:number,
      /**  Number198  */  
   Number198:number,
      /**  Number199  */  
   Number199:number,
      /**  Number200  */  
   Number200:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InspResultsRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Inspection Plan Type.  Valid plan type values - I (Inspection Plan),  C (Calibration Plan).  */  
   InspPlanType:string,
      /**  The name of the table that this record pertains to. Field not currently used.  */  
   File:string,
      /**  Major component of the primary key to the record. Depending on the context in which the inspection was done: for RMA, it would be the RMANum; for Receipts it would be the PackSlip; for FirstArt it would be the JobNum; for Materials, it would be the LaborHedSeq; for Inventory it would be the NCMTranID; JobNum or PartNum when no more information.  */  
   Key1:string,
      /**  2nd component of the primary key to the related record. The usage of this field is dependent on the type of record.  For example:  for a RMA, it would be the RMALine; for a Receipt it would be the PackLine; for FirstArt it would be the AssemblySeq; for Materials, it would be the LaborDtlSeq; in other cases would be the AssemblySeq or the RevisionNum of a PartNum.  */  
   Key2:string,
      /**  3rd component of the primary key to the related record. The usage of this field is dependent on the type of record referenced. The usage of this field is dependent on the type of record referenced. For example: for a RMA, it would be the RMAReceipt; for a Receipt it would be the VendorNum; for FirstArt it would be the OprSeq; in other cases it would be the OprSeq.  */  
   Key3:string,
      /**  4th component of the primary key to the related record.  For Example: for a RMA it would be the RMADisp.  */  
   Key4:string,
      /**  5th component of the primary key to the related record. For future use.  */  
   Key5:string,
      /**  A sequential number up to the total in the Inspection Quantity field.  */  
   SampleNumber:number,
      /**  Date the inspection data was saved  */  
   InspectDate:string,
      /**  System time (seconds since midnight) of when the inspection data was saved  */  
   InspectTime:number,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  Part number inspected  */  
   PartNum:string,
      /**  Revision Number Inspected  */  
   RevisionNum:string,
      /**  Contains the Job Number related to the job or non-conformance being inspected.  */  
   JobNum:string,
      /**  Contain the assembly sequence of the job being inspected  */  
   AssemblySeq:number,
      /**  Contains the operation sequence of the job operation being inspected.  */  
   OprSeq:number,
      /**  Contains the Non-Conformance (NonConf) TranID if inspecting Non-Conformance  */  
   NCMTranID:number,
      /**  Contains the inspection plan part number (configurator part number)  */  
   InspPlanPartNum:string,
      /**  Contains the inspection plan revision number (configurator revision number)  */  
   InspPlanRevNum:string,
      /**  Contains the specification ID that was used in the inspection plan.  */  
   SpecID:string,
      /**  Contains the specification revision number that was used in the inspection process.  */  
   SpecRevNum:string,
      /**  Contains Return Material Authorization number if inspecting for an RMA  */  
   RMANum:number,
      /**  Contains Line number of the RMA if inspecting for an RMA.  */  
   RMALine:number,
      /**  Contain the ResourceGrpID when inspected via Fixed Asset Calibration or Preventative Maintenance Calibration  */  
   ResourceGrpID:string,
      /**  Contain the ResourceID when inspected via Fixed Asset Calibration or Preventative Maintenance Calibration  */  
   ResourceID:string,
      /**  Contains the PO Packing Slip number.  */  
   PackSlip:string,
      /**  Contains the PO Packing Slip line number.  */  
   PackLine:number,
      /**  Contains the VendorNum when inspected via Skip Lot processing  */  
   VendorNum:number,
      /**  Contains the serial number of the part inspected  */  
   SerialNum:string,
      /**  Contains the lot number of the part inspected  */  
   LotNum:string,
      /**  True if passed  */  
   Passed:boolean,
      /**  Text describing why the inspection result failed  */  
   FailedCmtText:string,
      /**  True if the results were saved in product configuration  */  
   TestDataEntered:boolean,
      /**  This is a unique reference number that is assigned by the system for each audit record.  */  
   AuditRefNum:number,
      /**  Purchase point from Vendor.  */  
   PurPoint:string,
      /**  Shows how the audit was created - Scheduled or Manual  */  
   AuditType:string,
      /**  User defined Audit ID  */  
   AuditID:string,
      /**  Supplier Audit Revision Number  */  
   AuditRevNum:string,
      /**  Auditor.  Valid auditor values - E (Employee),  R (Role), S (Supplier)  */  
   Auditor:string,
   AuditSchedDate:string,
      /**  Date the audit reference was created  */  
   AuditCreateDate:string,
      /**  Employee ID.  If an employee code is entered, it must be valid in the EmpBasic table.  */  
   EmpID:string,
      /**  Auditor Supplier Number.  If a supplier number is entered, it must be valid in the Vendor table.  */  
   AuditVendNum:number,
      /**  Date the audit was completed  */  
   AuditCompDate:string,
      /**  Planned, Scheduled, In Progress, Complete  */  
   AuditStatus:string,
      /**  Passed, Failed, Unspecified  */  
   AuditResult:string,
      /**  Supplier Contact number.  If entered, it must be valid in the VendCnt record.  */  
   AuditConNum:number,
      /**  Code that identifies the role of the audit contact.  */  
   AuditConRole:string,
      /**  This is the cost of performing the audit.  */  
   AuditCost:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   Description:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InspResultsShortCharAttchRow{
   Company:string,
   InspPlanType:string,
   File:string,
   Key1:string,
   Key2:string,
   Key3:string,
   Key4:string,
   Key5:string,
   SampleNumber:number,
   InspectDate:string,
   InspectTime:number,
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

export interface Erp_Tablesets_InspResultsShortCharRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Inspection Plan Type - Inspection, Audit, or Survey  */  
   InspPlanType:string,
      /**  The name of the table that this record pertains to.  */  
   File:string,
      /**  Major component of the primary key to the record.  */  
   Key1:string,
      /**   2nd component of the primary key to the related record.
For example: For a "OrderDtl"   this field would contain the OrderLine # of the related Order detail record.  The usage of this field is dependant on the type of record.  For example "Part" references do not use this field while PartRev  would.  */  
   Key2:string,
      /**   3rd component of the primary key to the related record.
For example: For a "OrderRel"   this field would contain the Order Line Release # of the related Order Release record.  The usage of this field is dependant on the type of record referenced.  */  
   Key3:string,
      /**  4th component of the primary key to the related record.  */  
   Key4:string,
      /**  5th component of the primary key to the related record.  */  
   Key5:string,
      /**  A sequential number up to the total in the Inspection Quantity field.  */  
   SampleNumber:number,
      /**  Date the inspection data was saved  */  
   InspectDate:string,
      /**  System time (seconds since midnight) of when the inspection data was saved  */  
   InspectTime:number,
      /**  ShortChar001  */  
   ShortChar001:string,
      /**  ShortChar002  */  
   ShortChar002:string,
      /**  ShortChar003  */  
   ShortChar003:string,
      /**  ShortChar004  */  
   ShortChar004:string,
      /**  ShortChar005  */  
   ShortChar005:string,
      /**  ShortChar006  */  
   ShortChar006:string,
      /**  ShortChar007  */  
   ShortChar007:string,
      /**  ShortChar008  */  
   ShortChar008:string,
      /**  ShortChar009  */  
   ShortChar009:string,
      /**  ShortChar010  */  
   ShortChar010:string,
      /**  ShortChar011  */  
   ShortChar011:string,
      /**  ShortChar012  */  
   ShortChar012:string,
      /**  ShortChar013  */  
   ShortChar013:string,
      /**  ShortChar014  */  
   ShortChar014:string,
      /**  ShortChar015  */  
   ShortChar015:string,
      /**  ShortChar016  */  
   ShortChar016:string,
      /**  ShortChar017  */  
   ShortChar017:string,
      /**  ShortChar018  */  
   ShortChar018:string,
      /**  ShortChar019  */  
   ShortChar019:string,
      /**  ShortChar020  */  
   ShortChar020:string,
      /**  ShortChar021  */  
   ShortChar021:string,
      /**  ShortChar022  */  
   ShortChar022:string,
      /**  ShortChar023  */  
   ShortChar023:string,
      /**  ShortChar024  */  
   ShortChar024:string,
      /**  ShortChar025  */  
   ShortChar025:string,
      /**  ShortChar026  */  
   ShortChar026:string,
      /**  ShortChar027  */  
   ShortChar027:string,
      /**  ShortChar028  */  
   ShortChar028:string,
      /**  ShortChar029  */  
   ShortChar029:string,
      /**  ShortChar030  */  
   ShortChar030:string,
      /**  ShortChar031  */  
   ShortChar031:string,
      /**  ShortChar032  */  
   ShortChar032:string,
      /**  ShortChar033  */  
   ShortChar033:string,
      /**  ShortChar034  */  
   ShortChar034:string,
      /**  ShortChar035  */  
   ShortChar035:string,
      /**  ShortChar036  */  
   ShortChar036:string,
      /**  ShortChar037  */  
   ShortChar037:string,
      /**  ShortChar038  */  
   ShortChar038:string,
      /**  ShortChar039  */  
   ShortChar039:string,
      /**  ShortChar040  */  
   ShortChar040:string,
      /**  ShortChar041  */  
   ShortChar041:string,
      /**  ShortChar042  */  
   ShortChar042:string,
      /**  ShortChar043  */  
   ShortChar043:string,
      /**  ShortChar044  */  
   ShortChar044:string,
      /**  ShortChar045  */  
   ShortChar045:string,
      /**  ShortChar046  */  
   ShortChar046:string,
      /**  ShortChar047  */  
   ShortChar047:string,
      /**  ShortChar048  */  
   ShortChar048:string,
      /**  ShortChar049  */  
   ShortChar049:string,
      /**  ShortChar050  */  
   ShortChar050:string,
      /**  ShortChar051  */  
   ShortChar051:string,
      /**  ShortChar052  */  
   ShortChar052:string,
      /**  ShortChar053  */  
   ShortChar053:string,
      /**  ShortChar054  */  
   ShortChar054:string,
      /**  ShortChar055  */  
   ShortChar055:string,
      /**  ShortChar056  */  
   ShortChar056:string,
      /**  ShortChar057  */  
   ShortChar057:string,
      /**  ShortChar058  */  
   ShortChar058:string,
      /**  ShortChar059  */  
   ShortChar059:string,
      /**  ShortChar060  */  
   ShortChar060:string,
      /**  ShortChar061  */  
   ShortChar061:string,
      /**  ShortChar062  */  
   ShortChar062:string,
      /**  ShortChar063  */  
   ShortChar063:string,
      /**  ShortChar064  */  
   ShortChar064:string,
      /**  ShortChar065  */  
   ShortChar065:string,
      /**  ShortChar066  */  
   ShortChar066:string,
      /**  ShortChar067  */  
   ShortChar067:string,
      /**  ShortChar068  */  
   ShortChar068:string,
      /**  ShortChar069  */  
   ShortChar069:string,
      /**  ShortChar070  */  
   ShortChar070:string,
      /**  ShortChar071  */  
   ShortChar071:string,
      /**  ShortChar072  */  
   ShortChar072:string,
      /**  ShortChar073  */  
   ShortChar073:string,
      /**  ShortChar074  */  
   ShortChar074:string,
      /**  ShortChar075  */  
   ShortChar075:string,
      /**  ShortChar076  */  
   ShortChar076:string,
      /**  ShortChar077  */  
   ShortChar077:string,
      /**  ShortChar078  */  
   ShortChar078:string,
      /**  ShortChar079  */  
   ShortChar079:string,
      /**  ShortChar080  */  
   ShortChar080:string,
      /**  ShortChar081  */  
   ShortChar081:string,
      /**  ShortChar082  */  
   ShortChar082:string,
      /**  ShortChar083  */  
   ShortChar083:string,
      /**  ShortChar084  */  
   ShortChar084:string,
      /**  ShortChar085  */  
   ShortChar085:string,
      /**  ShortChar086  */  
   ShortChar086:string,
      /**  ShortChar087  */  
   ShortChar087:string,
      /**  ShortChar088  */  
   ShortChar088:string,
      /**  ShortChar089  */  
   ShortChar089:string,
      /**  ShortChar090  */  
   ShortChar090:string,
      /**  ShortChar091  */  
   ShortChar091:string,
      /**  ShortChar092  */  
   ShortChar092:string,
      /**  ShortChar093  */  
   ShortChar093:string,
      /**  ShortChar094  */  
   ShortChar094:string,
      /**  ShortChar095  */  
   ShortChar095:string,
      /**  ShortChar096  */  
   ShortChar096:string,
      /**  ShortChar097  */  
   ShortChar097:string,
      /**  ShortChar098  */  
   ShortChar098:string,
      /**  ShortChar099  */  
   ShortChar099:string,
      /**  ShortChar100  */  
   ShortChar100:string,
      /**  ShortChar101  */  
   ShortChar101:string,
      /**  ShortChar102  */  
   ShortChar102:string,
      /**  ShortChar103  */  
   ShortChar103:string,
      /**  ShortChar104  */  
   ShortChar104:string,
      /**  ShortChar105  */  
   ShortChar105:string,
      /**  ShortChar106  */  
   ShortChar106:string,
      /**  ShortChar107  */  
   ShortChar107:string,
      /**  ShortChar108  */  
   ShortChar108:string,
      /**  ShortChar109  */  
   ShortChar109:string,
      /**  ShortChar110  */  
   ShortChar110:string,
      /**  ShortChar111  */  
   ShortChar111:string,
      /**  ShortChar112  */  
   ShortChar112:string,
      /**  ShortChar113  */  
   ShortChar113:string,
      /**  ShortChar114  */  
   ShortChar114:string,
      /**  ShortChar115  */  
   ShortChar115:string,
      /**  ShortChar116  */  
   ShortChar116:string,
      /**  ShortChar117  */  
   ShortChar117:string,
      /**  ShortChar118  */  
   ShortChar118:string,
      /**  ShortChar119  */  
   ShortChar119:string,
      /**  ShortChar120  */  
   ShortChar120:string,
      /**  ShortChar121  */  
   ShortChar121:string,
      /**  ShortChar122  */  
   ShortChar122:string,
      /**  ShortChar123  */  
   ShortChar123:string,
      /**  ShortChar124  */  
   ShortChar124:string,
      /**  ShortChar125  */  
   ShortChar125:string,
      /**  ShortChar126  */  
   ShortChar126:string,
      /**  ShortChar127  */  
   ShortChar127:string,
      /**  ShortChar128  */  
   ShortChar128:string,
      /**  ShortChar129  */  
   ShortChar129:string,
      /**  ShortChar130  */  
   ShortChar130:string,
      /**  ShortChar131  */  
   ShortChar131:string,
      /**  ShortChar132  */  
   ShortChar132:string,
      /**  ShortChar133  */  
   ShortChar133:string,
      /**  ShortChar134  */  
   ShortChar134:string,
      /**  ShortChar135  */  
   ShortChar135:string,
      /**  ShortChar136  */  
   ShortChar136:string,
      /**  ShortChar137  */  
   ShortChar137:string,
      /**  ShortChar138  */  
   ShortChar138:string,
      /**  ShortChar139  */  
   ShortChar139:string,
      /**  ShortChar140  */  
   ShortChar140:string,
      /**  ShortChar141  */  
   ShortChar141:string,
      /**  ShortChar142  */  
   ShortChar142:string,
      /**  ShortChar143  */  
   ShortChar143:string,
      /**  ShortChar144  */  
   ShortChar144:string,
      /**  ShortChar145  */  
   ShortChar145:string,
      /**  ShortChar146  */  
   ShortChar146:string,
      /**  ShortChar147  */  
   ShortChar147:string,
      /**  ShortChar148  */  
   ShortChar148:string,
      /**  ShortChar149  */  
   ShortChar149:string,
      /**  ShortChar150  */  
   ShortChar150:string,
      /**  ShortChar151  */  
   ShortChar151:string,
      /**  ShortChar152  */  
   ShortChar152:string,
      /**  ShortChar153  */  
   ShortChar153:string,
      /**  ShortChar154  */  
   ShortChar154:string,
      /**  ShortChar155  */  
   ShortChar155:string,
      /**  ShortChar156  */  
   ShortChar156:string,
      /**  ShortChar157  */  
   ShortChar157:string,
      /**  ShortChar158  */  
   ShortChar158:string,
      /**  ShortChar159  */  
   ShortChar159:string,
      /**  ShortChar160  */  
   ShortChar160:string,
      /**  ShortChar161  */  
   ShortChar161:string,
      /**  ShortChar162  */  
   ShortChar162:string,
      /**  ShortChar163  */  
   ShortChar163:string,
      /**  ShortChar164  */  
   ShortChar164:string,
      /**  ShortChar165  */  
   ShortChar165:string,
      /**  ShortChar166  */  
   ShortChar166:string,
      /**  ShortChar167  */  
   ShortChar167:string,
      /**  ShortChar168  */  
   ShortChar168:string,
      /**  ShortChar169  */  
   ShortChar169:string,
      /**  ShortChar170  */  
   ShortChar170:string,
      /**  ShortChar171  */  
   ShortChar171:string,
      /**  ShortChar172  */  
   ShortChar172:string,
      /**  ShortChar173  */  
   ShortChar173:string,
      /**  ShortChar174  */  
   ShortChar174:string,
      /**  ShortChar175  */  
   ShortChar175:string,
      /**  ShortChar176  */  
   ShortChar176:string,
      /**  ShortChar177  */  
   ShortChar177:string,
      /**  ShortChar178  */  
   ShortChar178:string,
      /**  ShortChar179  */  
   ShortChar179:string,
      /**  ShortChar180  */  
   ShortChar180:string,
      /**  ShortChar181  */  
   ShortChar181:string,
      /**  ShortChar182  */  
   ShortChar182:string,
      /**  ShortChar183  */  
   ShortChar183:string,
      /**  ShortChar184  */  
   ShortChar184:string,
      /**  ShortChar185  */  
   ShortChar185:string,
      /**  ShortChar186  */  
   ShortChar186:string,
      /**  ShortChar187  */  
   ShortChar187:string,
      /**  ShortChar188  */  
   ShortChar188:string,
      /**  ShortChar189  */  
   ShortChar189:string,
      /**  ShortChar190  */  
   ShortChar190:string,
      /**  ShortChar191  */  
   ShortChar191:string,
      /**  ShortChar192  */  
   ShortChar192:string,
      /**  ShortChar193  */  
   ShortChar193:string,
      /**  ShortChar194  */  
   ShortChar194:string,
      /**  ShortChar195  */  
   ShortChar195:string,
      /**  ShortChar196  */  
   ShortChar196:string,
      /**  ShortChar197  */  
   ShortChar197:string,
      /**  ShortChar198  */  
   ShortChar198:string,
      /**  ShortChar199  */  
   ShortChar199:string,
      /**  ShortChar200  */  
   ShortChar200:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InspResultsTableset{
   InspResults:Erp_Tablesets_InspResultsRow[],
   InspResultsAttch:Erp_Tablesets_InspResultsAttchRow[],
   InspResultsChar:Erp_Tablesets_InspResultsCharRow[],
   InspResultsCharAttch:Erp_Tablesets_InspResultsCharAttchRow[],
   InspResultsCheckBox:Erp_Tablesets_InspResultsCheckBoxRow[],
   InspResultsCheckBoxAttch:Erp_Tablesets_InspResultsCheckBoxAttchRow[],
   InspResultsDate:Erp_Tablesets_InspResultsDateRow[],
   InspResultsDateAttch:Erp_Tablesets_InspResultsDateAttchRow[],
   InspResultsNum:Erp_Tablesets_InspResultsNumRow[],
   InspResultsNumAttch:Erp_Tablesets_InspResultsNumAttchRow[],
   InspResultsShortChar:Erp_Tablesets_InspResultsShortCharRow[],
   InspResultsShortCharAttch:Erp_Tablesets_InspResultsShortCharAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_InspSampleLstRow{
   SampleNumber:number,
   LotNum:string,
   Passed:boolean,
   SerialNum:string,
   PartNumTrackLots:boolean,
   PassedText:string,
   PartNumTrackSN:boolean,
   RelatedRowID:string,
   InspPlanRevNum:string,
   SpecID:string,
   SpecRevNum:string,
   InspPlanNum:string,
   InspPlanRevRowID:string,
      /**  Unique identifier of the SpecRev record. The value is a GUID. Currently, only used by configurator to include it in the name of the generated assembly.  */  
   SpecRevRowID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InspSampleLstTableset{
   InspSampleLst:Erp_Tablesets_InspSampleLstRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_LbrScrapSerialNumbersRow{
      /**  Company  */  
   Company:string,
      /**  LaborHedSeq of the related LaborDtl  */  
   LaborHedSeq:number,
      /**  LaborDtlSeq of the related LaborDtl  */  
   LaborDtlSeq:number,
      /**  Serial Number  */  
   SerialNumber:string,
      /**  Part Number  */  
   PartNum:string,
      /**  Job Number  */  
   JobNum:string,
      /**  AssemblySeq this scrap serial number is for  */  
   AssemblySeq:number,
      /**  OprSeq this scrap serial number is for  */  
   OprSeq:number,
      /**  Indicates whether the Status field can be updated.  */  
   EnableStatus:boolean,
      /**  New status for the serial number. This field will require Code/Desc definition: REJECTED`Scrap INSPECTION`Nonconformance WIP`WIP  */  
   SNStatus:string,
      /**  The SNStatus description ? set same as SerialNo.SNStatusTrans  */  
   SNStatusDesc:string,
      /**  Serial Number Selected for process  */  
   Selected:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SNFormatRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  The PartNum field identifies the Part and is used in the primary key.  */  
   PartNum:string,
      /**  Number of digits in the serial number  */  
   NumberOfDigits:number,
      /**  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  */  
   SNMask:string,
      /**   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  */  
   SNBaseDataType:string,
      /**   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  */  
   SNFormat:string,
      /**  Whether or not to have leading zeroes  */  
   LeadingZeroes:boolean,
      /**   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  */  
   SNPrefix:string,
      /**  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  */  
   SNMaskSuffix:string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  */  
   SNMaskPrefix:string,
      /**  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  */  
   SNLastUsedSeq:string,
   HasSerialNumbers:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   PartPricePerCode:string,
   PartTrackLots:boolean,
   PartTrackSerialNum:boolean,
   PartTrackDimension:boolean,
   PartSalesUM:string,
   PartIUM:string,
   PartSellingFactor:number,
   PartPartDescription:string,
   SerialMaskMaskType:number,
   SerialMaskMask:string,
   SerialMaskExample:string,
   SerialMaskDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SelectSerialNumbersParamsRow{
      /**  The part number to which the serial numbers have been assigned.  */  
   partNum:string,
      /**  The quantity of serial numbers that need to be selected.  */  
   quantity:number,
      /**  whereClause for filtering available serial numbers  */  
   whereClause:string,
      /**  transType of this transaction  */  
   transType:string,
      /**  Include when filtering a set of SN's for BL processing is necessary.  It may be null if not needed.  */  
   sourceRowID:string,
      /**  Determines if serial numbers can be created.  */  
   enableCreate:boolean,
      /**  Determines if serial numbers can be selected.  */  
   enableSelect:boolean,
      /**  Determines if serial numbers can be retrieved.  */  
   enableRetrieve:boolean,
      /**  Specifies whether Voided serial numbers can be manually selected.  */  
   allowVoided:boolean,
      /**  The Plant associated with this transaction  */  
   plant:string,
   xrefPartNum:string,
   xrefPartType:string,
   xrefCustNum:number,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   poLinkValues:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   attributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   attributeSetShortDescription:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   revisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SelectSerialNumbersParamsTableset{
   SelectSerialNumbersParams:Erp_Tablesets_SelectSerialNumbersParamsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SelectedSerialNumbersRow{
      /**  Company  */  
   Company:string,
      /**  SerialNumber  */  
   SerialNumber:string,
      /**  Scrapped flag  */  
   Scrapped:boolean,
      /**  Scrapped reason code  */  
   ScrappedReasonCode:string,
      /**  Voided flag  */  
   Voided:boolean,
      /**  Reference field  */  
   Reference:string,
      /**  Reason code type = s  */  
   ReasonCodeType:string,
      /**  Reason code description  */  
   ReasonCodeDesc:string,
      /**  PartNumber  */  
   PartNum:string,
      /**  Serial number prefix  */  
   SNPrefix:string,
      /**  Base number used to create the serial number  */  
   SNBaseNumber:string,
      /**  RowID of the source record for this serial number  */  
   SourceRowID:string,
      /**  TransType of the record that created this serial number  */  
   TransType:string,
      /**  True if this serial numbered part passed inspection  */  
   PassedInspection:boolean,
      /**  Used to flag previously selected serial numbers as deselected  */  
   Deselected:boolean,
   KitWhseList:string,
      /**  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  */  
   RawSerialNum:string,
      /**  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  */  
   KBLbrAction:number,
      /**  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  */  
   KBLbrActionDesc:string,
      /**  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  */  
   PreventDeselect:boolean,
      /**  Used only by SN Assignment  */  
   XRefPartNum:string,
      /**  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  */  
   XRefPartType:string,
   PreDeselected:boolean,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   poLinkValues:string,
      /**  The mask the was used to generate the serial number  */  
   SNMask:string,
      /**  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  */  
   NotSavedToDB:boolean,
   RowSelected:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtInspResultsTableset{
   InspResults:Erp_Tablesets_InspResultsRow[],
   InspResultsAttch:Erp_Tablesets_InspResultsAttchRow[],
   InspResultsChar:Erp_Tablesets_InspResultsCharRow[],
   InspResultsCharAttch:Erp_Tablesets_InspResultsCharAttchRow[],
   InspResultsCheckBox:Erp_Tablesets_InspResultsCheckBoxRow[],
   InspResultsCheckBoxAttch:Erp_Tablesets_InspResultsCheckBoxAttchRow[],
   InspResultsDate:Erp_Tablesets_InspResultsDateRow[],
   InspResultsDateAttch:Erp_Tablesets_InspResultsDateAttchRow[],
   InspResultsNum:Erp_Tablesets_InspResultsNumRow[],
   InspResultsNumAttch:Erp_Tablesets_InspResultsNumAttchRow[],
   InspResultsShortChar:Erp_Tablesets_InspResultsShortCharRow[],
   InspResultsShortCharAttch:Erp_Tablesets_InspResultsShortCharAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
      @param callProgram
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param dateStamp
      @param timeStamp
      @param inspPlanNum
      @param inspRevNum
      @param specID
      @param specRevNum
      @param inspectQty
      @param ds1
   */  
export interface GenerateResults_input{
   ds:Erp_Tablesets_InspParamTableset[],
      /**  The calling program  */  
   callProgram:string,
      /**  Key1 of existing records  */  
   key1:string,
      /**  Key2 of existing records  */  
   key2:string,
      /**  Key3 of existing records  */  
   key3:string,
      /**  Key4 of existing records  */  
   key4:string,
      /**  Key5 of existing records  */  
   key5:string,
      /**  DateStamp of existing records  */  
   dateStamp:string,
      /**  TimeStamp of existing records  */  
   timeStamp:number,
      /**  Inspection Plan Number.  */  
   inspPlanNum:string,
      /**  Inspection Revision Number.  */  
   inspRevNum:string,
      /**  Specification ID.  */  
   specID:string,
      /**  Specification revision number.  */  
   specRevNum:string,
      /**  Inspection Quantity.  */  
   inspectQty:number,
   ds1:Erp_Tablesets_InspSampleLstTableset[],
}

export interface GenerateResults_output{
parameters : {
      /**  output parameters  */  
   ds1:Erp_Tablesets_InspSampleLstTableset[],
}
}

   /** Required : 
      @param inspPlanType
      @param file
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param sampleNumber
      @param inspectDate
      @param inspectTime
   */  
export interface GetByID_input{
   inspPlanType:string,
   file:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   sampleNumber:number,
   inspectDate:string,
   inspectTime:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_InspResultsTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_InspResultsTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_InspResultsTableset[],
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

   /** Required : 
      @param inSpecID
      @param inSpecRevNum
      @param inInspPlanPartNum
      @param inInspPlanRevNum
   */  
export interface GetDisplayColumns_input{
      /**  The specification ID  */  
   inSpecID:string,
      /**  The specification revision number  */  
   inSpecRevNum:string,
      /**  The inspection plan part number  */  
   inInspPlanPartNum:string,
      /**  The inspection plan revision number  */  
   inInspPlanRevNum:string,
}

export interface GetDisplayColumns_output{
   returnObj:Erp_Tablesets_InspDisplayColumnsTableset[],
}

   /** Required : 
      @param callProgram
      @param callInspType
      @param tgtRowID
      @param inNCMTranID
      @param inNCMTranType
      @param inJobNum
      @param inAsmSeq
      @param inOprSeq
      @param inPartNum
      @param inRevisionNum
      @param inRMANum
      @param inRMALine
      @param inRMAReceipt
      @param inRMADisp
      @param inRMADispType
      @param inWhseCode
      @param inVendorNum
      @param inPurPoint
      @param inPackSlip
      @param inPackLine
      @param inSerialNum
      @param inLotNum
      @param inQty
      @param inResourceID
      @param inSeqNum
      @param inEmpID
      @param inAttributeSetID
   */  
export interface GetInspParams_input{
      /**  The calling program  */  
   callProgram:string,
      /**  The calling inspection type  */  
   callInspType:string,
      /**  The rowid of the calling inspection record  */  
   tgtRowID:string,
      /**  The calling program  */  
   inNCMTranID:number,
      /**  The calling program  */  
   inNCMTranType:string,
      /**  The calling program  */  
   inJobNum:string,
      /**  The calling program  */  
   inAsmSeq:number,
      /**  The calling program  */  
   inOprSeq:number,
      /**  The calling program  */  
   inPartNum:string,
      /**  The calling program  */  
   inRevisionNum:string,
      /**  The calling program  */  
   inRMANum:number,
      /**  The calling program  */  
   inRMALine:number,
      /**  The calling program  */  
   inRMAReceipt:number,
      /**  The calling program  */  
   inRMADisp:number,
      /**  The calling program  */  
   inRMADispType:string,
      /**  The calling program  */  
   inWhseCode:string,
      /**  The calling program  */  
   inVendorNum:number,
      /**  The calling program  */  
   inPurPoint:string,
      /**  The calling program  */  
   inPackSlip:string,
      /**  The calling program  */  
   inPackLine:number,
      /**  The calling program  */  
   inSerialNum:string,
      /**  The calling program  */  
   inLotNum:string,
      /**  The calling program  */  
   inQty:number,
      /**  ResourceID from the calling program  */  
   inResourceID:string,
      /**  SeqNum from the calling program  */  
   inSeqNum:number,
      /**  EmpID from the calling program  */  
   inEmpID:string,
   inAttributeSetID:number,
}

export interface GetInspParams_output{
   returnObj:Erp_Tablesets_InspParamTableset[],
}

   /** Required : 
      @param ds
   */  
export interface GetInspPlanPartNum_input{
   ds:Erp_Tablesets_InspParamTableset[],
}

export interface GetInspPlanPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspParamTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetInspQty_input{
   ds:Erp_Tablesets_InspParamTableset[],
}

export interface GetInspQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspParamTableset[],
}
}

   /** Required : 
      @param pcLaborRowIdent
      @param ds
   */  
export interface GetLaborSelectedSerialNumbers_input{
      /**  Input RowIdent field  of InspNonConf datatable  */  
   pcLaborRowIdent:string,
   ds:Erp_Tablesets_InspParamTableset[],
}

export interface GetLaborSelectedSerialNumbers_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspParamTableset[],
}
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
   returnObj:Erp_Tablesets_InspResultsListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param inspPlanType
      @param file
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param sampleNumber
      @param inspectDate
      @param inspectTime
   */  
export interface GetNewInspResultsAttch_input{
   ds:Erp_Tablesets_InspResultsTableset[],
   inspPlanType:string,
   file:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   sampleNumber:number,
   inspectDate:string,
   inspectTime:number,
}

export interface GetNewInspResultsAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspResultsTableset[],
}
}

   /** Required : 
      @param ds
      @param inspPlanType
      @param file
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param sampleNumber
      @param inspectDate
      @param inspectTime
   */  
export interface GetNewInspResultsCharAttch_input{
   ds:Erp_Tablesets_InspResultsTableset[],
   inspPlanType:string,
   file:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   sampleNumber:number,
   inspectDate:string,
   inspectTime:number,
}

export interface GetNewInspResultsCharAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspResultsTableset[],
}
}

   /** Required : 
      @param ds
      @param inspPlanType
      @param file
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param sampleNumber
      @param inspectDate
   */  
export interface GetNewInspResultsChar_input{
   ds:Erp_Tablesets_InspResultsTableset[],
   inspPlanType:string,
   file:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   sampleNumber:number,
   inspectDate:string,
}

export interface GetNewInspResultsChar_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspResultsTableset[],
}
}

   /** Required : 
      @param ds
      @param inspPlanType
      @param file
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param sampleNumber
      @param inspectDate
      @param inspectTime
   */  
export interface GetNewInspResultsCheckBoxAttch_input{
   ds:Erp_Tablesets_InspResultsTableset[],
   inspPlanType:string,
   file:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   sampleNumber:number,
   inspectDate:string,
   inspectTime:number,
}

export interface GetNewInspResultsCheckBoxAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspResultsTableset[],
}
}

   /** Required : 
      @param ds
      @param inspPlanType
      @param file
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param sampleNumber
      @param inspectDate
   */  
export interface GetNewInspResultsCheckBox_input{
   ds:Erp_Tablesets_InspResultsTableset[],
   inspPlanType:string,
   file:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   sampleNumber:number,
   inspectDate:string,
}

export interface GetNewInspResultsCheckBox_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspResultsTableset[],
}
}

   /** Required : 
      @param ds
      @param inspPlanType
      @param file
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param sampleNumber
      @param inspectDate
      @param inspectTime
   */  
export interface GetNewInspResultsDateAttch_input{
   ds:Erp_Tablesets_InspResultsTableset[],
   inspPlanType:string,
   file:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   sampleNumber:number,
   inspectDate:string,
   inspectTime:number,
}

export interface GetNewInspResultsDateAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspResultsTableset[],
}
}

   /** Required : 
      @param ds
      @param inspPlanType
      @param file
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param sampleNumber
      @param inspectDate
   */  
export interface GetNewInspResultsDate_input{
   ds:Erp_Tablesets_InspResultsTableset[],
   inspPlanType:string,
   file:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   sampleNumber:number,
   inspectDate:string,
}

export interface GetNewInspResultsDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspResultsTableset[],
}
}

   /** Required : 
      @param ds
      @param inspPlanType
      @param file
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param sampleNumber
      @param inspectDate
      @param inspectTime
   */  
export interface GetNewInspResultsNumAttch_input{
   ds:Erp_Tablesets_InspResultsTableset[],
   inspPlanType:string,
   file:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   sampleNumber:number,
   inspectDate:string,
   inspectTime:number,
}

export interface GetNewInspResultsNumAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspResultsTableset[],
}
}

   /** Required : 
      @param ds
      @param inspPlanType
      @param file
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param sampleNumber
      @param inspectDate
   */  
export interface GetNewInspResultsNum_input{
   ds:Erp_Tablesets_InspResultsTableset[],
   inspPlanType:string,
   file:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   sampleNumber:number,
   inspectDate:string,
}

export interface GetNewInspResultsNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspResultsTableset[],
}
}

   /** Required : 
      @param ds
      @param inspPlanType
      @param file
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param sampleNumber
      @param inspectDate
      @param inspectTime
   */  
export interface GetNewInspResultsShortCharAttch_input{
   ds:Erp_Tablesets_InspResultsTableset[],
   inspPlanType:string,
   file:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   sampleNumber:number,
   inspectDate:string,
   inspectTime:number,
}

export interface GetNewInspResultsShortCharAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspResultsTableset[],
}
}

   /** Required : 
      @param ds
      @param inspPlanType
      @param file
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param sampleNumber
      @param inspectDate
   */  
export interface GetNewInspResultsShortChar_input{
   ds:Erp_Tablesets_InspResultsTableset[],
   inspPlanType:string,
   file:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   sampleNumber:number,
   inspectDate:string,
}

export interface GetNewInspResultsShortChar_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspResultsTableset[],
}
}

   /** Required : 
      @param ds
      @param inspPlanType
      @param file
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param sampleNumber
      @param inspectDate
   */  
export interface GetNewInspResults_input{
   ds:Erp_Tablesets_InspResultsTableset[],
   inspPlanType:string,
   file:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   sampleNumber:number,
   inspectDate:string,
}

export interface GetNewInspResults_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspResultsTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewLbrScrapSerialNumbers_input{
   ds:Erp_Tablesets_InspParamTableset[],
}

export interface GetNewLbrScrapSerialNumbers_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspParamTableset[],
}
}

   /** Required : 
      @param quantity
      @param nonConformanceQty
      @param ds
   */  
export interface GetNonConformanceQty_input{
   quantity:number,
   nonConformanceQty:number,
   ds:Erp_Tablesets_InspSampleLstTableset[],
}

export interface GetNonConformanceQty_output{
parameters : {
      /**  output parameters  */  
   quantity:number,
   nonConformanceQty:number,
   ds:Erp_Tablesets_InspSampleLstTableset[],
}
}

   /** Required : 
      @param relatedRowID
      @param inspType
   */  
export interface GetPassedFailed_input{
      /**  RowID of the InspResults record  */  
   relatedRowID:string,
      /**  inspection Type  */  
   inspType:string,
}

export interface GetPassedFailed_output{
parameters : {
      /**  output parameters  */  
   passedSetting:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetRMASelectSerialNumbersParams_input{
   ds:Erp_Tablesets_InspParamTableset[],
}

export interface GetRMASelectSerialNumbersParams_output{
   returnObj:Erp_Tablesets_SelectSerialNumbersParamsTableset[],
}

   /** Required : 
      @param pcRowIdent
      @param ds
   */  
export interface GetRMASelectedSerialNumbers_input{
      /**  Input RowIdent field  of InspNonConf datatable  */  
   pcRowIdent:string,
   ds:Erp_Tablesets_InspParamTableset[],
}

export interface GetRMASelectedSerialNumbers_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspParamTableset[],
}
}

   /** Required : 
      @param inspSampleListDS
   */  
export interface GetResults_input{
   inspSampleListDS:Erp_Tablesets_InspSampleLstTableset[],
}

export interface GetResults_output{
      /**  Results dataset  */  
   returnObj:any,      //schema had no properties on an object.
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DynamicMetadataTableset[],
}
}

   /** Required : 
      @param whereClauseInspResults
      @param whereClauseInspResultsAttch
      @param whereClauseInspResultsChar
      @param whereClauseInspResultsCharAttch
      @param whereClauseInspResultsCheckBox
      @param whereClauseInspResultsCheckBoxAttch
      @param whereClauseInspResultsDate
      @param whereClauseInspResultsDateAttch
      @param whereClauseInspResultsNum
      @param whereClauseInspResultsNumAttch
      @param whereClauseInspResultsShortChar
      @param whereClauseInspResultsShortCharAttch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseInspResults:string,
   whereClauseInspResultsAttch:string,
   whereClauseInspResultsChar:string,
   whereClauseInspResultsCharAttch:string,
   whereClauseInspResultsCheckBox:string,
   whereClauseInspResultsCheckBoxAttch:string,
   whereClauseInspResultsDate:string,
   whereClauseInspResultsDateAttch:string,
   whereClauseInspResultsNum:string,
   whereClauseInspResultsNumAttch:string,
   whereClauseInspResultsShortChar:string,
   whereClauseInspResultsShortCharAttch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_InspResultsTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param enableCreate
   */  
export interface GetSelectSerialNumbersParams_input{
   ds:Erp_Tablesets_InspParamTableset[],
      /**  Enable create serial numbers  */  
   enableCreate:boolean,
}

export interface GetSelectSerialNumbersParams_output{
   returnObj:Erp_Tablesets_SelectSerialNumbersParamsTableset[],
}

   /** Required : 
      @param ds
   */  
export interface GetSpecID_input{
   ds:Erp_Tablesets_InspParamTableset[],
}

export interface GetSpecID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspParamTableset[],
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
      @param proposedValue
   */  
export interface IsDecimalValue_input{
   proposedValue:number,
}

export interface IsDecimalValue_output{
   returnObj:boolean,
}

   /** Required : 
      @param piProposedInspPlan
      @param ds
   */  
export interface OnChangeInspPlan_input{
      /**  The new proposed inspection plan part num value  */  
   piProposedInspPlan:string,
   ds:Erp_Tablesets_InspParamTableset[],
}

export interface OnChangeInspPlan_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspParamTableset[],
}
}

   /** Required : 
      @param pcProposedInspType
      @param ds
   */  
export interface OnChangeInspType_input{
      /**  The new proposed inspection type value  */  
   pcProposedInspType:string,
   ds:Erp_Tablesets_InspParamTableset[],
}

export interface OnChangeInspType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspParamTableset[],
}
}

   /** Required : 
      @param piProposedAssemblySeq
      @param ds
   */  
export interface OnChangeJobAsm_input{
      /**  The new proposed Job Assembly value  */  
   piProposedAssemblySeq:number,
   ds:Erp_Tablesets_InspParamTableset[],
}

export interface OnChangeJobAsm_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspParamTableset[],
}
}

   /** Required : 
      @param pcProposedJobNum
      @param ds
   */  
export interface OnChangeJobNum_input{
      /**  The new proposed JobNum value  */  
   pcProposedJobNum:string,
   ds:Erp_Tablesets_InspParamTableset[],
}

export interface OnChangeJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspParamTableset[],
}
}

   /** Required : 
      @param piProposedOprSeq
      @param ds
   */  
export interface OnChangeJobOpr_input{
      /**  The new proposed Job Operation Sequence value  */  
   piProposedOprSeq:number,
   ds:Erp_Tablesets_InspParamTableset[],
}

export interface OnChangeJobOpr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspParamTableset[],
}
}

   /** Required : 
      @param pcProposedNCMTranID
      @param ds
   */  
export interface OnChangeNCMID_input{
      /**  The new proposed NCMTranID value  */  
   pcProposedNCMTranID:number,
   ds:Erp_Tablesets_InspParamTableset[],
}

export interface OnChangeNCMID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspParamTableset[],
}
}

   /** Required : 
      @param piProposedPartNum
      @param ds
   */  
export interface OnChangePartNum_input{
      /**  The new proposed PartNum value  */  
   piProposedPartNum:string,
   ds:Erp_Tablesets_InspParamTableset[],
}

export interface OnChangePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspParamTableset[],
}
}

   /** Required : 
      @param piProposedSpecID
      @param ds
   */  
export interface OnChangeSpecID_input{
      /**  The new proposed specification id value  */  
   piProposedSpecID:string,
   ds:Erp_Tablesets_InspParamTableset[],
}

export interface OnChangeSpecID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspParamTableset[],
}
}

   /** Required : 
      @param piProposedSpecRev
      @param ds
   */  
export interface OnChangeSpecRev_input{
      /**  The new proposed specification revision value  */  
   piProposedSpecRev:string,
   ds:Erp_Tablesets_InspParamTableset[],
}

export interface OnChangeSpecRev_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspParamTableset[],
}
}

   /** Required : 
      @param ds
      @param inspPlanNum
      @param inspRevNum
      @param specID
      @param specRevNum
      @param inspectQty
   */  
export interface PreGenerateResultsForSpecification_input{
   ds:Erp_Tablesets_InspParamTableset[],
      /**  Inspection Plan Number.  */  
   inspPlanNum:string,
      /**  Inspection Revision Number.  */  
   inspRevNum:string,
      /**  Specification ID.  */  
   specID:string,
      /**  Specification revision number.  */  
   specRevNum:string,
      /**  Inspection Quantity.  */  
   inspectQty:number,
}

export interface PreGenerateResultsForSpecification_output{
parameters : {
      /**  output parameters  */  
   existsMessage:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   dateStamp:string,
   timeStamp:number,
}
}

   /** Required : 
      @param ds
      @param inspPlanNum
      @param inspRevNum
      @param specID
      @param specRevNum
      @param inspectQty
   */  
export interface PreGenerateResults_input{
   ds:Erp_Tablesets_InspParamTableset[],
      /**  Inspection Plan Number.  */  
   inspPlanNum:string,
      /**  Inspection Revision Number.  */  
   inspRevNum:string,
      /**  Specification ID.  */  
   specID:string,
      /**  Specification revision number.  */  
   specRevNum:string,
      /**  Inspection Quantity.  */  
   inspectQty:number,
}

export interface PreGenerateResults_output{
parameters : {
      /**  output parameters  */  
   existsMessage:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   dateStamp:string,
   timeStamp:number,
}
}

   /** Required : 
      @param ds
      @param relatedRowID
   */  
export interface RetrieveValues_input{
   ds:Erp_Tablesets_InspParamTableset[],
      /**  RowID of the InspResults record.  */  
   relatedRowID:string,
}

export interface RetrieveValues_output{
   returnObj:Erp_Tablesets_InspResultsTableset[],
}

   /** Required : 
      @param dynamicResultsDataSet
      @param ds
   */  
export interface UpdateDynamicResults_input{
   dynamicResultsDataSet:any,      //schema had no properties on an object.
   ds:Erp_Tablesets_InspSampleLstTableset[],
}

export interface UpdateDynamicResults_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspSampleLstTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtInspResultsTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtInspResultsTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
      @param ds1
   */  
export interface UpdateSelectedSN_input{
   ds:Erp_Tablesets_InspSampleLstTableset[],
   ds1:Erp_Tablesets_InspParamTableset[],
}

export interface UpdateSelectedSN_output{
parameters : {
      /**  output parameters  */  
   ds1:Erp_Tablesets_InspParamTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_InspResultsTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspResultsTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ValidateSerialAfterSelect_input{
   ds:Erp_Tablesets_InspParamTableset[],
}

export interface ValidateSerialAfterSelect_output{
}

   /** Required : 
      @param ds
   */  
export interface ValidateSerialBeforeSelect_input{
   ds:Erp_Tablesets_InspParamTableset[],
}

export interface ValidateSerialBeforeSelect_output{
parameters : {
      /**  output parameters  */  
   notEnoughSerials:string,
   totSNReq:number,
}
}

   /** Required : 
      @param ds
      @param relatedRowID
      @param inSpecID
      @param inSpecRevNum
      @param inInspPlanPartNum
      @param inInspPlanRevNum
   */  
export interface buildRetrieveValues_input{
   ds:Erp_Tablesets_InspParamTableset[],
      /**  RowID of the InspResults record.  */  
   relatedRowID:string,
      /**  The specification ID  */  
   inSpecID:string,
      /**  The specification revision number  */  
   inSpecRevNum:string,
      /**  The inspection plan part number  */  
   inInspPlanPartNum:string,
      /**  The inspection plan revision number  */  
   inInspPlanRevNum:string,
}

export interface buildRetrieveValues_output{
   returnObj:any,      //schema had no properties on an object.
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InspParamTableset[],
}
}

