import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.VendPartSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_VendParts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VendParts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendParts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendParts",headers=creds) as resp:
           return await resp.json()

async def post_VendParts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendPartRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VendPartRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendParts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VendParts_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate(Company, PartNum, OpCode, PUM, VendorNum, EffectiveDate, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendPart item
   Description: Calls GetByID to retrieve the VendPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param PUM: Desc: PUM   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param EffectiveDate: Desc: EffectiveDate   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendParts(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VendParts_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate(Company, PartNum, OpCode, PUM, VendorNum, EffectiveDate, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VendPart for the service
   Description: Calls UpdateExt to update VendPart. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param PUM: Desc: PUM   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param EffectiveDate: Desc: EffectiveDate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendPartRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendParts(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VendParts_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate(Company, PartNum, OpCode, PUM, VendorNum, EffectiveDate, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VendPart item
   Description: Call UpdateExt to delete VendPart item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param PUM: Desc: PUM   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param EffectiveDate: Desc: EffectiveDate   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendParts(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + ")",headers=creds) as resp:
           return await resp.json()

async def get_VendParts_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate_VendPBrks(Company, PartNum, OpCode, PUM, VendorNum, EffectiveDate, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get VendPBrks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VendPBrks1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param PUM: Desc: PUM   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param EffectiveDate: Desc: EffectiveDate   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendPBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendParts(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + ")/VendPBrks",headers=creds) as resp:
           return await resp.json()

async def get_VendParts_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate_VendPBrks_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate_BreakQty(Company, PartNum, OpCode, PUM, VendorNum, EffectiveDate, BreakQty, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendPBrk item
   Description: Calls GetByID to retrieve the VendPBrk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendPBrk1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param PUM: Desc: PUM   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param EffectiveDate: Desc: EffectiveDate   Required: True   Allow empty value : True
      :param BreakQty: Desc: BreakQty   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendPBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendParts(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + ")/VendPBrks(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + "," + BreakQty + ")",headers=creds) as resp:
           return await resp.json()

async def get_VendParts_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate_VendPartAttches(Company, PartNum, OpCode, PUM, VendorNum, EffectiveDate, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get VendPartAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VendPartAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param PUM: Desc: PUM   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param EffectiveDate: Desc: EffectiveDate   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendPartAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendParts(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + ")/VendPartAttches",headers=creds) as resp:
           return await resp.json()

async def get_VendParts_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate_VendPartAttches_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate_DrawingSeq(Company, PartNum, OpCode, PUM, VendorNum, EffectiveDate, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendPartAttch item
   Description: Calls GetByID to retrieve the VendPartAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendPartAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param PUM: Desc: PUM   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param EffectiveDate: Desc: EffectiveDate   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendPartAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendParts(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + ")/VendPartAttches(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_VendPBrks(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VendPBrks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendPBrks
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendPBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendPBrks",headers=creds) as resp:
           return await resp.json()

async def post_VendPBrks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendPBrks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendPBrkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VendPBrkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendPBrks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VendPBrks_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate_BreakQty(Company, PartNum, OpCode, PUM, VendorNum, EffectiveDate, BreakQty, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendPBrk item
   Description: Calls GetByID to retrieve the VendPBrk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendPBrk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param PUM: Desc: PUM   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param EffectiveDate: Desc: EffectiveDate   Required: True   Allow empty value : True
      :param BreakQty: Desc: BreakQty   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendPBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendPBrks(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + "," + BreakQty + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VendPBrks_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate_BreakQty(Company, PartNum, OpCode, PUM, VendorNum, EffectiveDate, BreakQty, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VendPBrk for the service
   Description: Calls UpdateExt to update VendPBrk. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendPBrk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param PUM: Desc: PUM   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param EffectiveDate: Desc: EffectiveDate   Required: True   Allow empty value : True
      :param BreakQty: Desc: BreakQty   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendPBrkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendPBrks(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + "," + BreakQty + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VendPBrks_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate_BreakQty(Company, PartNum, OpCode, PUM, VendorNum, EffectiveDate, BreakQty, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VendPBrk item
   Description: Call UpdateExt to delete VendPBrk item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendPBrk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param PUM: Desc: PUM   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param EffectiveDate: Desc: EffectiveDate   Required: True   Allow empty value : True
      :param BreakQty: Desc: BreakQty   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendPBrks(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + "," + BreakQty + ")",headers=creds) as resp:
           return await resp.json()

async def get_VendPartAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VendPartAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendPartAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendPartAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendPartAttches",headers=creds) as resp:
           return await resp.json()

async def post_VendPartAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendPartAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendPartAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VendPartAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendPartAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VendPartAttches_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate_DrawingSeq(Company, PartNum, OpCode, PUM, VendorNum, EffectiveDate, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendPartAttch item
   Description: Calls GetByID to retrieve the VendPartAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendPartAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param PUM: Desc: PUM   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param EffectiveDate: Desc: EffectiveDate   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendPartAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendPartAttches(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VendPartAttches_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate_DrawingSeq(Company, PartNum, OpCode, PUM, VendorNum, EffectiveDate, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VendPartAttch for the service
   Description: Calls UpdateExt to update VendPartAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendPartAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param PUM: Desc: PUM   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param EffectiveDate: Desc: EffectiveDate   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendPartAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendPartAttches(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VendPartAttches_Company_PartNum_OpCode_PUM_VendorNum_EffectiveDate_DrawingSeq(Company, PartNum, OpCode, PUM, VendorNum, EffectiveDate, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VendPartAttch item
   Description: Call UpdateExt to delete VendPartAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendPartAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param PUM: Desc: PUM   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param EffectiveDate: Desc: EffectiveDate   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/VendPartAttches(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + EffectiveDate + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendPartListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseVendPart, whereClauseVendPartAttch, whereClauseVendPBrk, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseVendPart=" + whereClauseVendPart
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseVendPartAttch=" + whereClauseVendPartAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseVendPBrk=" + whereClauseVendPBrk
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(partNum, opCode, puM, vendorNum, effectiveDate, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
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
   params += "partNum=" + partNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "opCode=" + opCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "puM=" + puM
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "vendorNum=" + vendorNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "effectiveDate=" + effectiveDate

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeAprvSupplier(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeAprvSupplier
   OperationID: ChangeAprvSupplier
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAprvSupplier_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAprvSupplier_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeConvOverride(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeConvOverride
   Description: This should be called on change of VendPart.ConvOverride
when false it will refresh the Conversion fields to UOM Master values.
   OperationID: ChangeConvOverride
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeConvOverride_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeConvOverride_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeEffectiveDays(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeEffectiveDays
   Description: Method to call when changing the EffectiveDays, EffectiveDate, or ExpirationDate changes.
This method will recalculate the ExpirationDate if the EffectiveDate or EffectiveDays
change; it will recalculate the EffectiveDays if the ExpirationDate changes.
   OperationID: ChangeEffectiveDays
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEffectiveDays_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEffectiveDays_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeImportExportVendorID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeImportExportVendorID
   Description: This assigns the vendor name in the SupListImpExpParams datatable.
   OperationID: ChangeImportExportVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeImportExportVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeImportExportVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePart
   Description: Run this method when Part Number on the detail screen changes (copied from SO)
   OperationID: ChangePart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateAprvSupplier(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateAprvSupplier
   OperationID: UpdateAprvSupplier
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateAprvSupplier_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateAprvSupplier_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePriceModifier(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePriceModifier
   Description: Method to call when changing the price modifier on the vendor part break record.
Recalculates the effective price based on the new price modifier.
   OperationID: ChangePriceModifier
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePriceModifier_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePriceModifier_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVendPartPUM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVendPartPUM
   Description: This method creates a new ttVendPart record and deletes the existing one when
changing this component of the primary unique index and update the VendPart.PUM.
This method should run before changing the VendPart.PUM.
   OperationID: ChangeVendPartPUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendPartPUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendPartPUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeConvOperator(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeConvOperator
   Description: This should be called on change of VendPart.ConvOperator
for recalculation of the ConvFactor
   OperationID: ChangeConvOperator
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeConvOperator_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeConvOperator_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeConvFactor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeConvFactor
   Description: This should be called on change of VendPart.ConvFactor
for recalculation of the ConvFactor
   OperationID: ChangeConvFactor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeConvFactor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeConvFactor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultRFQInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultRFQInfo
   Description: This method is called when the Supplier Price List object is called from
Supplier Response.  After a new VendPart record has been created, this method
needs to be called to default the specific RFQ information
   OperationID: GetDefaultRFQInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultRFQInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultRFQInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultRFQInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultRFQInfo
   Description: This method is called when the Supplier Price List object is called from
Supplier Response.  After a new VendPart record has been created, this method
needs to be called to default the specific RFQ information
   OperationID: DefaultRFQInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultRFQInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultRFQInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportSupplierList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportSupplierList
   Description: This method conditionally adds/overwrites supplier part records from an import file.
   OperationID: ExportSupplierList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportSupplierList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportSupplierList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportSupplierListToServerFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportSupplierListToServerFile
   Description: This method conditionally adds/overwrites supplier part records from an import file.
   OperationID: ExportSupplierListToServerFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportSupplierListToServerFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportSupplierListToServerFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetImportSupplierListFromServerFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetImportSupplierListFromServerFile
   Description: This method loads supplier part records from an import file for reviewing/editing.
   OperationID: GetImportSupplierListFromServerFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetImportSupplierListFromServerFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetImportSupplierListFromServerFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLastEffectiveVendPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLastEffectiveVendPart
   Description: Method to get the last effective VendPart record.
   OperationID: GetLastEffectiveVendPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLastEffectiveVendPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLastEffectiveVendPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSupListImpExpParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSupListImpExpParams
   Description: This method creates a record in SupListImpExpParams.  This record is used
to store the import/export parameters.
   OperationID: GetNewSupListImpExpParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSupListImpExpParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSupListImpExpParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetVendorNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetVendorNum
   Description: Method to call get a VendorNum given a VendorID.
   OperationID: GetVendorNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVendorNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendorNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPrimaryVendorNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPrimaryVendorNum
   Description: Method to get the Primary VendorNum given a PartNum.
   OperationID: GetPrimaryVendorNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPrimaryVendorNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPrimaryVendorNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetVendPartByPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetVendPartByPart
   Description: Method to call to get the dataset based on a specific part.
   OperationID: GetVendPartByPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVendPartByPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendPartByPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetVendPartByVendNumPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetVendPartByVendNumPart
   Description: Method to call to get the dataset based on a specific vendor and part.
   OperationID: GetVendPartByVendNumPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVendPartByVendNumPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendPartByVendNumPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetVendPartByVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetVendPartByVendor
   Description: Method to call to get the dataset based on a specific vendor.
   OperationID: GetVendPartByVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVendPartByVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendPartByVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportSupplierList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportSupplierList
   Description: This method conditionally adds/overwrites supplier part records from an import file.
   OperationID: ImportSupplierList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportSupplierList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportSupplierList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetVendPartIndexEffectiveRecord(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetVendPartIndexEffectiveRecord
   OperationID: GetVendPartIndexEffectiveRecord
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVendPartIndexEffectiveRecord_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendPartIndexEffectiveRecord_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetActiveParts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetActiveParts
   OperationID: GetActiveParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetActiveParts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetActiveParts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVendPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVendPart
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVendPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVendPartAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVendPartAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendPartAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVendPartAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendPartAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVendPBrk(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVendPBrk
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendPBrk
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVendPBrk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendPBrk_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPBrkRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VendPBrkRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VendPartAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VendPartListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VendPartRow] = obj["value"]
      pass

class Erp_Tablesets_VendPBrkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies our Part.  """  
      self.OpCode:str = obj["OpCode"]
      """   Operation Code - of the related parent VendPart record.
(See VendPart.OpCode).  """  
      self.PUM:str = obj["PUM"]
      """  Purchasing Unit of measure.  A component of the unique key and parent table (VendPart) relationship.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor's unique internal number.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  The date which this vendor/part information is effective.  """  
      self.BreakQty:int = obj["BreakQty"]
      """  Minimum Quantity required to obtain the related UnitPrice.  This is in Vendor's unit of measure.  """  
      self.PriceModifier:int = obj["PriceModifier"]
      """   This field represents the value used to determine a effective unit price for the related BreakQty.  It can be expressed as a Flat Amount or Percent of Base Price which is determined by the VendPart.PriceFormat field. Negatives are allowed to enter deductions to the base cost.
Effective Unit Price = BasePrice + PriceModifier  """  
      self.DaysOut:int = obj["DaysOut"]
      """  Hours required is calculated as days * 8.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EffectivePrice:int = obj["EffectivePrice"]
      self.BitFlag:int = obj["BitFlag"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendPartAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.OpCode:str = obj["OpCode"]
      self.PUM:str = obj["PUM"]
      self.VendorNum:int = obj["VendorNum"]
      self.EffectiveDate:str = obj["EffectiveDate"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendPartListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies our Part.  """  
      self.OpCode:str = obj["OpCode"]
      """   Operation Code - this is a component of the index which uniquely identifies the record.  Used to identify specific subcontracting operations prices  for a Part/Vendor.
This field can be blank (raw materials) or must be valid in the OpMaster (subcontracts).  """  
      self.PUM:str = obj["PUM"]
      """   The Purchasing Unit of measure for the Part from the vendor.
Defaulted from Part.PUM.  This is used in Purchase Order entry as the default on line item details.  It Overrides Part.PUM  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  The date which this vendor/part information is effective.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor's unique internal number.  """  
      self.LeadTime:int = obj["LeadTime"]
      """  Used to record the normal  order lead time that this vendor gives for this part. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  """  
      self.BaseUnitPrice:int = obj["BaseUnitPrice"]
      """   BaseUnitPrice + VendPBrk.UnitPrice = Unit Price for the Part.  This design allows users to enter "Qty Break Unit Prices" (VendPBrk.UnitPrice) either as a price that should be Added or Subtracted (negatives) to Base or as a true Unit Price(Base = 0).  This is an attempt to make it easier to enter prices from varying formats of vendor price lists.
Some vendors define their prices as a Base Unit Price with an additional amount to be added/deducted to it at specific quantities levels.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Part number that the Vendor uses to identify the item.  """  
      self.PriceFormat:str = obj["PriceFormat"]
      """  Indicates the format of UnitPrices in VendPBrk table.  This can either be "$" = Flat Unit Price, or "%" = Percent of Base.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """   Indicates the vendor's pricing per value for the part.                     "E" = per each, "C" = per hundred,  "M" = per thousand.
Used as a default in purchasing, also used to convert a vendor unit price to our unit costs.
Basic formula for converting to "our unit cost" is as follows...
Our Unit$ = Vendor Unit$ / Cost Per factor) * PurchasingFactor.  """  
      self.MinimumPrice:int = obj["MinimumPrice"]
      """   Minimum Charge for this material.  This is used as a default to QuoteMtl.MinimumCost, QuoteOpr.MinimumCost.  In routines used to retrieve a default unit cost (PO, Jobs..) the Manufacturing System  will take the greater of (required quantity * unit cost) or (MinimumCost).
Note: The AddlCharge is not included in the above formula.  """  
      self.ExpirationDate:str = obj["ExpirationDate"]
      """  Optional Expiration date of this cost information.  The Manufacturing System uses this date to inform the user when the cost information that is being used has expired.  This is an indicator that this information may not be accurate and should be reconfirmed with the vendor.  """  
      self.Reference:str = obj["Reference"]
      """  An optional field that may be used for any reference to this vendors costing info. Ex: RFQ, Quote#, etc...  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """   A total additional charge that is incurred when purchasing this service. Ex(Lot,Setup,Handling,etc...). This is only used with a Subcontract price. It's used as a default to QuoteOpr.MiscCharge, JobOper.MiscCharge and POMisc.MiscAmt
will be defaulted to the This is NOT part of the a Unit Cost. It is NOT consider in the logic of using Minimum Cost.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code related to the MiscCharge field. If MiscCharge <> 0 then must be entered and valid in the PURMisc file.  This will be the MiscCode used to create the PoMisc record when defaults are created in purchase order entry.  """  
      self.CommentText:str = obj["CommentText"]
      """  Additional comments that will be used as a default for purchasing.  View as an EDITOR widget.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """   Overall discount percent. Used to develop an effective unit price.
(BaseUnitPrice + QtyBrkValue) *( (100 - DiscountPercent) * .01)  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Description of Part. Used only for Non Part master parts.  """  
      self.RFQNum:int = obj["RFQNum"]
      """   Related RFQ number.
Note: zero for price breaks entered via master maintenance.  """  
      self.RFQLine:int = obj["RFQLine"]
      """   Related RFQ Line number.
Note: Zero for price breaks created by master maintenance programs.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """   A unique code that identifies the currency.
NOT ACTIVE  AS OF 3.20. RESERVED FOR FUTURE USE.  """  
      self.OnhandQty:int = obj["OnhandQty"]
      """  Suppliers Quantity on Hand  """  
      self.OnHandDate:str = obj["OnHandDate"]
      """  Date Suppliers Quantity was updated  """  
      self.OnHandTime:int = obj["OnHandTime"]
      """  Time Suppliers Quantity was updated  """  
      self.ConNum:int = obj["ConNum"]
      """  Supplier contact linked to this Price  """  
      self.SupplierResponseReady:bool = obj["SupplierResponseReady"]
      """  This is for use in SupplierConnect.  It indicates the Supplier has completed the changes to the RFQ and is ready for the data to be posted back to Epicor.  """  
      self.DefaultPUM:bool = obj["DefaultPUM"]
      """  Indicates if this Supplier Price List will be the default to select a PUM.  """  
      self.ConvOperator:str = obj["ConvOperator"]
      """   Indicates the mathmatical operator that is used for performing the UOM Conversion. Options are "*" (Multiply) or "\" (Divide).
For example for Feet to Inch where Inch is the base uom. 
You could have 1ft / 12 = 1In  """  
      self.ConvFactor:int = obj["ConvFactor"]
      """   Value used to convert to/from base uom for the specific part. Cannot change if it's base uom of UOMClass (always 1.0) Sometimes a unit of measure conversion is relative to a specific part. These are non-standard conversions.
For example; 1 box(bx) of  Part A is 12ea. 1(bx) of Part B is 24ea. Non-standard conversions are defined in the PartUOM table. When ConvOperator = * then ConvFactor is 1 UOM expressed in Base UOM else it is 1 Base UOM expressed in UOM  """  
      self.ConvOverRide:bool = obj["ConvOverRide"]
      """  Purchase Point  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OpCodeDescription:str = obj["OpCodeDescription"]
      self.VendorName:str = obj["VendorName"]
      self.CurrencyCodeDescription:str = obj["CurrencyCodeDescription"]
      self.PrimaryVendor:bool = obj["PrimaryVendor"]
      self.EffectiveDays:int = obj["EffectiveDays"]
      self.VendorID:str = obj["VendorID"]
      self.FromRFQ:str = obj["FromRFQ"]
      """  RFQVend ID  """  
      self.NonPartMaster:bool = obj["NonPartMaster"]
      """  This field is to check when the selected part doesnt exist in the part master. When the part does not exist in the Part Master, this field is set to YES, when the part exists in the part master it is set to NO.  """  
      self.AprvSupplier:bool = obj["AprvSupplier"]
      """  Approved Supplier  """  
      self.AprvForACustomer:bool = obj["AprvForACustomer"]
      """  Supplier Approved for a Customer. It is true when AprvVend.CustNum is not zero.  """  
      self.ConvBaseUOM:str = obj["ConvBaseUOM"]
      """  Base UOM  """  
      self.ConvFromUOM:str = obj["ConvFromUOM"]
      """  ReadOnly field used to clarify converion.  Displayed as one of the uom, ex 1 EA  """  
      self.ConvToUOM:str = obj["ConvToUOM"]
      """  ReadOnly field used to clarify converion.  Displayed as nnnnn.nnnn "base uom"  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      """  Description of the Miscellaneous Charge. Used as a default to Orders and Invoices.  """  
      self.MiscCodeLCDisburseMethod:str = obj["MiscCodeLCDisburseMethod"]
      """  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  """  
      self.MiscCodeLCAmount:int = obj["MiscCodeLCAmount"]
      """  Landed Cost amount in the specified document currency.  This will be the default when this miscellaneous charge is used as Indirect Cost during receipts.  """  
      self.MiscCodeLCCurrencyCode:str = obj["MiscCodeLCCurrencyCode"]
      """  The Landed Cost Currency Code for this miscellaneous charge.  """  
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      """  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.VendorNameTermsCode:str = obj["VendorNameTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNameCountry:str = obj["VendorNameCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNameAddress2:str = obj["VendorNameAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNameName:str = obj["VendorNameName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNameVendorID:str = obj["VendorNameVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNameAddress3:str = obj["VendorNameAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNameCurrencyCode:str = obj["VendorNameCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNameState:str = obj["VendorNameState"]
      """  Can be blank.  """  
      self.VendorNameZIP:str = obj["VendorNameZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNameAddress1:str = obj["VendorNameAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNameCity:str = obj["VendorNameCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNameDefaultFOB:str = obj["VendorNameDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendPartRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies our Part.  """  
      self.OpCode:str = obj["OpCode"]
      """   Operation Code - this is a component of the index which uniquely identifies the record.  Used to identify specific subcontracting operations prices  for a Part/Vendor.
This field can be blank (raw materials) or must be valid in the OpMaster (subcontracts).  """  
      self.PUM:str = obj["PUM"]
      """   The Purchasing Unit of measure for the Part from the vendor.
Defaulted from Part.PUM.  This is used in Purchase Order entry as the default on line item details.  It Overrides Part.PUM  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  The date which this vendor/part information is effective.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor's unique internal number.  """  
      self.LeadTime:int = obj["LeadTime"]
      """  Used to record the normal  order lead time that this vendor gives for this part. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  """  
      self.BaseUnitPrice:int = obj["BaseUnitPrice"]
      """   BaseUnitPrice + VendPBrk.UnitPrice = Unit Price for the Part.  This design allows users to enter "Qty Break Unit Prices" (VendPBrk.UnitPrice) either as a price that should be Added or Subtracted (negatives) to Base or as a true Unit Price(Base = 0).  This is an attempt to make it easier to enter prices from varying formats of vendor price lists.
Some vendors define their prices as a Base Unit Price with an additional amount to be added/deducted to it at specific quantities levels.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Part number that the Vendor uses to identify the item.  """  
      self.PriceFormat:str = obj["PriceFormat"]
      """  Indicates the format of UnitPrices in VendPBrk table.  This can either be "$" = Flat Unit Price, or "%" = Percent of Base.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """   Indicates the vendor's pricing per value for the part.                     "E" = per each, "C" = per hundred,  "M" = per thousand.
Used as a default in purchasing, also used to convert a vendor unit price to our unit costs.
Basic formula for converting to "our unit cost" is as follows...
Our Unit$ = Vendor Unit$ / Cost Per factor) * PurchasingFactor.  """  
      self.MinimumPrice:int = obj["MinimumPrice"]
      """   Minimum Charge for this material.  This is used as a default to QuoteMtl.MinimumCost, QuoteOpr.MinimumCost.  In routines used to retrieve a default unit cost (PO, Jobs..) the Manufacturing System  will take the greater of (required quantity * unit cost) or (MinimumCost).
Note: The AddlCharge is not included in the above formula.  """  
      self.ExpirationDate:str = obj["ExpirationDate"]
      """  Optional Expiration date of this cost information.  The Manufacturing System uses this date to inform the user when the cost information that is being used has expired.  This is an indicator that this information may not be accurate and should be reconfirmed with the vendor.  """  
      self.Reference:str = obj["Reference"]
      """  An optional field that may be used for any reference to this vendors costing info. Ex: RFQ, Quote#, etc...  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """   A total additional charge that is incurred when purchasing this service. Ex(Lot,Setup,Handling,etc...). This is only used with a Subcontract price. It's used as a default to QuoteOpr.MiscCharge, JobOper.MiscCharge and POMisc.MiscAmt
will be defaulted to the This is NOT part of the a Unit Cost. It is NOT consider in the logic of using Minimum Cost.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code related to the MiscCharge field. If MiscCharge <> 0 then must be entered and valid in the PURMisc file.  This will be the MiscCode used to create the PoMisc record when defaults are created in purchase order entry.  """  
      self.CommentText:str = obj["CommentText"]
      """  Additional comments that will be used as a default for purchasing.  View as an EDITOR widget.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """   Overall discount percent. Used to develop an effective unit price.
(BaseUnitPrice + QtyBrkValue) *( (100 - DiscountPercent) * .01)  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Description of Part. Used only for Non Part master parts.  """  
      self.RFQNum:int = obj["RFQNum"]
      """   Related RFQ number.
Note: zero for price breaks entered via master maintenance.  """  
      self.RFQLine:int = obj["RFQLine"]
      """   Related RFQ Line number.
Note: Zero for price breaks created by master maintenance programs.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """   A unique code that identifies the currency.
NOT ACTIVE  AS OF 3.20. RESERVED FOR FUTURE USE.  """  
      self.OnhandQty:int = obj["OnhandQty"]
      """  Suppliers Quantity on Hand  """  
      self.OnHandDate:str = obj["OnHandDate"]
      """  Date Suppliers Quantity was updated  """  
      self.OnHandTime:int = obj["OnHandTime"]
      """  Time Suppliers Quantity was updated  """  
      self.ConNum:int = obj["ConNum"]
      """  Supplier contact linked to this Price  """  
      self.SupplierResponseReady:bool = obj["SupplierResponseReady"]
      """  This is for use in SupplierConnect.  It indicates the Supplier has completed the changes to the RFQ and is ready for the data to be posted back to Epicor.  """  
      self.DefaultPUM:bool = obj["DefaultPUM"]
      """  Indicates if this Supplier Price List will be the default to select a PUM.  """  
      self.ConvOperator:str = obj["ConvOperator"]
      """   Indicates the mathmatical operator that is used for performing the UOM Conversion. Options are "*" (Multiply) or "\" (Divide).
For example for Feet to Inch where Inch is the base uom. 
You could have 1ft / 12 = 1In  """  
      self.ConvFactor:int = obj["ConvFactor"]
      """   Value used to convert to/from base uom for the specific part. Cannot change if it's base uom of UOMClass (always 1.0) Sometimes a unit of measure conversion is relative to a specific part. These are non-standard conversions.
For example; 1 box(bx) of  Part A is 12ea. 1(bx) of Part B is 24ea. Non-standard conversions are defined in the PartUOM table. When ConvOperator = * then ConvFactor is 1 UOM expressed in Base UOM else it is 1 Base UOM expressed in UOM  """  
      self.ConvOverRide:bool = obj["ConvOverRide"]
      """  Purchase Point  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OpCodeDescription:str = obj["OpCodeDescription"]
      self.VendorName:str = obj["VendorName"]
      self.CurrencyCodeDescription:str = obj["CurrencyCodeDescription"]
      self.PrimaryVendor:bool = obj["PrimaryVendor"]
      self.EffectiveDays:int = obj["EffectiveDays"]
      self.VendorID:str = obj["VendorID"]
      self.FromRFQ:str = obj["FromRFQ"]
      """  RFQVend ID  """  
      self.NonPartMaster:bool = obj["NonPartMaster"]
      """  This field is to check when the selected part doesnt exist in the part master. When the part does not exist in the Part Master, this field is set to YES, when the part exists in the part master it is set to NO.  """  
      self.AprvSupplier:bool = obj["AprvSupplier"]
      """  Approved Supplier  """  
      self.AprvForACustomer:bool = obj["AprvForACustomer"]
      """  Supplier Approved for a Customer. It is true when AprvVend.CustNum is not zero.  """  
      self.ConvBaseUOM:str = obj["ConvBaseUOM"]
      """  Base UOM  """  
      self.ConvFromUOM:str = obj["ConvFromUOM"]
      """  ReadOnly field used to clarify converion.  Displayed as one of the uom, ex 1 EA  """  
      self.ConvToUOM:str = obj["ConvToUOM"]
      """  ReadOnly field used to clarify converion.  Displayed as nnnnn.nnnn "base uom"  """  
      self.VendSuppPart:str = obj["VendSuppPart"]
      """  Supplier Part for a Supplier. This is used to assign a Supplier Part to a given Part row.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.MiscCodeLCAmount:int = obj["MiscCodeLCAmount"]
      self.MiscCodeLCDisburseMethod:str = obj["MiscCodeLCDisburseMethod"]
      self.MiscCodeLCCurrencyCode:str = obj["MiscCodeLCCurrencyCode"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.VendorNameAddress3:str = obj["VendorNameAddress3"]
      self.VendorNameVendorID:str = obj["VendorNameVendorID"]
      self.VendorNameCity:str = obj["VendorNameCity"]
      self.VendorNameAddress1:str = obj["VendorNameAddress1"]
      self.VendorNameCurrencyCode:str = obj["VendorNameCurrencyCode"]
      self.VendorNameCountry:str = obj["VendorNameCountry"]
      self.VendorNameAddress2:str = obj["VendorNameAddress2"]
      self.VendorNameName:str = obj["VendorNameName"]
      self.VendorNameZIP:str = obj["VendorNameZIP"]
      self.VendorNameTermsCode:str = obj["VendorNameTermsCode"]
      self.VendorNameState:str = obj["VendorNameState"]
      self.VendorNameDefaultFOB:str = obj["VendorNameDefaultFOB"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeAprvSupplier_input:
   """ Required : 
   ds
   ipAprvSupplier
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      self.ipAprvSupplier:bool = obj["ipAprvSupplier"]
      """  Proposed part number  """  
      pass

class ChangeAprvSupplier_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      self.opExistApprovedSupplier:bool = obj["opExistApprovedSupplier"]
      pass

      """  output parameters  """  

class ChangeConvFactor_input:
   """ Required : 
   pConvFactor
   ds
   """  
   def __init__(self, obj):
      self.pConvFactor:int = obj["pConvFactor"]
      """  Proposed value for ConvFactor  """  
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      pass

class ChangeConvFactor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeConvOperator_input:
   """ Required : 
   pConvOperator
   ds
   """  
   def __init__(self, obj):
      self.pConvOperator:str = obj["pConvOperator"]
      """  Proposed value for ConvOperator  """  
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      pass

class ChangeConvOperator_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeConvOverride_input:
   """ Required : 
   pConvOverride
   ds
   """  
   def __init__(self, obj):
      self.pConvOverride:bool = obj["pConvOverride"]
      """  Proposed value for ConvOverride  """  
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      pass

class ChangeConvOverride_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeEffectiveDays_input:
   """ Required : 
   ds
   cFieldModified
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      self.cFieldModified:str = obj["cFieldModified"]
      """  cFieldModified indicates which field was updated.  Possible values are:
            blank  - indicates we are just getting a value for days
            "days" - indicates the number of days changed; recalculate expiration date
            "eff"  - indicates effective date changed; recalculate expiration date
            "exp"  - indicates expiration date changed; recalculate effective date  """  
      pass

class ChangeEffectiveDays_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeImportExportVendorID_input:
   """ Required : 
   cProposedSupplierID
   ds
   """  
   def __init__(self, obj):
      self.cProposedSupplierID:str = obj["cProposedSupplierID"]
      self.ds:list[Erp_Tablesets_SupListImpExpParamsTableset] = obj["ds"]
      pass

class ChangeImportExportVendorID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SupListImpExpParamsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePart_input:
   """ Required : 
   partNum
   SysRowID
   rowType
   uomCode
   ds
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Proposed PartNumber change  """  
      self.SysRowID:str = obj["SysRowID"]
      self.rowType:str = obj["rowType"]
      """  RowType of the selected record. Only used with sysRowID.  """  
      self.uomCode:str = obj["uomCode"]
      """  UOM Code (only used for Product Codes)  """  
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      pass

class ChangePart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partNum:str = obj["parameters"]
      self.uomCode:str = obj["parameters"]
      self.serialWarning:str = obj["parameters"]
      self.questionString:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePriceModifier_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      pass

class ChangePriceModifier_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeVendPartPUM_input:
   """ Required : 
   ds
   inPUM
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      self.inPUM:str = obj["inPUM"]
      """  Proposed PUM  """  
      pass

class ChangeVendPartPUM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultRFQInfo_input:
   """ Required : 
   rfqRowIDent
   """  
   def __init__(self, obj):
      self.rfqRowIDent:str = obj["rfqRowIDent"]
      """  Supplier Response RowIDent  """  
      pass

class DefaultRFQInfo_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendPartTableset] = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   partNum
   opCode
   puM
   vendorNum
   effectiveDate
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.opCode:str = obj["opCode"]
      self.puM:str = obj["puM"]
      self.vendorNum:int = obj["vendorNum"]
      self.effectiveDate:str = obj["effectiveDate"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_SupListImpExpParamsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.EffectiveDate:str = obj["EffectiveDate"]
      self.VendorID:str = obj["VendorID"]
      self.VendorName:str = obj["VendorName"]
      self.FileName:str = obj["FileName"]
      self.VendorNum:int = obj["VendorNum"]
      self.ListSeparator:str = obj["ListSeparator"]
      """  The delimiter to use in the CSV file.  """  
      self.NumberDecimalSeparator:str = obj["NumberDecimalSeparator"]
      """  The decimal separator used in numerics.  Either a comma(,) or a point(.).  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SupListImpExpParamsTableset:
   def __init__(self, obj):
      self.SupListImpExpParams:list[Erp_Tablesets_SupListImpExpParamsRow] = obj["SupListImpExpParams"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SupplierListImportExportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.PartDescription:str = obj["PartDescription"]
      self.VenPartNum:str = obj["VenPartNum"]
      self.MinimumPrice:int = obj["MinimumPrice"]
      self.BaseUnitPrice:int = obj["BaseUnitPrice"]
      self.DiscountPercent:int = obj["DiscountPercent"]
      self.BreakQty:int = obj["BreakQty"]
      self.BreakPrice:int = obj["BreakPrice"]
      self.PriceFormat:str = obj["PriceFormat"]
      self.PricePerCode:str = obj["PricePerCode"]
      self.LeadTime:int = obj["LeadTime"]
      self.PUM:str = obj["PUM"]
      self.Reference:str = obj["Reference"]
      self.CommentText:str = obj["CommentText"]
      self.ImportErrorMsg:str = obj["ImportErrorMsg"]
      """  Reason import of this record failed.  Blank implies no error occurred.  """  
      self.ImportSeq:int = obj["ImportSeq"]
      self.MfgID:str = obj["MfgID"]
      """  Manufacturer's ID  """  
      self.MfgPartNum:str = obj["MfgPartNum"]
      """  Manufacturer's Part Number.  """  
      self.SupplierPartNum:str = obj["SupplierPartNum"]
      """  Supplier's Part Number.  """  
      self.VendorID:str = obj["VendorID"]
      """  Vendor's ID  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SupplierListImportExportTableset:
   def __init__(self, obj):
      self.SupplierListImportExport:list[Erp_Tablesets_SupplierListImportExportRow] = obj["SupplierListImportExport"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtVendPartTableset:
   def __init__(self, obj):
      self.VendPart:list[Erp_Tablesets_VendPartRow] = obj["VendPart"]
      self.VendPartAttch:list[Erp_Tablesets_VendPartAttchRow] = obj["VendPartAttch"]
      self.VendPBrk:list[Erp_Tablesets_VendPBrkRow] = obj["VendPBrk"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_VendPBrkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies our Part.  """  
      self.OpCode:str = obj["OpCode"]
      """   Operation Code - of the related parent VendPart record.
(See VendPart.OpCode).  """  
      self.PUM:str = obj["PUM"]
      """  Purchasing Unit of measure.  A component of the unique key and parent table (VendPart) relationship.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor's unique internal number.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  The date which this vendor/part information is effective.  """  
      self.BreakQty:int = obj["BreakQty"]
      """  Minimum Quantity required to obtain the related UnitPrice.  This is in Vendor's unit of measure.  """  
      self.PriceModifier:int = obj["PriceModifier"]
      """   This field represents the value used to determine a effective unit price for the related BreakQty.  It can be expressed as a Flat Amount or Percent of Base Price which is determined by the VendPart.PriceFormat field. Negatives are allowed to enter deductions to the base cost.
Effective Unit Price = BasePrice + PriceModifier  """  
      self.DaysOut:int = obj["DaysOut"]
      """  Hours required is calculated as days * 8.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EffectivePrice:int = obj["EffectivePrice"]
      self.BitFlag:int = obj["BitFlag"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendPartAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.OpCode:str = obj["OpCode"]
      self.PUM:str = obj["PUM"]
      self.VendorNum:int = obj["VendorNum"]
      self.EffectiveDate:str = obj["EffectiveDate"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendPartListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies our Part.  """  
      self.OpCode:str = obj["OpCode"]
      """   Operation Code - this is a component of the index which uniquely identifies the record.  Used to identify specific subcontracting operations prices  for a Part/Vendor.
This field can be blank (raw materials) or must be valid in the OpMaster (subcontracts).  """  
      self.PUM:str = obj["PUM"]
      """   The Purchasing Unit of measure for the Part from the vendor.
Defaulted from Part.PUM.  This is used in Purchase Order entry as the default on line item details.  It Overrides Part.PUM  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  The date which this vendor/part information is effective.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor's unique internal number.  """  
      self.LeadTime:int = obj["LeadTime"]
      """  Used to record the normal  order lead time that this vendor gives for this part. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  """  
      self.BaseUnitPrice:int = obj["BaseUnitPrice"]
      """   BaseUnitPrice + VendPBrk.UnitPrice = Unit Price for the Part.  This design allows users to enter "Qty Break Unit Prices" (VendPBrk.UnitPrice) either as a price that should be Added or Subtracted (negatives) to Base or as a true Unit Price(Base = 0).  This is an attempt to make it easier to enter prices from varying formats of vendor price lists.
Some vendors define their prices as a Base Unit Price with an additional amount to be added/deducted to it at specific quantities levels.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Part number that the Vendor uses to identify the item.  """  
      self.PriceFormat:str = obj["PriceFormat"]
      """  Indicates the format of UnitPrices in VendPBrk table.  This can either be "$" = Flat Unit Price, or "%" = Percent of Base.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """   Indicates the vendor's pricing per value for the part.                     "E" = per each, "C" = per hundred,  "M" = per thousand.
Used as a default in purchasing, also used to convert a vendor unit price to our unit costs.
Basic formula for converting to "our unit cost" is as follows...
Our Unit$ = Vendor Unit$ / Cost Per factor) * PurchasingFactor.  """  
      self.MinimumPrice:int = obj["MinimumPrice"]
      """   Minimum Charge for this material.  This is used as a default to QuoteMtl.MinimumCost, QuoteOpr.MinimumCost.  In routines used to retrieve a default unit cost (PO, Jobs..) the Manufacturing System  will take the greater of (required quantity * unit cost) or (MinimumCost).
Note: The AddlCharge is not included in the above formula.  """  
      self.ExpirationDate:str = obj["ExpirationDate"]
      """  Optional Expiration date of this cost information.  The Manufacturing System uses this date to inform the user when the cost information that is being used has expired.  This is an indicator that this information may not be accurate and should be reconfirmed with the vendor.  """  
      self.Reference:str = obj["Reference"]
      """  An optional field that may be used for any reference to this vendors costing info. Ex: RFQ, Quote#, etc...  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """   A total additional charge that is incurred when purchasing this service. Ex(Lot,Setup,Handling,etc...). This is only used with a Subcontract price. It's used as a default to QuoteOpr.MiscCharge, JobOper.MiscCharge and POMisc.MiscAmt
will be defaulted to the This is NOT part of the a Unit Cost. It is NOT consider in the logic of using Minimum Cost.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code related to the MiscCharge field. If MiscCharge <> 0 then must be entered and valid in the PURMisc file.  This will be the MiscCode used to create the PoMisc record when defaults are created in purchase order entry.  """  
      self.CommentText:str = obj["CommentText"]
      """  Additional comments that will be used as a default for purchasing.  View as an EDITOR widget.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """   Overall discount percent. Used to develop an effective unit price.
(BaseUnitPrice + QtyBrkValue) *( (100 - DiscountPercent) * .01)  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Description of Part. Used only for Non Part master parts.  """  
      self.RFQNum:int = obj["RFQNum"]
      """   Related RFQ number.
Note: zero for price breaks entered via master maintenance.  """  
      self.RFQLine:int = obj["RFQLine"]
      """   Related RFQ Line number.
Note: Zero for price breaks created by master maintenance programs.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """   A unique code that identifies the currency.
NOT ACTIVE  AS OF 3.20. RESERVED FOR FUTURE USE.  """  
      self.OnhandQty:int = obj["OnhandQty"]
      """  Suppliers Quantity on Hand  """  
      self.OnHandDate:str = obj["OnHandDate"]
      """  Date Suppliers Quantity was updated  """  
      self.OnHandTime:int = obj["OnHandTime"]
      """  Time Suppliers Quantity was updated  """  
      self.ConNum:int = obj["ConNum"]
      """  Supplier contact linked to this Price  """  
      self.SupplierResponseReady:bool = obj["SupplierResponseReady"]
      """  This is for use in SupplierConnect.  It indicates the Supplier has completed the changes to the RFQ and is ready for the data to be posted back to Epicor.  """  
      self.DefaultPUM:bool = obj["DefaultPUM"]
      """  Indicates if this Supplier Price List will be the default to select a PUM.  """  
      self.ConvOperator:str = obj["ConvOperator"]
      """   Indicates the mathmatical operator that is used for performing the UOM Conversion. Options are "*" (Multiply) or "\" (Divide).
For example for Feet to Inch where Inch is the base uom. 
You could have 1ft / 12 = 1In  """  
      self.ConvFactor:int = obj["ConvFactor"]
      """   Value used to convert to/from base uom for the specific part. Cannot change if it's base uom of UOMClass (always 1.0) Sometimes a unit of measure conversion is relative to a specific part. These are non-standard conversions.
For example; 1 box(bx) of  Part A is 12ea. 1(bx) of Part B is 24ea. Non-standard conversions are defined in the PartUOM table. When ConvOperator = * then ConvFactor is 1 UOM expressed in Base UOM else it is 1 Base UOM expressed in UOM  """  
      self.ConvOverRide:bool = obj["ConvOverRide"]
      """  Purchase Point  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OpCodeDescription:str = obj["OpCodeDescription"]
      self.VendorName:str = obj["VendorName"]
      self.CurrencyCodeDescription:str = obj["CurrencyCodeDescription"]
      self.PrimaryVendor:bool = obj["PrimaryVendor"]
      self.EffectiveDays:int = obj["EffectiveDays"]
      self.VendorID:str = obj["VendorID"]
      self.FromRFQ:str = obj["FromRFQ"]
      """  RFQVend ID  """  
      self.NonPartMaster:bool = obj["NonPartMaster"]
      """  This field is to check when the selected part doesnt exist in the part master. When the part does not exist in the Part Master, this field is set to YES, when the part exists in the part master it is set to NO.  """  
      self.AprvSupplier:bool = obj["AprvSupplier"]
      """  Approved Supplier  """  
      self.AprvForACustomer:bool = obj["AprvForACustomer"]
      """  Supplier Approved for a Customer. It is true when AprvVend.CustNum is not zero.  """  
      self.ConvBaseUOM:str = obj["ConvBaseUOM"]
      """  Base UOM  """  
      self.ConvFromUOM:str = obj["ConvFromUOM"]
      """  ReadOnly field used to clarify converion.  Displayed as one of the uom, ex 1 EA  """  
      self.ConvToUOM:str = obj["ConvToUOM"]
      """  ReadOnly field used to clarify converion.  Displayed as nnnnn.nnnn "base uom"  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      """  Description of the Miscellaneous Charge. Used as a default to Orders and Invoices.  """  
      self.MiscCodeLCDisburseMethod:str = obj["MiscCodeLCDisburseMethod"]
      """  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  """  
      self.MiscCodeLCAmount:int = obj["MiscCodeLCAmount"]
      """  Landed Cost amount in the specified document currency.  This will be the default when this miscellaneous charge is used as Indirect Cost during receipts.  """  
      self.MiscCodeLCCurrencyCode:str = obj["MiscCodeLCCurrencyCode"]
      """  The Landed Cost Currency Code for this miscellaneous charge.  """  
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      """  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.VendorNameTermsCode:str = obj["VendorNameTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNameCountry:str = obj["VendorNameCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNameAddress2:str = obj["VendorNameAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNameName:str = obj["VendorNameName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNameVendorID:str = obj["VendorNameVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNameAddress3:str = obj["VendorNameAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNameCurrencyCode:str = obj["VendorNameCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNameState:str = obj["VendorNameState"]
      """  Can be blank.  """  
      self.VendorNameZIP:str = obj["VendorNameZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNameAddress1:str = obj["VendorNameAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNameCity:str = obj["VendorNameCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNameDefaultFOB:str = obj["VendorNameDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendPartListTableset:
   def __init__(self, obj):
      self.VendPartList:list[Erp_Tablesets_VendPartListRow] = obj["VendPartList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_VendPartRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies our Part.  """  
      self.OpCode:str = obj["OpCode"]
      """   Operation Code - this is a component of the index which uniquely identifies the record.  Used to identify specific subcontracting operations prices  for a Part/Vendor.
This field can be blank (raw materials) or must be valid in the OpMaster (subcontracts).  """  
      self.PUM:str = obj["PUM"]
      """   The Purchasing Unit of measure for the Part from the vendor.
Defaulted from Part.PUM.  This is used in Purchase Order entry as the default on line item details.  It Overrides Part.PUM  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  The date which this vendor/part information is effective.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor's unique internal number.  """  
      self.LeadTime:int = obj["LeadTime"]
      """  Used to record the normal  order lead time that this vendor gives for this part. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  """  
      self.BaseUnitPrice:int = obj["BaseUnitPrice"]
      """   BaseUnitPrice + VendPBrk.UnitPrice = Unit Price for the Part.  This design allows users to enter "Qty Break Unit Prices" (VendPBrk.UnitPrice) either as a price that should be Added or Subtracted (negatives) to Base or as a true Unit Price(Base = 0).  This is an attempt to make it easier to enter prices from varying formats of vendor price lists.
Some vendors define their prices as a Base Unit Price with an additional amount to be added/deducted to it at specific quantities levels.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Part number that the Vendor uses to identify the item.  """  
      self.PriceFormat:str = obj["PriceFormat"]
      """  Indicates the format of UnitPrices in VendPBrk table.  This can either be "$" = Flat Unit Price, or "%" = Percent of Base.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """   Indicates the vendor's pricing per value for the part.                     "E" = per each, "C" = per hundred,  "M" = per thousand.
Used as a default in purchasing, also used to convert a vendor unit price to our unit costs.
Basic formula for converting to "our unit cost" is as follows...
Our Unit$ = Vendor Unit$ / Cost Per factor) * PurchasingFactor.  """  
      self.MinimumPrice:int = obj["MinimumPrice"]
      """   Minimum Charge for this material.  This is used as a default to QuoteMtl.MinimumCost, QuoteOpr.MinimumCost.  In routines used to retrieve a default unit cost (PO, Jobs..) the Manufacturing System  will take the greater of (required quantity * unit cost) or (MinimumCost).
Note: The AddlCharge is not included in the above formula.  """  
      self.ExpirationDate:str = obj["ExpirationDate"]
      """  Optional Expiration date of this cost information.  The Manufacturing System uses this date to inform the user when the cost information that is being used has expired.  This is an indicator that this information may not be accurate and should be reconfirmed with the vendor.  """  
      self.Reference:str = obj["Reference"]
      """  An optional field that may be used for any reference to this vendors costing info. Ex: RFQ, Quote#, etc...  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """   A total additional charge that is incurred when purchasing this service. Ex(Lot,Setup,Handling,etc...). This is only used with a Subcontract price. It's used as a default to QuoteOpr.MiscCharge, JobOper.MiscCharge and POMisc.MiscAmt
will be defaulted to the This is NOT part of the a Unit Cost. It is NOT consider in the logic of using Minimum Cost.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code related to the MiscCharge field. If MiscCharge <> 0 then must be entered and valid in the PURMisc file.  This will be the MiscCode used to create the PoMisc record when defaults are created in purchase order entry.  """  
      self.CommentText:str = obj["CommentText"]
      """  Additional comments that will be used as a default for purchasing.  View as an EDITOR widget.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """   Overall discount percent. Used to develop an effective unit price.
(BaseUnitPrice + QtyBrkValue) *( (100 - DiscountPercent) * .01)  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Description of Part. Used only for Non Part master parts.  """  
      self.RFQNum:int = obj["RFQNum"]
      """   Related RFQ number.
Note: zero for price breaks entered via master maintenance.  """  
      self.RFQLine:int = obj["RFQLine"]
      """   Related RFQ Line number.
Note: Zero for price breaks created by master maintenance programs.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """   A unique code that identifies the currency.
NOT ACTIVE  AS OF 3.20. RESERVED FOR FUTURE USE.  """  
      self.OnhandQty:int = obj["OnhandQty"]
      """  Suppliers Quantity on Hand  """  
      self.OnHandDate:str = obj["OnHandDate"]
      """  Date Suppliers Quantity was updated  """  
      self.OnHandTime:int = obj["OnHandTime"]
      """  Time Suppliers Quantity was updated  """  
      self.ConNum:int = obj["ConNum"]
      """  Supplier contact linked to this Price  """  
      self.SupplierResponseReady:bool = obj["SupplierResponseReady"]
      """  This is for use in SupplierConnect.  It indicates the Supplier has completed the changes to the RFQ and is ready for the data to be posted back to Epicor.  """  
      self.DefaultPUM:bool = obj["DefaultPUM"]
      """  Indicates if this Supplier Price List will be the default to select a PUM.  """  
      self.ConvOperator:str = obj["ConvOperator"]
      """   Indicates the mathmatical operator that is used for performing the UOM Conversion. Options are "*" (Multiply) or "\" (Divide).
For example for Feet to Inch where Inch is the base uom. 
You could have 1ft / 12 = 1In  """  
      self.ConvFactor:int = obj["ConvFactor"]
      """   Value used to convert to/from base uom for the specific part. Cannot change if it's base uom of UOMClass (always 1.0) Sometimes a unit of measure conversion is relative to a specific part. These are non-standard conversions.
For example; 1 box(bx) of  Part A is 12ea. 1(bx) of Part B is 24ea. Non-standard conversions are defined in the PartUOM table. When ConvOperator = * then ConvFactor is 1 UOM expressed in Base UOM else it is 1 Base UOM expressed in UOM  """  
      self.ConvOverRide:bool = obj["ConvOverRide"]
      """  Purchase Point  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OpCodeDescription:str = obj["OpCodeDescription"]
      self.VendorName:str = obj["VendorName"]
      self.CurrencyCodeDescription:str = obj["CurrencyCodeDescription"]
      self.PrimaryVendor:bool = obj["PrimaryVendor"]
      self.EffectiveDays:int = obj["EffectiveDays"]
      self.VendorID:str = obj["VendorID"]
      self.FromRFQ:str = obj["FromRFQ"]
      """  RFQVend ID  """  
      self.NonPartMaster:bool = obj["NonPartMaster"]
      """  This field is to check when the selected part doesnt exist in the part master. When the part does not exist in the Part Master, this field is set to YES, when the part exists in the part master it is set to NO.  """  
      self.AprvSupplier:bool = obj["AprvSupplier"]
      """  Approved Supplier  """  
      self.AprvForACustomer:bool = obj["AprvForACustomer"]
      """  Supplier Approved for a Customer. It is true when AprvVend.CustNum is not zero.  """  
      self.ConvBaseUOM:str = obj["ConvBaseUOM"]
      """  Base UOM  """  
      self.ConvFromUOM:str = obj["ConvFromUOM"]
      """  ReadOnly field used to clarify converion.  Displayed as one of the uom, ex 1 EA  """  
      self.ConvToUOM:str = obj["ConvToUOM"]
      """  ReadOnly field used to clarify converion.  Displayed as nnnnn.nnnn "base uom"  """  
      self.VendSuppPart:str = obj["VendSuppPart"]
      """  Supplier Part for a Supplier. This is used to assign a Supplier Part to a given Part row.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.MiscCodeLCAmount:int = obj["MiscCodeLCAmount"]
      self.MiscCodeLCDisburseMethod:str = obj["MiscCodeLCDisburseMethod"]
      self.MiscCodeLCCurrencyCode:str = obj["MiscCodeLCCurrencyCode"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.VendorNameAddress3:str = obj["VendorNameAddress3"]
      self.VendorNameVendorID:str = obj["VendorNameVendorID"]
      self.VendorNameCity:str = obj["VendorNameCity"]
      self.VendorNameAddress1:str = obj["VendorNameAddress1"]
      self.VendorNameCurrencyCode:str = obj["VendorNameCurrencyCode"]
      self.VendorNameCountry:str = obj["VendorNameCountry"]
      self.VendorNameAddress2:str = obj["VendorNameAddress2"]
      self.VendorNameName:str = obj["VendorNameName"]
      self.VendorNameZIP:str = obj["VendorNameZIP"]
      self.VendorNameTermsCode:str = obj["VendorNameTermsCode"]
      self.VendorNameState:str = obj["VendorNameState"]
      self.VendorNameDefaultFOB:str = obj["VendorNameDefaultFOB"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendPartTableset:
   def __init__(self, obj):
      self.VendPart:list[Erp_Tablesets_VendPartRow] = obj["VendPart"]
      self.VendPartAttch:list[Erp_Tablesets_VendPartAttchRow] = obj["VendPartAttch"]
      self.VendPBrk:list[Erp_Tablesets_VendPBrkRow] = obj["VendPBrk"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExportSupplierListToServerFile_input:
   """ Required : 
   ds
   dsParams
   dtEffectiveDate
   cSupplierID
   serverFileName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SupplierListImportExportTableset] = obj["ds"]
      self.dsParams:list[Erp_Tablesets_SupListImpExpParamsTableset] = obj["dsParams"]
      self.dtEffectiveDate:str = obj["dtEffectiveDate"]
      """  Effective Date  """  
      self.cSupplierID:str = obj["cSupplierID"]
      """  Supplier Code  """  
      self.serverFileName:str = obj["serverFileName"]
      pass

class ExportSupplierListToServerFile_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  returns the name of the saved file on the server  """  
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SupplierListImportExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ExportSupplierList_input:
   """ Required : 
   ds
   dtEffectiveDate
   cSupplierID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SupplierListImportExportTableset] = obj["ds"]
      self.dtEffectiveDate:str = obj["dtEffectiveDate"]
      """  Effective Date  """  
      self.cSupplierID:str = obj["cSupplierID"]
      """  Supplier Code  """  
      pass

class ExportSupplierList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SupplierListImportExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetActiveParts_input:
   """ Required : 
   vendorNum
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      pass

class GetActiveParts_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendPartTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   partNum
   opCode
   puM
   vendorNum
   effectiveDate
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.opCode:str = obj["opCode"]
      self.puM:str = obj["puM"]
      self.vendorNum:int = obj["vendorNum"]
      self.effectiveDate:str = obj["effectiveDate"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendPartTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_VendPartTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_VendPartTableset] = obj["returnObj"]
      pass

class GetDefaultRFQInfo_input:
   """ Required : 
   ds
   rfqRowIDent
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      self.rfqRowIDent:str = obj["rfqRowIDent"]
      """  Supplier Response RowIDent  """  
      pass

class GetDefaultRFQInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetImportSupplierListFromServerFile_input:
   """ Required : 
   ds
   dsParams
   serverFileName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SupplierListImportExportTableset] = obj["ds"]
      self.dsParams:list[Erp_Tablesets_SupListImpExpParamsTableset] = obj["dsParams"]
      self.serverFileName:str = obj["serverFileName"]
      pass

class GetImportSupplierListFromServerFile_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SupplierListImportExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetLastEffectiveVendPart_input:
   """ Required : 
   iVendorNum
   cPartNum
   cOpCode
   cPUM
   dtEffDate
   """  
   def __init__(self, obj):
      self.iVendorNum:int = obj["iVendorNum"]
      """  The Vendor Number to retrieve the dataset for  """  
      self.cPartNum:str = obj["cPartNum"]
      """  The Part Number to retrieve the dataset for  """  
      self.cOpCode:str = obj["cOpCode"]
      """  The OpCode to retrieve the dataset for  """  
      self.cPUM:str = obj["cPUM"]
      """  The UOM to retrieve the dataset for  """  
      self.dtEffDate:str = obj["dtEffDate"]
      """  The Date to retrieve the dataset for  """  
      pass

class GetLastEffectiveVendPart_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendPartTableset] = obj["returnObj"]
      pass

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
      self.returnObj:list[Erp_Tablesets_VendPartListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewSupListImpExpParams_input:
   """ Required : 
   cSupplierID
   """  
   def __init__(self, obj):
      self.cSupplierID:str = obj["cSupplierID"]
      pass

class GetNewSupListImpExpParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SupListImpExpParamsTableset] = obj["returnObj"]
      pass

class GetNewVendPBrk_input:
   """ Required : 
   ds
   partNum
   opCode
   puM
   vendorNum
   effectiveDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      self.opCode:str = obj["opCode"]
      self.puM:str = obj["puM"]
      self.vendorNum:int = obj["vendorNum"]
      self.effectiveDate:str = obj["effectiveDate"]
      pass

class GetNewVendPBrk_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewVendPartAttch_input:
   """ Required : 
   ds
   partNum
   opCode
   puM
   vendorNum
   effectiveDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      self.opCode:str = obj["opCode"]
      self.puM:str = obj["puM"]
      self.vendorNum:int = obj["vendorNum"]
      self.effectiveDate:str = obj["effectiveDate"]
      pass

class GetNewVendPartAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewVendPart_input:
   """ Required : 
   ds
   partNum
   opCode
   puM
   vendorNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      self.opCode:str = obj["opCode"]
      self.puM:str = obj["puM"]
      self.vendorNum:int = obj["vendorNum"]
      pass

class GetNewVendPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPrimaryVendorNum_input:
   """ Required : 
   iPartNum
   """  
   def __init__(self, obj):
      self.iPartNum:str = obj["iPartNum"]
      """  Input: The part num  """  
      pass

class GetPrimaryVendorNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.oVendorNum:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseVendPart
   whereClauseVendPartAttch
   whereClauseVendPBrk
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseVendPart:str = obj["whereClauseVendPart"]
      self.whereClauseVendPartAttch:str = obj["whereClauseVendPartAttch"]
      self.whereClauseVendPBrk:str = obj["whereClauseVendPBrk"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendPartTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetVendPartByPart_input:
   """ Required : 
   cPartNum
   """  
   def __init__(self, obj):
      self.cPartNum:str = obj["cPartNum"]
      """  The Part Number to retrieve the dataset for  """  
      pass

class GetVendPartByPart_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendPartTableset] = obj["returnObj"]
      pass

class GetVendPartByVendNumPart_input:
   """ Required : 
   iVendorNum
   cPartNum
   """  
   def __init__(self, obj):
      self.iVendorNum:int = obj["iVendorNum"]
      """  The Vendor Number to retrieve the dataset for  """  
      self.cPartNum:str = obj["cPartNum"]
      """  The Part Number to retrieve the dataset for  """  
      pass

class GetVendPartByVendNumPart_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendPartTableset] = obj["returnObj"]
      pass

class GetVendPartByVendor_input:
   """ Required : 
   VendNum
   ds
   """  
   def __init__(self, obj):
      self.VendNum:int = obj["VendNum"]
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      pass

class GetVendPartByVendor_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  The VendPart data set  """  
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetVendPartIndexEffectiveRecord_input:
   """ Required : 
   VendorNum
   PartNum
   """  
   def __init__(self, obj):
      self.VendorNum:int = obj["VendorNum"]
      self.PartNum:str = obj["PartNum"]
      pass

class GetVendPartIndexEffectiveRecord_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendPartTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.VendPartIndex:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetVendorNum_input:
   """ Required : 
   cVendorID
   """  
   def __init__(self, obj):
      self.cVendorID:str = obj["cVendorID"]
      """  The Vendor ID  """  
      pass

class GetVendorNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.iVendorNum:int = obj["parameters"]
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

class ImportSupplierList_input:
   """ Required : 
   ds
   dtEffectiveDate
   cSupplierID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SupplierListImportExportTableset] = obj["ds"]
      self.dtEffectiveDate:str = obj["dtEffectiveDate"]
      """  Effective Date  """  
      self.cSupplierID:str = obj["cSupplierID"]
      """  Supplier Code  """  
      pass

class ImportSupplierList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SupplierListImportExportTableset] = obj["ds"]
      self.numRecsImported:int = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateAprvSupplier_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      pass

class UpdateAprvSupplier_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtVendPartTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtVendPartTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendPartTableset] = obj["ds"]
      pass

      """  output parameters  """  

