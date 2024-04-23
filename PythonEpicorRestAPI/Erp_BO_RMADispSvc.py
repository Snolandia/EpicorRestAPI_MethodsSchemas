import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.RMADispSvc
# Description: RMA Disposition Business Object
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_RMADisps(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RMADisps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RMADisps
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RMADispRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/RMADisps",headers=creds) as resp:
           return await resp.json()

async def post_RMADisps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RMADisps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RMADispRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RMADispRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/RMADisps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RMADisps_Company_RMANum_RMALine_RMAReceipt(Company, RMANum, RMALine, RMAReceipt, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RMADisp item
   Description: Calls GetByID to retrieve the RMADisp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RMADisp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param RMALine: Desc: RMALine   Required: True
      :param RMAReceipt: Desc: RMAReceipt   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RMADispRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/RMADisps(" + Company + "," + RMANum + "," + RMALine + "," + RMAReceipt + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RMADisps_Company_RMANum_RMALine_RMAReceipt(Company, RMANum, RMALine, RMAReceipt, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RMADisp for the service
   Description: Calls UpdateExt to update RMADisp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RMADisp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param RMALine: Desc: RMALine   Required: True
      :param RMAReceipt: Desc: RMAReceipt   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RMADispRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/RMADisps(" + Company + "," + RMANum + "," + RMALine + "," + RMAReceipt + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RMADisps_Company_RMANum_RMALine_RMAReceipt(Company, RMANum, RMALine, RMAReceipt, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RMADisp item
   Description: Call UpdateExt to delete RMADisp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RMADisp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param RMALine: Desc: RMALine   Required: True
      :param RMAReceipt: Desc: RMAReceipt   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/RMADisps(" + Company + "," + RMANum + "," + RMALine + "," + RMAReceipt + ")",headers=creds) as resp:
           return await resp.json()

async def get_RMADisps_Company_RMANum_RMALine_RMAReceipt_RMADisps(Company, RMANum, RMALine, RMAReceipt, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RMADisps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RMADisps1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param RMALine: Desc: RMALine   Required: True
      :param RMAReceipt: Desc: RMAReceipt   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RMADispRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/RMADisps(" + Company + "," + RMANum + "," + RMALine + "," + RMAReceipt + ")/RMADisps",headers=creds) as resp:
           return await resp.json()

async def get_RMADisps_Company_RMANum_RMALine_RMAReceipt_RMADisps_Company_RMANum_RMALine_RMAReceipt(Company, RMANum, RMALine, RMAReceipt, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RMADisp item
   Description: Calls GetByID to retrieve the RMADisp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RMADisp1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param RMALine: Desc: RMALine   Required: True
      :param RMAReceipt: Desc: RMAReceipt   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RMADispRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/RMADisps(" + Company + "," + RMANum + "," + RMALine + "," + RMAReceipt + ")/RMADisps(" + Company + "," + RMANum + "," + RMALine + "," + RMAReceipt + ")",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LegalNumGenOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumGenOpts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/LegalNumGenOpts",headers=creds) as resp:
           return await resp.json()

async def post_LegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/LegalNumGenOpts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LegalNumGenOpt item
   Description: Calls GetByID to retrieve the LegalNumGenOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LegalNumGenOpt for the service
   Description: Calls UpdateExt to update LegalNumGenOpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LegalNumGenOpt item
   Description: Call UpdateExt to delete LegalNumGenOpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
           return await resp.json()

async def get_SelectedSerialNumbers(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SelectedSerialNumbers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SelectedSerialNumbers
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SelectedSerialNumbersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/SelectedSerialNumbers",headers=creds) as resp:
           return await resp.json()

async def post_SelectedSerialNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/SelectedSerialNumbers", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SelectedSerialNumber item
   Description: Calls GetByID to retrieve the SelectedSerialNumber item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SelectedSerialNumber for the service
   Description: Calls UpdateExt to update SelectedSerialNumber. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SelectedSerialNumber item
   Description: Call UpdateExt to delete SelectedSerialNumber item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def get_SerialNumberSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SerialNumberSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SerialNumberSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SerialNumberSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/SerialNumberSearches",headers=creds) as resp:
           return await resp.json()

async def post_SerialNumberSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SerialNumberSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SerialNumberSearchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SerialNumberSearchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/SerialNumberSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SerialNumberSearches_ProcessToken(ProcessToken, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SerialNumberSearch item
   Description: Calls GetByID to retrieve the SerialNumberSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SerialNumberSearch
      :param ProcessToken: Desc: ProcessToken   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SerialNumberSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/SerialNumberSearches(" + ProcessToken + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SerialNumberSearches_ProcessToken(ProcessToken, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SerialNumberSearch for the service
   Description: Calls UpdateExt to update SerialNumberSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SerialNumberSearch
      :param ProcessToken: Desc: ProcessToken   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SerialNumberSearchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/SerialNumberSearches(" + ProcessToken + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SerialNumberSearches_ProcessToken(ProcessToken, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SerialNumberSearch item
   Description: Call UpdateExt to delete SerialNumberSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SerialNumberSearch
      :param ProcessToken: Desc: ProcessToken   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/SerialNumberSearches(" + ProcessToken + ")",headers=creds) as resp:
           return await resp.json()

async def get_SNFormats(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SNFormats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SNFormats
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SNFormatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/SNFormats",headers=creds) as resp:
           return await resp.json()

async def post_SNFormats(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SNFormats
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/SNFormats", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SNFormat item
   Description: Calls GetByID to retrieve the SNFormat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SNFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SNFormat for the service
   Description: Calls UpdateExt to update SNFormat. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SNFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SNFormat item
   Description: Call UpdateExt to delete SNFormat item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SNFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RMARcptListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseRMARcpt, whereClauseRMADisp, whereClauseLegalNumGenOpts, whereClauseSelectedSerialNumbers, whereClauseSerialNumberSearch, whereClauseSNFormat, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRMARcpt=" + whereClauseRMARcpt
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRMADisp=" + whereClauseRMADisp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLegalNumGenOpts=" + whereClauseLegalNumGenOpts
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSelectedSerialNumbers=" + whereClauseSelectedSerialNumbers
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSerialNumberSearch=" + whereClauseSerialNumberSearch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSNFormat=" + whereClauseSNFormat
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(rmANum, rmALine, rmAReceipt, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "rmANum=" + rmANum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "rmALine=" + rmALine
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "rmAReceipt=" + rmAReceipt

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeBinNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeBinNum
   Description: Method to call when changing the bin number.  Provides the bin description.
   OperationID: ChangeBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDispType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDispType
   Description: Method to call when changing the Disposition Type.  Provides default values for the RMADisp record.
   OperationID: ChangeDispType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDispType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDispType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeJob
   Description: Method to call when changing the job number.  Provides default values for the RMADisp record.
   OperationID: ChangeJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeToBinNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeToBinNum
   Description: Method to call when changing the to bin number.  Provides the bin description.
   OperationID: ChangeToBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeToBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeToBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeToWarehouse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeToWarehouse
   Description: Method to call when changing the to warehouse, RMADisp.ToWareHouseCode if Request Move is checked
It will only affect the mtlqueue record "to" whs default. Provides default values for the RMADisp mtlqueue record.
   OperationID: ChangeToWarehouse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeToWarehouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeToWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeWarehouse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeWarehouse
   Description: Method to call when changing RMADisp.WarehouseCode (associated with the Disposition Warehouse).  Provides default values for the RMADisp record.
   OperationID: ChangeWarehouse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeWarehouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckClosedJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckClosedJob
   Description: This method checks to see if the job is closed.  Returns text of a question to
be asked of the user if it is.  This method should be called when entering a job number.
   OperationID: CheckClosedJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckClosedJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckClosedJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RMACanBeLinkedToJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RMACanBeLinkedToJob
   Description: This method checks to see if the job has already been linked to another RMA.  Returns text of a question to
be asked to user if wants to continue with half link.  This method should be called when entering a job number.
   OperationID: RMACanBeLinkedToJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RMACanBeLinkedToJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RMACanBeLinkedToJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPlanningContractBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPlanningContractBin
   Description: Method to check Contract bin.
   OperationID: CheckPlanningContractBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPlanningContractBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPlanningContractBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckWithInspResults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckWithInspResults
   Description: Method to check the Inspection Results Qty (EQM)
   OperationID: CheckWithInspResults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckWithInspResults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckWithInspResults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLegalNumGenOpts
   Description: Returns the legal number generation options.
   OperationID: GetLegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLegalNumGenOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegalNumGenOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartTranPKs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartTranPKs
   Description: Return Primary Keys for generated PartTran records.
   OperationID: GetPartTranPKs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartTranPKs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartTranPKs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectSerialNumbersParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Gets parameters required for launching Select Serial Numbers
   OperationID: GetSelectSerialNumbersParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectSerialNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectSerialNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDispQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDispQty
   Description: Purpose:     If Quantity is for FIFO/LOTFIFO part then a special logic will be called to
determine the FIFO layers to return and calculate the FIFO weighted average
for the RMADisp.
Parameters:  none
Notes:
<param name="ds">Epicor.Mfg.BO.RMADispDataSet</param><param name="proposedDispQty">The Disposition Quantity that the user entered.</param>
   OperationID: OnChangeDispQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDispQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDispQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOverrideCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOverrideCost
   Description: Purpose:
Parameters:  none
Notes:
<param name="ds">Epicor.Mfg.BO.RMADispDataSet</param><param name="ProposedOverride">Override Cost value that the user selected.</param>
   OperationID: OnChangeOverrideCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOverrideCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOverrideCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeUseCurrentCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeUseCurrentCost
   Description: Purpose:
Parameters:  none
Notes:
<param name="ds">Epicor.Mfg.BO.RMADispDataSet</param><param name="proposedUseCurrentCost">Use Current Cost value that the user selected.</param>
   OperationID: OnChangeUseCurrentCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeUseCurrentCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeUseCurrentCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSN(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSN
   Description: Validates that a single serial number is valid for this transaction
   OperationID: ValidateSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DisplayWarnMsg(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DisplayWarnMsg
   Description: DisplayWarnMsg
   OperationID: DisplayWarnMsg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DisplayWarnMsg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DisplayWarnMsg_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailTranDocTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailTranDocTypes
   OperationID: GetAvailTranDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRMARcpt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRMARcpt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRMARcpt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRMARcpt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRMARcpt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRMADisp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRMADisp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRMADisp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRMADisp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRMADisp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMADispRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RMADispRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMARcptListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RMARcptListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SNFormatRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialNumberSearchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SerialNumberSearchRow] = obj["value"]
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RMADispRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Material Authorization number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA Receipt  """  
      self.RMADisp1:int = obj["RMADisp1"]
      self.DispType:str = obj["DispType"]
      """   Every part received on an RMA that needs to be disposition is received to inspection.  So when dispositioning RMAs the parts are coming out of inspection.
Field that indicates the type of disposition:
INS-MFG - Issued to Mfg ( Job Material)
INS-STK -  Received into Stock (Inventory)
INS-REJ -  Failed  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """   Warehouse ID the item was received into.
NOTE: Applies only to "RMA-STK".  """  
      self.BinNum:str = obj["BinNum"]
      """   Warehouse Bin location in which the item was placed.
NOTE: Applies only to "RMA-STK".  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number to which item was issued.  Applies only to RMA-MFG  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job Assembly sequence to which item was issued.  Applies only to RMA-MFG  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Job Material number to which item was issued.  Applies only to RMA-MFG  """  
      self.DispComment:str = obj["DispComment"]
      """   Comments about the disposition of this item.  These will be copied to the JobMtl.MfgComment for RMA-MFG.
Comments for manufacturing about this material record.  These comments are printed on manufacturing reports, such as the router.  For valid Parts use the Part.MfgComment as a default. 
View as editor widget.  """  
      self.InspectorID:str = obj["InspectorID"]
      """  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  """  
      self.InspectedBy:str = obj["InspectedBy"]
      """  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  """  
      self.InspectedDate:str = obj["InspectedDate"]
      """  Date when item was inspected.  """  
      self.InspectedTime:int = obj["InspectedTime"]
      """   Time of day when inspection transaction was recorded.
(seconds since midnight format)  """  
      self.NonConfTranID:int = obj["NonConfTranID"]
      """  TranID of related NonConf record.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Provides a link to the Reason table.  """  
      self.DispQty:int = obj["DispQty"]
      """  Disposition Quantity.  """  
      self.DispQtyUOM:str = obj["DispQtyUOM"]
      """  Unit Of Measure.  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.RequestMove:bool = obj["RequestMove"]
      """  Material Queue Records will only be updated if the "Request Move" box is checked  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OverrideCosts:bool = obj["OverrideCosts"]
      """  If set to true the user can manually override the costs used for the RMA disposition  """  
      self.UseCurrentCost:bool = obj["UseCurrentCost"]
      """  If set to true the current costs will default for the RMA disposition.  """  
      self.ToBinNum:str = obj["ToBinNum"]
      """  The to bin for the RMA disposition  """  
      self.ToWareHouseCode:str = obj["ToWareHouseCode"]
      """  The to warehouse for the RMA disposition  """  
      self.SetReassignSNAsm:bool = obj["SetReassignSNAsm"]
      """  Flag used to designate if the serial numbers from the job material/subassembly can be reassigned as the serial number of the parent assembly (top assembly or n deep subassembly) being reworked using a job.  """  
      self.CreateCorrectiveAction:bool = obj["CreateCorrectiveAction"]
      self.UpdateCommentAndReasonOnly:bool = obj["UpdateCommentAndReasonOnly"]
      self.MaterialUnitCost:int = obj["MaterialUnitCost"]
      self.BurdenUnitCost:int = obj["BurdenUnitCost"]
      self.SubUnitCost:int = obj["SubUnitCost"]
      self.MaterialBurdenUnitCost:int = obj["MaterialBurdenUnitCost"]
      self.LaborUnitCost:int = obj["LaborUnitCost"]
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      self.EnableBin:bool = obj["EnableBin"]
      self.DispTypeDescription:str = obj["DispTypeDescription"]
      self.EnableInspectedBy:bool = obj["EnableInspectedBy"]
      self.PartNum:str = obj["PartNum"]
      """  PartNum from RMADtl.  """  
      self.EnableSN:bool = obj["EnableSN"]
      """  Flag to know if serial number is valid in this transaction.  """  
      self.RequestMoveLicense:bool = obj["RequestMoveLicense"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.EnableInspection:bool = obj["EnableInspection"]
      """  To enable/disable the Inspection Data button on UI  """  
      self.ToBinDesc:str = obj["ToBinDesc"]
      self.ToWareHouseDesc:str = obj["ToWareHouseDesc"]
      self.FSAServiceType:str = obj["FSAServiceType"]
      """  Serivce Type  """  
      self.FSATechnician:str = obj["FSATechnician"]
      """  Technician  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Determines if the RMA is synchronized with Epicor FSA application.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.DispTypeList:str = obj["DispTypeList"]
      """  List of valid Disp types  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.Plant:str = obj["Plant"]
      """  The plant that any warehouse being selected for RMADisp should come from.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.InspectedByName:str = obj["InspectedByName"]
      self.InspectorIDName:str = obj["InspectorIDName"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.ReasonCodeDescription:str = obj["ReasonCodeDescription"]
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      self.WareHouseCodeDescription:str = obj["WareHouseCodeDescription"]
      self.WhseBinDescription:str = obj["WhseBinDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RMARcptListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Authorization Number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line # of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA Receipt  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse ID the item was received into.  Normally this would be a "Inspection" type of warehouse.  """  
      self.BinNum:str = obj["BinNum"]
      """  Warehouse Bin location in which the received item was placed.  """  
      self.RcvDate:str = obj["RcvDate"]
      """  Receipt Date  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.OpenReceipt:bool = obj["OpenReceipt"]
      """  This is set to NO when the entire quantity has been accounted for in RMADisp.  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  The unit cost assigned to the return item.  This will actually be used to pass the cost value via the write trigger to the corresponding PartTran field. The system attempts to retrieve the cost from the last related "costed" shipment.  It's either the last shipment of the Order/Line, if given, or else it's the last shipment to the customer for this part.  If the shipment was from a job, and the shipment has not yet been costed then the system will attempt to calculate the proper costs using the Calculate COS logic found in program JCP80-GN.W.  The Qty X Unit Cost provides the amount that will be used to post to GL via the parttran record. The resulting G/L transactions are Debit to Inspection and Credit to "Cost of Returns".  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost of Returned Item.  (See MtlUnitCost)  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost of Returned Item.  (See MtlUnitCost)  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost of Returned Item.  (See MtlUnitCost)  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  The unit cost assigned to the return item.  This will actually be used to pass the cost value via the write trigger to the corresponding PartTran field. The system attempts to retrieve the cost from the last related "costed" shipment.  It's either the last shipment of the Order/Line, if given, or else it's the last shipment to the customer for this part.  If the shipment was from a job, and the shipment has not yet been costed then the system will attempt to calculate the proper costs using the Calculate COS logic found in program JCP80-GN.W.  The Qty X Unit Cost provides the amount that will be used to post to GL via the parttran record. The resulting G/L transactions are Debit to Inspection and Credit to "Cost of Returns".  """  
      self.Plant:str = obj["Plant"]
      """  The Site that this RMA receipt was received to.  This is set as from the "Current Site" at the time of receipt.  It will be used in the filtering of receipts in the Disposition process.  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.MtlMtlBurUnitCost:int = obj["MtlMtlBurUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  Quantity that has been received.  """  
      self.DisposedQty:int = obj["DisposedQty"]
      """  Quantity that has been dispositioned .  Cannot exceed ReceivedQty.  This is summation of the quantities from the supporting RMADisp records.  When DisposedQty = ReceivedQty the RMARcpt.OpenReceipt is set to NO.  """  
      self.CostUOM:str = obj["CostUOM"]
      """  Unit of measure that qualifies the unit costs.  """  
      self.ReceivedQtyUOM:str = obj["ReceivedQtyUOM"]
      """  Received Quantity unit of measure.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.RequestMove:bool = obj["RequestMove"]
      """  Material Queue Records will only be updated if the "Request Move" box is checked  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of the RMA line  """  
      self.EnableWarehouse:bool = obj["EnableWarehouse"]
      self.EnableBin:bool = obj["EnableBin"]
      self.CustomerName:str = obj["CustomerName"]
      self.PartRevisionNum:str = obj["PartRevisionNum"]
      self.EnableDelete:bool = obj["EnableDelete"]
      self.EnableUpdate:bool = obj["EnableUpdate"]
      self.CustNum:int = obj["CustNum"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      """  PartPartDescription  """  
      self.PartTrackLots:bool = obj["PartTrackLots"]
      """  PartTrackLots  """  
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      """  PartTrackSerialNum  """  
      self.ThisRcptQty:int = obj["ThisRcptQty"]
      """  The receipt quantity displayed in the RMADtl.ReturnQty.  """  
      self.ThisRcptQtyUOM:str = obj["ThisRcptQtyUOM"]
      """  The UOM of the RMA Detail ( RMADtl.ReturnQtyUOM)  """  
      self.DisposedQtyUOM:str = obj["DisposedQtyUOM"]
      """  Same value as ReceivedQtyUOM.  """  
      self.EnableSN:bool = obj["EnableSN"]
      """  Flag to determine if Serial Numbers are required for this transaction.  """  
      self.EnableInspection:bool = obj["EnableInspection"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.WareHouseCodeDescription:str = obj["WareHouseCodeDescription"]
      """  Description.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used in the primary key.  """  
      self.NumberOfDigits:int = obj["NumberOfDigits"]
      """  Number of digits in the serial number  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  """  
      self.SNFormat1:str = obj["SNFormat1"]
      self.LeadingZeroes:bool = obj["LeadingZeroes"]
      """  Whether or not to have leading zeroes  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.HasSerialNumbers:bool = obj["HasSerialNumbers"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskMask:str = obj["SerialMaskMask"]
      self.SerialMaskExample:str = obj["SerialMaskExample"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Scrapped flag  """  
      self.ScrappedReasonCode:str = obj["ScrappedReasonCode"]
      """  Scrapped reason code  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.Reference:str = obj["Reference"]
      """  Reference field  """  
      self.ReasonCodeType:str = obj["ReasonCodeType"]
      """  Reason code type = s  """  
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      """  Reason code description  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNumber  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Serial number prefix  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number used to create the serial number  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this serial number  """  
      self.TransType:str = obj["TransType"]
      """  TransType of the record that created this serial number  """  
      self.PassedInspection:bool = obj["PassedInspection"]
      """  True if this serial numbered part passed inspection  """  
      self.Deselected:bool = obj["Deselected"]
      """  Used to flag previously selected serial numbers as deselected  """  
      self.KitWhseList:str = obj["KitWhseList"]
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  """  
      self.KBLbrAction:int = obj["KBLbrAction"]
      """  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  """  
      self.KBLbrActionDesc:str = obj["KBLbrActionDesc"]
      """  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  """  
      self.PreventDeselect:bool = obj["PreventDeselect"]
      """  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Used only by SN Assignment  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  """  
      self.PreDeselected:bool = obj["PreDeselected"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.SNMask:str = obj["SNMask"]
      """  The mask the was used to generate the serial number  """  
      self.NotSavedToDB:bool = obj["NotSavedToDB"]
      """  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  """  
      self.RowSelected:bool = obj["RowSelected"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SerialNumberSearchRow:
   def __init__(self, obj):
      self.ProcessToken:str = obj["ProcessToken"]
      """  Token reserved for the process ID  """  
      self.GenericToken1:str = obj["GenericToken1"]
      """  1st generic token.  """  
      self.GenericToken2:str = obj["GenericToken2"]
      """  2nd generic token  """  
      self.WhereClause:str = obj["WhereClause"]
      """  Returns where clause based on input tokens.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeBinNum_input:
   """ Required : 
   ds
   cBinNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      self.cBinNum:str = obj["cBinNum"]
      """  The proposed bin number  """  
      pass

class ChangeBinNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDispType_input:
   """ Required : 
   ds
   cDispType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      self.cDispType:str = obj["cDispType"]
      """  The proposed Disposition Type  """  
      pass

class ChangeDispType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      self.cMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeJob_input:
   """ Required : 
   ds
   cJobNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      self.cJobNum:str = obj["cJobNum"]
      """  The proposed Job number  """  
      pass

class ChangeJob_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      self.cmsgtype:int = obj["parameters"]
      self.cMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeToBinNum_input:
   """ Required : 
   ds
   cBinNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      self.cBinNum:str = obj["cBinNum"]
      """  The proposed bin number  """  
      pass

class ChangeToBinNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeToWarehouse_input:
   """ Required : 
   ds
   cWarehouseCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      self.cWarehouseCode:str = obj["cWarehouseCode"]
      """  The proposed warehouse code  """  
      pass

class ChangeToWarehouse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      self.cMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeWarehouse_input:
   """ Required : 
   ds
   cWarehouseCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      self.cWarehouseCode:str = obj["cWarehouseCode"]
      """  The proposed warehouse code  """  
      pass

class ChangeWarehouse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      self.cMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckClosedJob_input:
   """ Required : 
   cJobNum
   """  
   def __init__(self, obj):
      self.cJobNum:str = obj["cJobNum"]
      """  The Job number  """  
      pass

class CheckClosedJob_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cQuestionText:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckPlanningContractBin_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      pass

class CheckPlanningContractBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      self.pcPCBinAction:str = obj["parameters"]
      self.pcPCBinMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckWithInspResults_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      pass

class CheckWithInspResults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.TotPassed:int = obj["parameters"]
      self.TotFailed:int = obj["parameters"]
      self.InspDataEntered:bool = obj["InspDataEntered"]
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   rmANum
   rmALine
   rmAReceipt
   """  
   def __init__(self, obj):
      self.rmANum:int = obj["rmANum"]
      self.rmALine:int = obj["rmALine"]
      self.rmAReceipt:int = obj["rmAReceipt"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DisplayWarnMsg_input:
   """ Required : 
   PartTranType
   JobNum
   AsmSeq
   JobSeq
   """  
   def __init__(self, obj):
      self.PartTranType:str = obj["PartTranType"]
      self.JobNum:str = obj["JobNum"]
      self.AsmSeq:int = obj["AsmSeq"]
      self.JobSeq:int = obj["JobSeq"]
      pass

class DisplayWarnMsg_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RMADispRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Material Authorization number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA Receipt  """  
      self.RMADisp:int = obj["RMADisp"]
      """  An integer which is used to make the record unique to the related RMARcpt record.  """  
      self.DispType:str = obj["DispType"]
      """   Every part received on an RMA that needs to be disposition is received to inspection.  So when dispositioning RMAs the parts are coming out of inspection.
Field that indicates the type of disposition:
INS-MFG - Issued to Mfg ( Job Material)
INS-STK -  Received into Stock (Inventory)
INS-REJ -  Failed  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """   Warehouse ID the item was received into.
NOTE: Applies only to "RMA-STK".  """  
      self.BinNum:str = obj["BinNum"]
      """   Warehouse Bin location in which the item was placed.
NOTE: Applies only to "RMA-STK".  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number to which item was issued.  Applies only to RMA-MFG  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job Assembly sequence to which item was issued.  Applies only to RMA-MFG  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Job Material number to which item was issued.  Applies only to RMA-MFG  """  
      self.DispComment:str = obj["DispComment"]
      """   Comments about the disposition of this item.  These will be copied to the JobMtl.MfgComment for RMA-MFG.
Comments for manufacturing about this material record.  These comments are printed on manufacturing reports, such as the router.  For valid Parts use the Part.MfgComment as a default. 
View as editor widget.  """  
      self.InspectorID:str = obj["InspectorID"]
      """  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  """  
      self.InspectedBy:str = obj["InspectedBy"]
      """  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  """  
      self.InspectedDate:str = obj["InspectedDate"]
      """  Date when item was inspected.  """  
      self.InspectedTime:int = obj["InspectedTime"]
      """   Time of day when inspection transaction was recorded.
(seconds since midnight format)  """  
      self.NonConfTranID:int = obj["NonConfTranID"]
      """  TranID of related NonConf record.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Provides a link to the Reason table.  """  
      self.DispQty:int = obj["DispQty"]
      """  Disposition Quantity.  """  
      self.DispQtyUOM:str = obj["DispQtyUOM"]
      """  Unit Of Measure.  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.RequestMove:bool = obj["RequestMove"]
      """  Material Queue Records will only be updated if the "Request Move" box is checked  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OverrideCosts:bool = obj["OverrideCosts"]
      """  If set to true the user can manually override the costs used for the RMA disposition  """  
      self.UseCurrentCost:bool = obj["UseCurrentCost"]
      """  If set to true the current costs will default for the RMA disposition.  """  
      self.ToBinNum:str = obj["ToBinNum"]
      """  The to bin for the RMA disposition  """  
      self.ToWareHouseCode:str = obj["ToWareHouseCode"]
      """  The to warehouse for the RMA disposition  """  
      self.SetReassignSNAsm:bool = obj["SetReassignSNAsm"]
      """  Flag used to designate if the serial numbers from the job material/subassembly can be reassigned as the serial number of the parent assembly (top assembly or n deep subassembly) being reworked using a job.  """  
      self.CreateCorrectiveAction:bool = obj["CreateCorrectiveAction"]
      self.UpdateCommentAndReasonOnly:bool = obj["UpdateCommentAndReasonOnly"]
      self.MaterialUnitCost:int = obj["MaterialUnitCost"]
      self.BurdenUnitCost:int = obj["BurdenUnitCost"]
      self.SubUnitCost:int = obj["SubUnitCost"]
      self.MaterialBurdenUnitCost:int = obj["MaterialBurdenUnitCost"]
      self.LaborUnitCost:int = obj["LaborUnitCost"]
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      self.EnableBin:bool = obj["EnableBin"]
      self.DispTypeDescription:str = obj["DispTypeDescription"]
      self.EnableInspectedBy:bool = obj["EnableInspectedBy"]
      self.PartNum:str = obj["PartNum"]
      """  PartNum from RMADtl.  """  
      self.EnableSN:bool = obj["EnableSN"]
      """  Flag to know if serial number is valid in this transaction.  """  
      self.RequestMoveLicense:bool = obj["RequestMoveLicense"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.EnableInspection:bool = obj["EnableInspection"]
      """  To enable/disable the Inspection Data button on UI  """  
      self.ToBinDesc:str = obj["ToBinDesc"]
      self.ToWareHouseDesc:str = obj["ToWareHouseDesc"]
      self.FSAServiceType:str = obj["FSAServiceType"]
      """  Serivce Type  """  
      self.FSATechnician:str = obj["FSATechnician"]
      """  Technician  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Determines if the RMA is synchronized with Epicor FSA application.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.DispTypeList:str = obj["DispTypeList"]
      """  List of valid Disp types  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.Plant:str = obj["Plant"]
      """  The plant that any warehouse being selected for RMADisp should come from.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.InspectedByName:str = obj["InspectedByName"]
      self.InspectorIDName:str = obj["InspectorIDName"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.ReasonCodeDescription:str = obj["ReasonCodeDescription"]
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      self.WareHouseCodeDescription:str = obj["WareHouseCodeDescription"]
      self.WhseBinDescription:str = obj["WhseBinDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RMADispTableset:
   def __init__(self, obj):
      self.RMARcpt:list[Erp_Tablesets_RMARcptRow] = obj["RMARcpt"]
      self.RMADisp:list[Erp_Tablesets_RMADispRow] = obj["RMADisp"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SerialNumberSearch:list[Erp_Tablesets_SerialNumberSearchRow] = obj["SerialNumberSearch"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_RMARcptListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Authorization Number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line # of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA Receipt  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse ID the item was received into.  Normally this would be a "Inspection" type of warehouse.  """  
      self.BinNum:str = obj["BinNum"]
      """  Warehouse Bin location in which the received item was placed.  """  
      self.RcvDate:str = obj["RcvDate"]
      """  Receipt Date  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.OpenReceipt:bool = obj["OpenReceipt"]
      """  This is set to NO when the entire quantity has been accounted for in RMADisp.  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  The unit cost assigned to the return item.  This will actually be used to pass the cost value via the write trigger to the corresponding PartTran field. The system attempts to retrieve the cost from the last related "costed" shipment.  It's either the last shipment of the Order/Line, if given, or else it's the last shipment to the customer for this part.  If the shipment was from a job, and the shipment has not yet been costed then the system will attempt to calculate the proper costs using the Calculate COS logic found in program JCP80-GN.W.  The Qty X Unit Cost provides the amount that will be used to post to GL via the parttran record. The resulting G/L transactions are Debit to Inspection and Credit to "Cost of Returns".  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost of Returned Item.  (See MtlUnitCost)  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost of Returned Item.  (See MtlUnitCost)  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost of Returned Item.  (See MtlUnitCost)  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  The unit cost assigned to the return item.  This will actually be used to pass the cost value via the write trigger to the corresponding PartTran field. The system attempts to retrieve the cost from the last related "costed" shipment.  It's either the last shipment of the Order/Line, if given, or else it's the last shipment to the customer for this part.  If the shipment was from a job, and the shipment has not yet been costed then the system will attempt to calculate the proper costs using the Calculate COS logic found in program JCP80-GN.W.  The Qty X Unit Cost provides the amount that will be used to post to GL via the parttran record. The resulting G/L transactions are Debit to Inspection and Credit to "Cost of Returns".  """  
      self.Plant:str = obj["Plant"]
      """  The Site that this RMA receipt was received to.  This is set as from the "Current Site" at the time of receipt.  It will be used in the filtering of receipts in the Disposition process.  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.MtlMtlBurUnitCost:int = obj["MtlMtlBurUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  Quantity that has been received.  """  
      self.DisposedQty:int = obj["DisposedQty"]
      """  Quantity that has been dispositioned .  Cannot exceed ReceivedQty.  This is summation of the quantities from the supporting RMADisp records.  When DisposedQty = ReceivedQty the RMARcpt.OpenReceipt is set to NO.  """  
      self.CostUOM:str = obj["CostUOM"]
      """  Unit of measure that qualifies the unit costs.  """  
      self.ReceivedQtyUOM:str = obj["ReceivedQtyUOM"]
      """  Received Quantity unit of measure.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.RequestMove:bool = obj["RequestMove"]
      """  Material Queue Records will only be updated if the "Request Move" box is checked  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of the RMA line  """  
      self.EnableWarehouse:bool = obj["EnableWarehouse"]
      self.EnableBin:bool = obj["EnableBin"]
      self.CustomerName:str = obj["CustomerName"]
      self.PartRevisionNum:str = obj["PartRevisionNum"]
      self.EnableDelete:bool = obj["EnableDelete"]
      self.EnableUpdate:bool = obj["EnableUpdate"]
      self.CustNum:int = obj["CustNum"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      """  PartPartDescription  """  
      self.PartTrackLots:bool = obj["PartTrackLots"]
      """  PartTrackLots  """  
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      """  PartTrackSerialNum  """  
      self.ThisRcptQty:int = obj["ThisRcptQty"]
      """  The receipt quantity displayed in the RMADtl.ReturnQty.  """  
      self.ThisRcptQtyUOM:str = obj["ThisRcptQtyUOM"]
      """  The UOM of the RMA Detail ( RMADtl.ReturnQtyUOM)  """  
      self.DisposedQtyUOM:str = obj["DisposedQtyUOM"]
      """  Same value as ReceivedQtyUOM.  """  
      self.EnableSN:bool = obj["EnableSN"]
      """  Flag to determine if Serial Numbers are required for this transaction.  """  
      self.EnableInspection:bool = obj["EnableInspection"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.WareHouseCodeDescription:str = obj["WareHouseCodeDescription"]
      """  Description.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RMARcptListTableset:
   def __init__(self, obj):
      self.RMARcptList:list[Erp_Tablesets_RMARcptListRow] = obj["RMARcptList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_RMARcptRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Authorization Number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line # of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA Receipt  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse ID the item was received into.  Normally this would be a "Inspection" type of warehouse.  """  
      self.BinNum:str = obj["BinNum"]
      """  Warehouse Bin location in which the received item was placed.  """  
      self.RcvDate:str = obj["RcvDate"]
      """  Receipt Date  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.OpenReceipt:bool = obj["OpenReceipt"]
      """  This is set to NO when the entire quantity has been accounted for in RMADisp.  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  The unit cost assigned to the return item.  This will actually be used to pass the cost value via the write trigger to the corresponding PartTran field. The system attempts to retrieve the cost from the last related "costed" shipment.  It's either the last shipment of the Order/Line, if given, or else it's the last shipment to the customer for this part.  If the shipment was from a job, and the shipment has not yet been costed then the system will attempt to calculate the proper costs using the Calculate COS logic found in program JCP80-GN.W.  The Qty X Unit Cost provides the amount that will be used to post to GL via the parttran record. The resulting G/L transactions are Debit to Inspection and Credit to "Cost of Returns".  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost of Returned Item.  (See MtlUnitCost)  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost of Returned Item.  (See MtlUnitCost)  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost of Returned Item.  (See MtlUnitCost)  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  The unit cost assigned to the return item.  This will actually be used to pass the cost value via the write trigger to the corresponding PartTran field. The system attempts to retrieve the cost from the last related "costed" shipment.  It's either the last shipment of the Order/Line, if given, or else it's the last shipment to the customer for this part.  If the shipment was from a job, and the shipment has not yet been costed then the system will attempt to calculate the proper costs using the Calculate COS logic found in program JCP80-GN.W.  The Qty X Unit Cost provides the amount that will be used to post to GL via the parttran record. The resulting G/L transactions are Debit to Inspection and Credit to "Cost of Returns".  """  
      self.Plant:str = obj["Plant"]
      """  The Site that this RMA receipt was received to.  This is set as from the "Current Site" at the time of receipt.  It will be used in the filtering of receipts in the Disposition process.  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.MtlMtlBurUnitCost:int = obj["MtlMtlBurUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  Quantity that has been received.  """  
      self.DisposedQty:int = obj["DisposedQty"]
      """  Quantity that has been dispositioned .  Cannot exceed ReceivedQty.  This is summation of the quantities from the supporting RMADisp records.  When DisposedQty = ReceivedQty the RMARcpt.OpenReceipt is set to NO.  """  
      self.CostUOM:str = obj["CostUOM"]
      """  Unit of measure that qualifies the unit costs.  """  
      self.ReceivedQtyUOM:str = obj["ReceivedQtyUOM"]
      """  Received Quantity unit of measure.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.RequestMove:bool = obj["RequestMove"]
      """  Material Queue Records will only be updated if the "Request Move" box is checked  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of the RMA line  """  
      self.EnableWarehouse:bool = obj["EnableWarehouse"]
      self.EnableBin:bool = obj["EnableBin"]
      self.CustomerName:str = obj["CustomerName"]
      self.PartRevisionNum:str = obj["PartRevisionNum"]
      self.EnableDelete:bool = obj["EnableDelete"]
      self.EnableUpdate:bool = obj["EnableUpdate"]
      self.CustNum:int = obj["CustNum"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      """  PartPartDescription  """  
      self.PartTrackLots:bool = obj["PartTrackLots"]
      """  PartTrackLots  """  
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      """  PartTrackSerialNum  """  
      self.ThisRcptQty:int = obj["ThisRcptQty"]
      """  The receipt quantity displayed in the RMADtl.ReturnQty.  """  
      self.ThisRcptQtyUOM:str = obj["ThisRcptQtyUOM"]
      """  The UOM of the RMA Detail ( RMADtl.ReturnQtyUOM)  """  
      self.DisposedQtyUOM:str = obj["DisposedQtyUOM"]
      """  Same value as ReceivedQtyUOM.  """  
      self.EnableSN:bool = obj["EnableSN"]
      """  Flag to determine if Serial Numbers are required for this transaction.  """  
      self.EnableInspection:bool = obj["EnableInspection"]
      self.IsPartMaster:bool = obj["IsPartMaster"]
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial Number used only for FSA  """  
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.PartTrackInventoryByRevision:bool = obj["PartTrackInventoryByRevision"]
      self.PartTrackInventoryAttributes:bool = obj["PartTrackInventoryAttributes"]
      self.BitFlag:int = obj["BitFlag"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.WareHouseCodeDescription:str = obj["WareHouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used in the primary key.  """  
      self.NumberOfDigits:int = obj["NumberOfDigits"]
      """  Number of digits in the serial number  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  """  
      self.SNFormat:str = obj["SNFormat"]
      """   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  """  
      self.LeadingZeroes:bool = obj["LeadingZeroes"]
      """  Whether or not to have leading zeroes  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.HasSerialNumbers:bool = obj["HasSerialNumbers"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskMask:str = obj["SerialMaskMask"]
      self.SerialMaskExample:str = obj["SerialMaskExample"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectSerialNumbersParamsRow:
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  The part number to which the serial numbers have been assigned.  """  
      self.quantity:int = obj["quantity"]
      """  The quantity of serial numbers that need to be selected.  """  
      self.whereClause:str = obj["whereClause"]
      """  whereClause for filtering available serial numbers  """  
      self.transType:str = obj["transType"]
      """  transType of this transaction  """  
      self.sourceRowID:str = obj["sourceRowID"]
      """  Include when filtering a set of SN's for BL processing is necessary.  It may be null if not needed.  """  
      self.enableCreate:bool = obj["enableCreate"]
      """  Determines if serial numbers can be created.  """  
      self.enableSelect:bool = obj["enableSelect"]
      """  Determines if serial numbers can be selected.  """  
      self.enableRetrieve:bool = obj["enableRetrieve"]
      """  Determines if serial numbers can be retrieved.  """  
      self.allowVoided:bool = obj["allowVoided"]
      """  Specifies whether Voided serial numbers can be manually selected.  """  
      self.plant:str = obj["plant"]
      """  The Plant associated with this transaction  """  
      self.xrefPartNum:str = obj["xrefPartNum"]
      self.xrefPartType:str = obj["xrefPartType"]
      self.xrefCustNum:int = obj["xrefCustNum"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.attributeSetShortDescription:str = obj["attributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.revisionNum:str = obj["revisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectSerialNumbersParamsTableset:
   def __init__(self, obj):
      self.SelectSerialNumbersParams:list[Erp_Tablesets_SelectSerialNumbersParamsRow] = obj["SelectSerialNumbersParams"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Scrapped flag  """  
      self.ScrappedReasonCode:str = obj["ScrappedReasonCode"]
      """  Scrapped reason code  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.Reference:str = obj["Reference"]
      """  Reference field  """  
      self.ReasonCodeType:str = obj["ReasonCodeType"]
      """  Reason code type = s  """  
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      """  Reason code description  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNumber  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Serial number prefix  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number used to create the serial number  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this serial number  """  
      self.TransType:str = obj["TransType"]
      """  TransType of the record that created this serial number  """  
      self.PassedInspection:bool = obj["PassedInspection"]
      """  True if this serial numbered part passed inspection  """  
      self.Deselected:bool = obj["Deselected"]
      """  Used to flag previously selected serial numbers as deselected  """  
      self.KitWhseList:str = obj["KitWhseList"]
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  """  
      self.KBLbrAction:int = obj["KBLbrAction"]
      """  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  """  
      self.KBLbrActionDesc:str = obj["KBLbrActionDesc"]
      """  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  """  
      self.PreventDeselect:bool = obj["PreventDeselect"]
      """  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Used only by SN Assignment  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  """  
      self.PreDeselected:bool = obj["PreDeselected"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.SNMask:str = obj["SNMask"]
      """  The mask the was used to generate the serial number  """  
      self.NotSavedToDB:bool = obj["NotSavedToDB"]
      """  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  """  
      self.RowSelected:bool = obj["RowSelected"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SerialNumberSearchRow:
   def __init__(self, obj):
      self.ProcessToken:str = obj["ProcessToken"]
      """  Token reserved for the process ID  """  
      self.GenericToken1:str = obj["GenericToken1"]
      """  1st generic token.  """  
      self.GenericToken2:str = obj["GenericToken2"]
      """  2nd generic token  """  
      self.WhereClause:str = obj["WhereClause"]
      """  Returns where clause based on input tokens.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtRMADispTableset:
   def __init__(self, obj):
      self.RMARcpt:list[Erp_Tablesets_RMARcptRow] = obj["RMARcpt"]
      self.RMADisp:list[Erp_Tablesets_RMADispRow] = obj["RMADisp"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SerialNumberSearch:list[Erp_Tablesets_SerialNumberSearchRow] = obj["SerialNumberSearch"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetAvailTranDocTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.listAvailTranDocTypes:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   rmANum
   rmALine
   rmAReceipt
   """  
   def __init__(self, obj):
      self.rmANum:int = obj["rmANum"]
      self.rmALine:int = obj["rmALine"]
      self.rmAReceipt:int = obj["rmAReceipt"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RMADispTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RMADispTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RMADispTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetLegalNumGenOpts_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      pass

class GetLegalNumGenOpts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      self.requiresUserInput:bool = obj["requiresUserInput"]
      pass

      """  output parameters  """  

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RMARcptListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewRMADisp_input:
   """ Required : 
   ds
   rmANum
   rmALine
   rmAReceipt
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      self.rmANum:int = obj["rmANum"]
      self.rmALine:int = obj["rmALine"]
      self.rmAReceipt:int = obj["rmAReceipt"]
      pass

class GetNewRMADisp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRMARcpt_input:
   """ Required : 
   ds
   rmANum
   rmALine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      self.rmANum:int = obj["rmANum"]
      self.rmALine:int = obj["rmALine"]
      pass

class GetNewRMARcpt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPartTranPKs_input:
   """ Required : 
   ipRMANum
   ipRMALine
   ipRMAReceipt
   ipRMADisp
   """  
   def __init__(self, obj):
      self.ipRMANum:int = obj["ipRMANum"]
      """  RMANum field  """  
      self.ipRMALine:int = obj["ipRMALine"]
      """  RMALine field  """  
      self.ipRMAReceipt:int = obj["ipRMAReceipt"]
      """  RMAReceipt field  """  
      self.ipRMADisp:int = obj["ipRMADisp"]
      """  RMADisp field  """  
      pass

class GetPartTranPKs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partTranPKs:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseRMARcpt
   whereClauseRMADisp
   whereClauseLegalNumGenOpts
   whereClauseSelectedSerialNumbers
   whereClauseSerialNumberSearch
   whereClauseSNFormat
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseRMARcpt:str = obj["whereClauseRMARcpt"]
      self.whereClauseRMADisp:str = obj["whereClauseRMADisp"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      self.whereClauseSerialNumberSearch:str = obj["whereClauseSerialNumberSearch"]
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RMADispTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSelectSerialNumbersParams_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      pass

class GetSelectSerialNumbersParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SelectSerialNumbersParamsTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class OnChangeDispQty_input:
   """ Required : 
   ds
   proposedDispQty
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      self.proposedDispQty:int = obj["proposedDispQty"]
      pass

class OnChangeDispQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOverrideCost_input:
   """ Required : 
   ds
   ProposedOverride
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      self.ProposedOverride:bool = obj["ProposedOverride"]
      pass

class OnChangeOverrideCost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeUseCurrentCost_input:
   """ Required : 
   ds
   proposedUseCurrentCost
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      self.proposedUseCurrentCost:bool = obj["proposedUseCurrentCost"]
      pass

class OnChangeUseCurrentCost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RMACanBeLinkedToJob_input:
   """ Required : 
   jobNum
   rmaNum
   rmaLine
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      """  The Job number  """  
      self.rmaNum:int = obj["rmaNum"]
      """  The RMA number  """  
      self.rmaLine:int = obj["rmaLine"]
      """  The RMA line  """  
      pass

class RMACanBeLinkedToJob_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.cQuestionText:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtRMADispTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtRMADispTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateSN_input:
   """ Required : 
   ds
   serialNumber
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      self.serialNumber:str = obj["serialNumber"]
      """  Serial number to validate.  """  
      pass

class ValidateSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMADispTableset] = obj["ds"]
      self.isVoided:bool = obj["isVoided"]
      pass

      """  output parameters  """  

