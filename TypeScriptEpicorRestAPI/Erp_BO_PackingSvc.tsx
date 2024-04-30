import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PackingSvc
// Description: Packing Data Set
// Version: v1
*/ 



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
   Description: Get Packings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Packings
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PackingRow
   */  
export function get_Packings(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PackingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/Packings", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PackingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Packings
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PackingRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PackingRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Packings(requestBody:Erp_Tablesets_PackingRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/Packings", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the Packing item
   Description: Calls GetByID to retrieve the Packing item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Packing
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PkgCode Desc: PkgCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PackingRow
   */  
export function get_Packings_Company_PkgCode(Company:string, PkgCode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PackingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/Packings(" + Company + "," + PkgCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_PackingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Packing for the service
   Description: Calls UpdateExt to update Packing. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Packing
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PkgCode Desc: PkgCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PackingRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Packings_Company_PkgCode(Company:string, PkgCode:string, requestBody:Erp_Tablesets_PackingRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/Packings(" + Company + "," + PkgCode + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete Packing item
   Description: Call UpdateExt to delete Packing item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Packing
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PkgCode Desc: PkgCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Packings_Company_PkgCode(Company:string, PkgCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/Packings(" + Company + "," + PkgCode + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
   Description: Get PackingPlants items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PackingPlants1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PkgCode Desc: PkgCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PackingPlantRow
   */  
export function get_Packings_Company_PkgCode_PackingPlants(Company:string, PkgCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PackingPlantRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/Packings(" + Company + "," + PkgCode + ")/PackingPlants", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PackingPlantRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PackingPlant item
   Description: Calls GetByID to retrieve the PackingPlant item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PackingPlant1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PkgCode Desc: PkgCode   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PackingPlantRow
   */  
export function get_Packings_Company_PkgCode_PackingPlants_Company_PkgCode_Plant(Company:string, PkgCode:string, Plant:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PackingPlantRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/Packings(" + Company + "," + PkgCode + ")/PackingPlants(" + Company + "," + PkgCode + "," + Plant + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_PackingPlantRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PackingShipToes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PackingShipToes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PkgCode Desc: PkgCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PackingShipToRow
   */  
export function get_Packings_Company_PkgCode_PackingShipToes(Company:string, PkgCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PackingShipToRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/Packings(" + Company + "," + PkgCode + ")/PackingShipToes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PackingShipToRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PackingShipTo item
   Description: Calls GetByID to retrieve the PackingShipTo item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PackingShipTo1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PkgCode Desc: PkgCode   Required: True   Allow empty value : True
      @param ShipToSeq Desc: ShipToSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PackingShipToRow
   */  
export function get_Packings_Company_PkgCode_PackingShipToes_Company_PkgCode_ShipToSeq(Company:string, PkgCode:string, ShipToSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PackingShipToRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/Packings(" + Company + "," + PkgCode + ")/PackingShipToes(" + Company + "," + PkgCode + "," + ShipToSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_PackingShipToRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PackingPlants items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PackingPlants
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PackingPlantRow
   */  
export function get_PackingPlants(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PackingPlantRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/PackingPlants", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PackingPlantRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PackingPlants
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PackingPlantRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PackingPlantRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PackingPlants(requestBody:Erp_Tablesets_PackingPlantRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/PackingPlants", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PackingPlant item
   Description: Calls GetByID to retrieve the PackingPlant item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PackingPlant
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PkgCode Desc: PkgCode   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PackingPlantRow
   */  
export function get_PackingPlants_Company_PkgCode_Plant(Company:string, PkgCode:string, Plant:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PackingPlantRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/PackingPlants(" + Company + "," + PkgCode + "," + Plant + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_PackingPlantRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PackingPlant for the service
   Description: Calls UpdateExt to update PackingPlant. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PackingPlant
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PkgCode Desc: PkgCode   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PackingPlantRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PackingPlants_Company_PkgCode_Plant(Company:string, PkgCode:string, Plant:string, requestBody:Erp_Tablesets_PackingPlantRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/PackingPlants(" + Company + "," + PkgCode + "," + Plant + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete PackingPlant item
   Description: Call UpdateExt to delete PackingPlant item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PackingPlant
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PkgCode Desc: PkgCode   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PackingPlants_Company_PkgCode_Plant(Company:string, PkgCode:string, Plant:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/PackingPlants(" + Company + "," + PkgCode + "," + Plant + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
   Description: Get PackingShipToes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PackingShipToes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PackingShipToRow
   */  
export function get_PackingShipToes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PackingShipToRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/PackingShipToes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PackingShipToRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PackingShipToes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PackingShipToRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PackingShipToRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PackingShipToes(requestBody:Erp_Tablesets_PackingShipToRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/PackingShipToes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PackingShipTo item
   Description: Calls GetByID to retrieve the PackingShipTo item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PackingShipTo
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PkgCode Desc: PkgCode   Required: True   Allow empty value : True
      @param ShipToSeq Desc: ShipToSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PackingShipToRow
   */  
export function get_PackingShipToes_Company_PkgCode_ShipToSeq(Company:string, PkgCode:string, ShipToSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PackingShipToRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/PackingShipToes(" + Company + "," + PkgCode + "," + ShipToSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_PackingShipToRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PackingShipTo for the service
   Description: Calls UpdateExt to update PackingShipTo. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PackingShipTo
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PkgCode Desc: PkgCode   Required: True   Allow empty value : True
      @param ShipToSeq Desc: ShipToSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PackingShipToRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PackingShipToes_Company_PkgCode_ShipToSeq(Company:string, PkgCode:string, ShipToSeq:string, requestBody:Erp_Tablesets_PackingShipToRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/PackingShipToes(" + Company + "," + PkgCode + "," + ShipToSeq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete PackingShipTo item
   Description: Call UpdateExt to delete PackingShipTo item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PackingShipTo
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PkgCode Desc: PkgCode   Required: True   Allow empty value : True
      @param ShipToSeq Desc: ShipToSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PackingShipToes_Company_PkgCode_ShipToSeq(Company:string, PkgCode:string, ShipToSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/PackingShipToes(" + Company + "," + PkgCode + "," + ShipToSeq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PackingListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PackingListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PackingListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClausePacking:string, whereClausePackingPlant:string, whereClausePackingShipTo:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePacking!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePacking=" + whereClausePacking
   }
   if(typeof whereClausePackingPlant!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePackingPlant=" + whereClausePackingPlant
   }
   if(typeof whereClausePackingShipTo!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePackingShipTo=" + whereClausePackingShipTo
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

   return (new Promise<GetRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRows_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(pkgCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof pkgCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pkgCode=" + pkgCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetByID_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPackingList
   Description: Retrieve a packing list for combo by part number. If part is not specified then it return all packing codes.
   OperationID: GetPackingList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPackingList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackingList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPackingList(requestBody:GetPackingList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPackingList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/GetPackingList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPackingList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPackingByPart
   Description: Purpose:     Used by combo to retrieve package codes by part and plant
Parameters:  whereclause
Notes:
///<param name="packingPlantWhereClause">Where Clause</param>
   OperationID: GetPackingByPart
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPackingByPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackingByPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPackingByPart(requestBody:GetPackingByPart_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPackingByPart_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/GetPackingByPart", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPackingByPart_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePartNum
   Description: Purpose:
Parameters:  none
Notes:
///<param name="ipPartNum">Part Number</param>
/// <param name="ds">Packing dataset</param>
   OperationID: OnChangePartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePartNum(requestBody:OnChangePartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/OnChangePartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeCustomerCustID
   Description: Update Customer information when the Customer is changed.
   OperationID: OnChangeCustomerCustID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeCustomerCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCustomerCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCustomerCustID(requestBody:OnChangeCustomerCustID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeCustomerCustID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/OnChangeCustomerCustID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeCustomerCustID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeShipToID
   Description: Update PackingShipTo information with values from the Ship To when the Ship To is changed.
   OperationID: OnChangeShipToID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeShipToID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeShipToID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeShipToID(requestBody:OnChangeShipToID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeShipToID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/OnChangeShipToID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeShipToID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPackingRecords
   Description: Used to retrieve Packing, PackingPlant and PackingShipTo records for the current plant.
<returns>Packing Tableset</returns><param name="pkgWClause" type="string">WhereClause for Packing table</param><param name="pkgPlantWClause" type="string">WhereClause for PackingPlant table</param><param name="pkgShipToWClause" type="string">WhereClause for PackingShipTo table</param><param name="table" type="string">Search form will display records from this table</param><param name="pageSize">Page size</param><param name="absolutePage">Absolute page</param><param name="morePages">More Pages</param>
   OperationID: GetPackingRecords
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPackingRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackingRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPackingRecords(requestBody:GetPackingRecords_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPackingRecords_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/GetPackingRecords", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPackingRecords_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPacking
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPacking
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPacking_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPacking_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPacking(requestBody:GetNewPacking_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPacking_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/GetNewPacking", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPacking_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPackingPlant
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPackingPlant
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPackingPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPackingPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPackingPlant(requestBody:GetNewPackingPlant_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPackingPlant_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/GetNewPackingPlant", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPackingPlant_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPackingShipTo
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPackingShipTo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPackingShipTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPackingShipTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPackingShipTo(requestBody:GetNewPackingShipTo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPackingShipTo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/GetNewPackingShipTo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPackingShipTo_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:DeleteByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DeleteByID_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetBySysRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetBySysRowID_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetBySysRowIDs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetBySysRowIDs_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:Update_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Update_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Update_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:UpdateExt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateExt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateExt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PackingListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PackingListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PackingPlantRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PackingPlantRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PackingRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PackingRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PackingShipToRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PackingShipToRow,
}

export interface Erp_Tablesets_PackingListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique packaging code assigned by the user. For example - box, skid, drum...etc.  */  
   "PkgCode":string,
      /**  Full description of Packing Code.  */  
   "Description":string,
      /**  Length dimension for this package code  */  
   "PkgLength":number,
      /**  Width dimension for this package code  */  
   "PkgWidth":number,
      /**  Height dimension for this package code  */  
   "PkgHeight":number,
      /**  Determines whether or not the packaging length is predefined or if users are able to enter a different length than what is specified on this record.  A zero indicates the length is prompted.  A one indicates the length specified on this record is the value used.  */  
   "PromptSetLength":number,
      /**  Determines whether or not the packaging width is predefined or if users are able to enter a different width than what is specified on this record.  A zero indicates the width is prompted.  A one indicates the width specified on this record is the value used.  */  
   "PromptSetWidth":number,
      /**  Determines whether or not the packaging height is predefined or if users are able to enter a different height than what is specified on this record.  A zero indicates the height is prompted.  A one indicates the height specified on this record is the value used.  */  
   "PromptSetHeight":number,
      /**   Unit of measure used to qualify the PkgLength, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  */  
   "PkgSizeUOM":string,
      /**  Serialized  */  
   "Serialized":boolean,
      /**  Returnable  */  
   "Returnable":boolean,
      /**  If defined will override the extension digit at the company level. The extension digit is used to increase the capacity of the SSCC. It is assigned by the company that constructs the SSCC. Sometimes is used to identify the Package Type (P).  0=Case or carton. 1=Pallet (Larger than a case). 2=Container (larger than a pallet). 3=Undefined. 4=Internal company use. 5-8=Reserved. 9=Variable container.  */  
   "ExtensionDigit":number,
      /**  Tare Weight.  */  
   "Weight":number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  when creating new records.  */  
   "WeightUOM":string,
      /**  Determines whether or not the packaging weight is predefined or if users are able to enter a different weight than what is specified on this record.  A zero indicates the weight is prompted.  A one indicates the weight specified on this record is the value used.  */  
   "PromptSetWeight":number,
      /**  Marks this Packing as global, available to be sent out to other companies.  */  
   "GlobalPacking":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PackingPlantRow{
      /**  Company  */  
   "Company":string,
      /**  Unique packaging code assigned by the user.  */  
   "PkgCode":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  The Internal PartNum for the Package Code.  */  
   "PkgCodePartNum":string,
      /**  If yes then the system will track the returnable container.  If yes the Internal Part Number must be defined.  */  
   "TrackReturnable":boolean,
      /**  Reason Code used by the Container Return Receipt transaction when the package is returned.  */  
   "TrackingReasonCodeIn":string,
      /**  Reason Code used when a Quantity Adjustment is triggered when the package is shipped.  */  
   "TrackingReasonCodeOut":string,
      /**  If yes then the system will track the expendable container.  */  
   "TrackExpendable":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  A flag used to indicate if the user is not authorized for the PackingPlant.Plant - to prevent updates in the UI.  */  
   "PlantInvalidForUser":boolean,
   "BitFlag":number,
   "InternalPartSellingFactor":number,
   "InternalPartPartDescription":string,
   "InternalPartPricePerCode":string,
   "InternalPartTrackDimension":boolean,
   "InternalPartTrackLots":boolean,
   "InternalPartIUM":string,
   "InternalPartSalesUM":string,
   "InternalPartTrackSerialNum":boolean,
   "PackingDescription":string,
   "PlantName":string,
   "ReasonInDescription":string,
   "ReasonOutDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PackingRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique packaging code assigned by the user. For example - box, skid, drum...etc.  */  
   "PkgCode":string,
      /**  Full description of Packing Code.  */  
   "Description":string,
      /**  Length dimension for this package code  */  
   "PkgLength":number,
      /**  Width dimension for this package code  */  
   "PkgWidth":number,
      /**  Height dimension for this package code  */  
   "PkgHeight":number,
      /**  Determines whether or not the packaging length is predefined or if users are able to enter a different length than what is specified on this record.  A zero indicates the length is prompted.  A one indicates the length specified on this record is the value used.  */  
   "PromptSetLength":number,
      /**  Determines whether or not the packaging width is predefined or if users are able to enter a different width than what is specified on this record.  A zero indicates the width is prompted.  A one indicates the width specified on this record is the value used.  */  
   "PromptSetWidth":number,
      /**  Determines whether or not the packaging height is predefined or if users are able to enter a different height than what is specified on this record.  A zero indicates the height is prompted.  A one indicates the height specified on this record is the value used.  */  
   "PromptSetHeight":number,
      /**   Unit of measure used to qualify the PkgLength, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  */  
   "PkgSizeUOM":string,
      /**  Serialized  */  
   "Serialized":boolean,
      /**  Returnable  */  
   "Returnable":boolean,
      /**  If defined will override the extension digit at the company level. The extension digit is used to increase the capacity of the SSCC. It is assigned by the company that constructs the SSCC. Sometimes is used to identify the Package Type (P).  0=Case or carton. 1=Pallet (Larger than a case). 2=Container (larger than a pallet). 3=Undefined. 4=Internal company use. 5-8=Reserved. 9=Variable container.  */  
   "ExtensionDigit":number,
      /**  Tare Weight.  */  
   "Weight":number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  when creating new records.  */  
   "WeightUOM":string,
      /**  Determines whether or not the packaging weight is predefined or if users are able to enter a different weight than what is specified on this record.  A zero indicates the weight is prompted.  A one indicates the weight specified on this record is the value used.  */  
   "PromptSetWeight":number,
      /**  Marks this Packing as global, available to be sent out to other companies.  */  
   "GlobalPacking":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Package Type Code assigned by the user  */  
   "PkgTypeCode":string,
      /**  Maximum Stack  */  
   "MaximumStack":number,
      /**  Maximum Gross Weight not to exceed for both the package and its contents.  */  
   "MaximumWeight":number,
      /**  Volume unit of measure.  */  
   "VolumeUOM":string,
      /**  Internal Volume.  */  
   "InternalVolume":number,
      /**  External Volume  */  
   "ExternalVolume":number,
      /**  Indicates if the package code has been inactivated.  */  
   "Inactive":boolean,
      /**  Expendable  */  
   "Expendable":boolean,
      /**  Internal length dimension for this package code.  */  
   "PkgInternalLength":number,
      /**  Internal width dimension for this package code.  */  
   "PkgInternalWidth":number,
      /**  Internal height dimension for this package code.  */  
   "PkgInternalHeight":number,
      /**  Determines whether or not the packaging length is predefined or if users are able to enter a different length than what is specified on this record.  A zero indicates the length is prompted.  A one indicates the length specified on this record is the value used.  */  
   "InternalPromptSetLength":number,
      /**  Determines whether or not the packaging width is predefined or if users are able to enter a different width than what is specified on this record.  A zero indicates the width is prompted.  A one indicates the width specified on this record is the value used.  */  
   "InternalPromptSetWidth":number,
      /**  Determines whether or not the packaging height is predefined or if users are able to enter a different width than what is specified on this record.  A zero indicates the width is prompted.  A one indicates the width specified on this record is the value used.  */  
   "InternalPromptSetHeight":number,
      /**  Unique package material type code assigned by the user.  */  
   "PkgMtlTypeCode":string,
      /**  Indicates if the record is active or not. Default is true.  */  
   "Active":boolean,
      /**  Flag to be used internally for row rules for whether to allow the Packing Code to be set to inactive.  */  
   "EnableInactive":boolean,
   "BitFlag":number,
   "PackingMtlTypePkgMtlTypeCodeDesc":string,
   "PackingTypePkgTypeDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PackingShipToRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique packaging code assigned by the user.  */  
   "PkgCode":string,
      /**  ShipToSeq  */  
   "ShipToSeq":number,
      /**  Customer Number.  */  
   "CustNum":number,
      /**  Ship To Number.  */  
   "ShipToNum":string,
      /**  The ship to specified container part ID.  */  
   "ShipToContainerPartID":string,
      /**  The ship to specified container part description.  */  
   "ShipToContainerPartDesc":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Holds "~" delimited name and address data from the ShipTo record.  */  
   "ShipToAddressList":string,
   "PkgCodePartNum":string,
   "CustID":string,
      /**  The name and address data from the ShipTo record formatted.  */  
   "ShipToAddressFormatted":string,
   "BitFlag":number,
   "CustomerBTName":string,
   "CustomerName":string,
   "CustomerCustID":string,
   "PackingDescription":string,
   "ShipToName":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param pkgCode
   */  
export interface DeleteByID_input{
   pkgCode:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PackingListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique packaging code assigned by the user. For example - box, skid, drum...etc.  */  
   PkgCode:string,
      /**  Full description of Packing Code.  */  
   Description:string,
      /**  Length dimension for this package code  */  
   PkgLength:number,
      /**  Width dimension for this package code  */  
   PkgWidth:number,
      /**  Height dimension for this package code  */  
   PkgHeight:number,
      /**  Determines whether or not the packaging length is predefined or if users are able to enter a different length than what is specified on this record.  A zero indicates the length is prompted.  A one indicates the length specified on this record is the value used.  */  
   PromptSetLength:number,
      /**  Determines whether or not the packaging width is predefined or if users are able to enter a different width than what is specified on this record.  A zero indicates the width is prompted.  A one indicates the width specified on this record is the value used.  */  
   PromptSetWidth:number,
      /**  Determines whether or not the packaging height is predefined or if users are able to enter a different height than what is specified on this record.  A zero indicates the height is prompted.  A one indicates the height specified on this record is the value used.  */  
   PromptSetHeight:number,
      /**   Unit of measure used to qualify the PkgLength, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  */  
   PkgSizeUOM:string,
      /**  Serialized  */  
   Serialized:boolean,
      /**  Returnable  */  
   Returnable:boolean,
      /**  If defined will override the extension digit at the company level. The extension digit is used to increase the capacity of the SSCC. It is assigned by the company that constructs the SSCC. Sometimes is used to identify the Package Type (P).  0=Case or carton. 1=Pallet (Larger than a case). 2=Container (larger than a pallet). 3=Undefined. 4=Internal company use. 5-8=Reserved. 9=Variable container.  */  
   ExtensionDigit:number,
      /**  Tare Weight.  */  
   Weight:number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  when creating new records.  */  
   WeightUOM:string,
      /**  Determines whether or not the packaging weight is predefined or if users are able to enter a different weight than what is specified on this record.  A zero indicates the weight is prompted.  A one indicates the weight specified on this record is the value used.  */  
   PromptSetWeight:number,
      /**  Marks this Packing as global, available to be sent out to other companies.  */  
   GlobalPacking:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PackingListTableset{
   PackingList:Erp_Tablesets_PackingListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PackingPlantRow{
      /**  Company  */  
   Company:string,
      /**  Unique packaging code assigned by the user.  */  
   PkgCode:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  The Internal PartNum for the Package Code.  */  
   PkgCodePartNum:string,
      /**  If yes then the system will track the returnable container.  If yes the Internal Part Number must be defined.  */  
   TrackReturnable:boolean,
      /**  Reason Code used by the Container Return Receipt transaction when the package is returned.  */  
   TrackingReasonCodeIn:string,
      /**  Reason Code used when a Quantity Adjustment is triggered when the package is shipped.  */  
   TrackingReasonCodeOut:string,
      /**  If yes then the system will track the expendable container.  */  
   TrackExpendable:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  A flag used to indicate if the user is not authorized for the PackingPlant.Plant - to prevent updates in the UI.  */  
   PlantInvalidForUser:boolean,
   BitFlag:number,
   InternalPartSellingFactor:number,
   InternalPartPartDescription:string,
   InternalPartPricePerCode:string,
   InternalPartTrackDimension:boolean,
   InternalPartTrackLots:boolean,
   InternalPartIUM:string,
   InternalPartSalesUM:string,
   InternalPartTrackSerialNum:boolean,
   PackingDescription:string,
   PlantName:string,
   ReasonInDescription:string,
   ReasonOutDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PackingRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique packaging code assigned by the user. For example - box, skid, drum...etc.  */  
   PkgCode:string,
      /**  Full description of Packing Code.  */  
   Description:string,
      /**  Length dimension for this package code  */  
   PkgLength:number,
      /**  Width dimension for this package code  */  
   PkgWidth:number,
      /**  Height dimension for this package code  */  
   PkgHeight:number,
      /**  Determines whether or not the packaging length is predefined or if users are able to enter a different length than what is specified on this record.  A zero indicates the length is prompted.  A one indicates the length specified on this record is the value used.  */  
   PromptSetLength:number,
      /**  Determines whether or not the packaging width is predefined or if users are able to enter a different width than what is specified on this record.  A zero indicates the width is prompted.  A one indicates the width specified on this record is the value used.  */  
   PromptSetWidth:number,
      /**  Determines whether or not the packaging height is predefined or if users are able to enter a different height than what is specified on this record.  A zero indicates the height is prompted.  A one indicates the height specified on this record is the value used.  */  
   PromptSetHeight:number,
      /**   Unit of measure used to qualify the PkgLength, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  */  
   PkgSizeUOM:string,
      /**  Serialized  */  
   Serialized:boolean,
      /**  Returnable  */  
   Returnable:boolean,
      /**  If defined will override the extension digit at the company level. The extension digit is used to increase the capacity of the SSCC. It is assigned by the company that constructs the SSCC. Sometimes is used to identify the Package Type (P).  0=Case or carton. 1=Pallet (Larger than a case). 2=Container (larger than a pallet). 3=Undefined. 4=Internal company use. 5-8=Reserved. 9=Variable container.  */  
   ExtensionDigit:number,
      /**  Tare Weight.  */  
   Weight:number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  when creating new records.  */  
   WeightUOM:string,
      /**  Determines whether or not the packaging weight is predefined or if users are able to enter a different weight than what is specified on this record.  A zero indicates the weight is prompted.  A one indicates the weight specified on this record is the value used.  */  
   PromptSetWeight:number,
      /**  Marks this Packing as global, available to be sent out to other companies.  */  
   GlobalPacking:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Package Type Code assigned by the user  */  
   PkgTypeCode:string,
      /**  Maximum Stack  */  
   MaximumStack:number,
      /**  Maximum Gross Weight not to exceed for both the package and its contents.  */  
   MaximumWeight:number,
      /**  Volume unit of measure.  */  
   VolumeUOM:string,
      /**  Internal Volume.  */  
   InternalVolume:number,
      /**  External Volume  */  
   ExternalVolume:number,
      /**  Indicates if the package code has been inactivated.  */  
   Inactive:boolean,
      /**  Expendable  */  
   Expendable:boolean,
      /**  Internal length dimension for this package code.  */  
   PkgInternalLength:number,
      /**  Internal width dimension for this package code.  */  
   PkgInternalWidth:number,
      /**  Internal height dimension for this package code.  */  
   PkgInternalHeight:number,
      /**  Determines whether or not the packaging length is predefined or if users are able to enter a different length than what is specified on this record.  A zero indicates the length is prompted.  A one indicates the length specified on this record is the value used.  */  
   InternalPromptSetLength:number,
      /**  Determines whether or not the packaging width is predefined or if users are able to enter a different width than what is specified on this record.  A zero indicates the width is prompted.  A one indicates the width specified on this record is the value used.  */  
   InternalPromptSetWidth:number,
      /**  Determines whether or not the packaging height is predefined or if users are able to enter a different width than what is specified on this record.  A zero indicates the width is prompted.  A one indicates the width specified on this record is the value used.  */  
   InternalPromptSetHeight:number,
      /**  Unique package material type code assigned by the user.  */  
   PkgMtlTypeCode:string,
      /**  Indicates if the record is active or not. Default is true.  */  
   Active:boolean,
      /**  Flag to be used internally for row rules for whether to allow the Packing Code to be set to inactive.  */  
   EnableInactive:boolean,
   BitFlag:number,
   PackingMtlTypePkgMtlTypeCodeDesc:string,
   PackingTypePkgTypeDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PackingShipToRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique packaging code assigned by the user.  */  
   PkgCode:string,
      /**  ShipToSeq  */  
   ShipToSeq:number,
      /**  Customer Number.  */  
   CustNum:number,
      /**  Ship To Number.  */  
   ShipToNum:string,
      /**  The ship to specified container part ID.  */  
   ShipToContainerPartID:string,
      /**  The ship to specified container part description.  */  
   ShipToContainerPartDesc:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Holds "~" delimited name and address data from the ShipTo record.  */  
   ShipToAddressList:string,
   PkgCodePartNum:string,
   CustID:string,
      /**  The name and address data from the ShipTo record formatted.  */  
   ShipToAddressFormatted:string,
   BitFlag:number,
   CustomerBTName:string,
   CustomerName:string,
   CustomerCustID:string,
   PackingDescription:string,
   ShipToName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PackingTableset{
   Packing:Erp_Tablesets_PackingRow[],
   PackingPlant:Erp_Tablesets_PackingPlantRow[],
   PackingShipTo:Erp_Tablesets_PackingShipToRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPackingTableset{
   Packing:Erp_Tablesets_PackingRow[],
   PackingPlant:Erp_Tablesets_PackingPlantRow[],
   PackingShipTo:Erp_Tablesets_PackingShipToRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param pkgCode
   */  
export interface GetByID_input{
   pkgCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PackingTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PackingTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PackingTableset[],
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
   returnObj:Erp_Tablesets_PackingListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param pkgCode
   */  
export interface GetNewPackingPlant_input{
   ds:Erp_Tablesets_PackingTableset[],
   pkgCode:string,
}

export interface GetNewPackingPlant_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackingTableset,
}
}

   /** Required : 
      @param ds
      @param pkgCode
   */  
export interface GetNewPackingShipTo_input{
   ds:Erp_Tablesets_PackingTableset[],
   pkgCode:string,
}

export interface GetNewPackingShipTo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackingTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPacking_input{
   ds:Erp_Tablesets_PackingTableset[],
}

export interface GetNewPacking_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackingTableset,
}
}

   /** Required : 
      @param packingPlantWhereClause
   */  
export interface GetPackingByPart_input{
   packingPlantWhereClause:string,
}

export interface GetPackingByPart_output{
   returnObj:Erp_Tablesets_PackingListTableset[],
}

   /** Required : 
      @param partNum
   */  
export interface GetPackingList_input{
   partNum:string,
}

export interface GetPackingList_output{
   returnObj:Erp_Tablesets_PackingListTableset[],
}

   /** Required : 
      @param pkgWClause
      @param pkgPlantWClause
      @param pkgShipToWClause
      @param table
      @param pageSize
      @param absolutePage
   */  
export interface GetPackingRecords_input{
   pkgWClause:string,
   pkgPlantWClause:string,
   pkgShipToWClause:string,
   table:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetPackingRecords_output{
   returnObj:Erp_Tablesets_PackingTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClausePacking
      @param whereClausePackingPlant
      @param whereClausePackingShipTo
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePacking:string,
   whereClausePackingPlant:string,
   whereClausePackingShipTo:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PackingTableset[],
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
      @param ipCustId
      @param ds
   */  
export interface OnChangeCustomerCustID_input{
      /**  The Customer ID  */  
   ipCustId:string,
   ds:Erp_Tablesets_PackingTableset[],
}

export interface OnChangeCustomerCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackingTableset,
}
}

   /** Required : 
      @param ipPartNum
      @param ds
   */  
export interface OnChangePartNum_input{
   ipPartNum:string,
   ds:Erp_Tablesets_PackingTableset[],
}

export interface OnChangePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackingTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeShipToID_input{
   ds:Erp_Tablesets_PackingTableset[],
}

export interface OnChangeShipToID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackingTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPackingTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPackingTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PackingTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackingTableset,
}
}

