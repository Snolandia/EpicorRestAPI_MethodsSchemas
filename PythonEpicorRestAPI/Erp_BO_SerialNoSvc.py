import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.SerialNoSvc
# Description: Update the SerialNo table. Update the Part Table for
Serial number format changes.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_SerialNoes(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SerialNoes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SerialNoes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SerialNoRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoes",headers=creds) as resp:
           return await resp.json()

async def post_SerialNoes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SerialNoes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SerialNoRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SerialNoRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SerialNoes_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SerialNo item
   Description: Calls GetByID to retrieve the SerialNo item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SerialNo
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SerialNoRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoes(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SerialNoes_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SerialNo for the service
   Description: Calls UpdateExt to update SerialNo. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SerialNo
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SerialNoRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoes(" + Company + "," + PartNum + "," + SerialNumber + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SerialNoes_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SerialNo item
   Description: Call UpdateExt to delete SerialNo item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SerialNo
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoes(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def get_SerialNoes_Company_PartNum_SerialNumber_SerialNoConditions(Company, PartNum, SerialNumber, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SerialNoConditions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SerialNoConditions1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SerialNoConditionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoes(" + Company + "," + PartNum + "," + SerialNumber + ")/SerialNoConditions",headers=creds) as resp:
           return await resp.json()

async def get_SerialNoes_Company_PartNum_SerialNumber_SerialNoConditions_Company_PartNum_SerialNumber_FSConditionID(Company, PartNum, SerialNumber, FSConditionID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SerialNoCondition item
   Description: Calls GetByID to retrieve the SerialNoCondition item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SerialNoCondition1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param FSConditionID: Desc: FSConditionID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SerialNoConditionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoes(" + Company + "," + PartNum + "," + SerialNumber + ")/SerialNoConditions(" + Company + "," + PartNum + "," + SerialNumber + "," + FSConditionID + ")",headers=creds) as resp:
           return await resp.json()

async def get_SerialNoes_Company_PartNum_SerialNumber_SerialNoAttches(Company, PartNum, SerialNumber, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SerialNoAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SerialNoAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SerialNoAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoes(" + Company + "," + PartNum + "," + SerialNumber + ")/SerialNoAttches",headers=creds) as resp:
           return await resp.json()

async def get_SerialNoes_Company_PartNum_SerialNumber_SerialNoAttches_Company_PartNum_SerialNumber_DrawingSeq(Company, PartNum, SerialNumber, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SerialNoAttch item
   Description: Calls GetByID to retrieve the SerialNoAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SerialNoAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SerialNoAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoes(" + Company + "," + PartNum + "," + SerialNumber + ")/SerialNoAttches(" + Company + "," + PartNum + "," + SerialNumber + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_SerialNoConditions(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SerialNoConditions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SerialNoConditions
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SerialNoConditionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoConditions",headers=creds) as resp:
           return await resp.json()

async def post_SerialNoConditions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SerialNoConditions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SerialNoConditionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SerialNoConditionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoConditions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SerialNoConditions_Company_PartNum_SerialNumber_FSConditionID(Company, PartNum, SerialNumber, FSConditionID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SerialNoCondition item
   Description: Calls GetByID to retrieve the SerialNoCondition item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SerialNoCondition
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param FSConditionID: Desc: FSConditionID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SerialNoConditionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoConditions(" + Company + "," + PartNum + "," + SerialNumber + "," + FSConditionID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SerialNoConditions_Company_PartNum_SerialNumber_FSConditionID(Company, PartNum, SerialNumber, FSConditionID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SerialNoCondition for the service
   Description: Calls UpdateExt to update SerialNoCondition. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SerialNoCondition
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param FSConditionID: Desc: FSConditionID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SerialNoConditionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoConditions(" + Company + "," + PartNum + "," + SerialNumber + "," + FSConditionID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SerialNoConditions_Company_PartNum_SerialNumber_FSConditionID(Company, PartNum, SerialNumber, FSConditionID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SerialNoCondition item
   Description: Call UpdateExt to delete SerialNoCondition item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SerialNoCondition
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param FSConditionID: Desc: FSConditionID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoConditions(" + Company + "," + PartNum + "," + SerialNumber + "," + FSConditionID + ")",headers=creds) as resp:
           return await resp.json()

async def get_SerialNoAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SerialNoAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SerialNoAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SerialNoAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoAttches",headers=creds) as resp:
           return await resp.json()

async def post_SerialNoAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SerialNoAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SerialNoAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SerialNoAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SerialNoAttches_Company_PartNum_SerialNumber_DrawingSeq(Company, PartNum, SerialNumber, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SerialNoAttch item
   Description: Calls GetByID to retrieve the SerialNoAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SerialNoAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SerialNoAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoAttches(" + Company + "," + PartNum + "," + SerialNumber + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SerialNoAttches_Company_PartNum_SerialNumber_DrawingSeq(Company, PartNum, SerialNumber, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SerialNoAttch for the service
   Description: Calls UpdateExt to update SerialNoAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SerialNoAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SerialNoAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoAttches(" + Company + "," + PartNum + "," + SerialNumber + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SerialNoAttches_Company_PartNum_SerialNumber_DrawingSeq(Company, PartNum, SerialNumber, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SerialNoAttch item
   Description: Call UpdateExt to delete SerialNoAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SerialNoAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoAttches(" + Company + "," + PartNum + "," + SerialNumber + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SerialNoListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseSerialNo, whereClauseSerialNoAttch, whereClauseSerialNoCondition, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseSerialNo=" + whereClauseSerialNo
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSerialNoAttch=" + whereClauseSerialNoAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSerialNoCondition=" + whereClauseSerialNoCondition
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(partNum, serialNumber, epicorHeaders = None):
   """  
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
   params += "serialNumber=" + serialNumber

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeAssemblySeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeAssemblySeq
   Description: Method to call when changing the AssemblySeq.
   OperationID: ChangeAssemblySeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAssemblySeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAssemblySeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeAssemblySeqAssetCond(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeAssemblySeqAssetCond
   Description: Method to call when changing the AssemblySeq in Mobile Asset Condition.
   OperationID: ChangeAssemblySeqAssetCond
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAssemblySeqAssetCond_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAssemblySeqAssetCond_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCustomerID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCustomerID
   Description: Method to call when changing the CustID, passing a blank CustID clears the related fields.
   OperationID: ChangeCustomerID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCustomerID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCustomerID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDMRAction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDMRAction
   Description: Method to call when changing the DMRAction.
   OperationID: ChangeDMRAction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDMRAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDMRAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDMRNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDMRNum
   Description: Method to call when changing the DMRNum, passing a 0 clears the related fields.
   OperationID: ChangeDMRNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDMRNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDMRNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeJobNum
   Description: Method to call when changing the JobNum, passing a blank JobNum clears the related fields.
   OperationID: ChangeJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeJobNumAssetCond(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeJobNumAssetCond
   Description: Method to call when changing the JobNum in Mobile Asset Condition, passing a blank JobNum clears the related fields.
   OperationID: ChangeJobNumAssetCond
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeJobNumAssetCond_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJobNumAssetCond_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeMtlSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeMtlSeq
   Description: Method to call when changing the MtlSeq.
   OperationID: ChangeMtlSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMtlSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMtlSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOprSeqAssetCond(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOprSeqAssetCond
   Description: Method to call when changing the OprSeq.
   OperationID: ChangeOprSeqAssetCond
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOprSeqAssetCond_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOprSeqAssetCond_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePackLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePackLine
   Description: Method to call when changing the Ship To PackLine.
   OperationID: ChangePackLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePackLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePackLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePackNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePackNum
   Description: Method to call when changing the Ship To PackNum, passing 0 clears the PackLine.
   OperationID: ChangePackNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePackNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePackNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePackSlip(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePackSlip
   Description: Method to call when changing the Receiving PackSlip, passing a blank PackSlip clears the PackSlipLine.
   OperationID: ChangePackSlip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePackSlip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePackSlip_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePackSlipLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePackSlipLine
   Description: Method to call when changing the Receiving PackSlipLine.
   OperationID: ChangePackSlipLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePackSlipLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePackSlipLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePartNum
   Description: Call this method when the SerialNo.PartNum changes.
   OperationID: ChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePCID
   Description: Call this method when the SerialNo.PCID changes.
   OperationID: ChangePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRMALine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRMALine
   Description: Method to call when changing the RMALine.
   OperationID: ChangeRMALine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRMALine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRMALine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRMANum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRMANum
   Description: Method to call when changing the RMANum, passing a 0 clears the related fields.
   OperationID: ChangeRMANum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRMANum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRMANum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRMAReceipt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRMAReceipt
   Description: Method to call when changing the RMAReceipt.
   OperationID: ChangeRMAReceipt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRMAReceipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRMAReceipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeShipToCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeShipToCustID
   Description: Method to call when changing the ShipToCustID.
   OperationID: ChangeShipToCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipToCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipToCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeShipToNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeShipToNum
   Description: Method to call when changing the ShipToNum.
   OperationID: ChangeShipToNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeUseOTS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeUseOTS
   OperationID: ChangeUseOTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeUseOTS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUseOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVendorID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVendorID
   Description: Method to call when changing the VendorID, passing a blank VendorID clears the related fields.
   OperationID: ChangeVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVendorPP(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVendorPP
   Description: Method to call when changing the VendorPP.
   OperationID: ChangeVendorPP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendorPP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendorPP_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FindPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindPart
   OperationID: FindPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartFromRowId(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartFromRowId
   OperationID: GetPartFromRowId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartFromRowId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartFromRowId_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListForOperation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListForOperation
   Description: Purpose:  Call normal getlist and then filter out completed serial/operations
   OperationID: GetListForOperation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForOperation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForOperation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListInclReassigned(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListInclReassigned
   Description: Purpose:  To find serial numbers related to a given job number.
   OperationID: GetListInclReassigned
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListInclReassigned_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListInclReassigned_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListCustom
   Description: Custom GetList method to allow sort by Customer ID and Name.
   OperationID: GetListCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListServiceCall(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListServiceCall
   Description: Purpose:  Call normal getlist and then filter by given contract/line.
   OperationID: GetListServiceCall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListServiceCall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListServiceCall_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartXRefInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartXRefInfo
   Description: This method defaults PartAdvisor fields when the PartNum field changes
   OperationID: GetPartXRefInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartXRefInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartXRefInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsPerPlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsPerPlant
   Description: Gets the SerialNo dataset using a string with a WHERE clause and Plant as parameters to execute the query.
   OperationID: GetRowsPerPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsPerPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsPerPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsPerPlantKinetic(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsPerPlantKinetic
   Description: Gets the SerialNo dataset using Tracker parameters
   OperationID: GetRowsPerPlantKinetic
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsPerPlantKinetic_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsPerPlantKinetic_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsServiceCall(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsServiceCall
   Description: Purpose:  Gets the SerialNo dataset for Service Call Center
   OperationID: GetRowsServiceCall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsServiceCall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsServiceCall_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSerialsForCustShipTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSerialsForCustShipTracker
   Description: Purpose:  To find serials that were shipped on a given pack number.
   OperationID: GetSerialsForCustShipTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSerialsForCustShipTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSerialsForCustShipTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PlantSerialTracking(epicorHeaders = None):
   """  
   Summary: Invoke method PlantSerialTracking
   Description: Verifies if the current login plant is set for Serial Tracking
   OperationID: PlantSerialTracking
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/PlantSerialTracking_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ChangeToData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeToData
   Description: Updates the ToCustNum and FullToShipToAddr fields, based either on the OTS status and OrderNum or the CustID/ShipTo
   OperationID: ChangeToData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeToData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeToData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FormatOTSAddress(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FormatOTSAddress
   Description: Updates FullToShipToAddr with the data stored on the OTS Fields (display only)
   OperationID: FormatOTSAddress
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FormatOTSAddress_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FormatOTSAddress_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SerialNumberExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SerialNumberExists
   Description: Verifies if a Serial Number exists in the Database.
   OperationID: SerialNumberExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SerialNumberExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SerialNumberExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsPerPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsPerPCID
   Description: Gets the SerialNo dataset by PCID. This method will search for any PCID child items and retrieve their SerialNo.
   OperationID: GetRowsPerPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsPerPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsPerPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSerialsForJobTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSerialsForJobTracker
   Description: Purpose:  To find serials that were ever associated with a given job number.
   OperationID: GetSerialsForJobTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSerialsForJobTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSerialsForJobTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSerialNumbersNotCompleted(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSerialNumbersNotCompleted
   Description: Gets serial numbers not completed
   OperationID: GetSerialNumbersNotCompleted
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSerialNumbersNotCompleted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSerialNumbersNotCompleted_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateOTSTaxID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateOTSTaxID
   Description: One Time Ship To Tax Id validation
   OperationID: ValidateOTSTaxID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateOTSTaxID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateOTSTaxID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingAttributeSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingAttributeSet
   Description: Call this method when the attribute set changes
   OperationID: OnChangingAttributeSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSerialNo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSerialNo
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSerialNo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSerialNo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSerialNo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSerialNoAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSerialNoAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSerialNoAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSerialNoAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSerialNoAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSerialNoCondition(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSerialNoCondition
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSerialNoCondition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSerialNoCondition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSerialNoCondition_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialNoAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SerialNoAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialNoConditionRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SerialNoConditionRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialNoListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SerialNoListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialNoRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SerialNoRow] = obj["value"]
      pass

class Erp_Tablesets_SerialNoAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.SerialNumber:str = obj["SerialNumber"]
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

class Erp_Tablesets_SerialNoConditionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number.  This is part is the unique index for this table.  It can contain prefixes and sufixxes determined during setup of the part.  """  
      self.FSConditionID:int = obj["FSConditionID"]
      """  System Generated Unique ID  """  
      self.FSConditionDate:str = obj["FSConditionDate"]
      """  Date condition was observed  """  
      self.FSAssetConditionCode:str = obj["FSAssetConditionCode"]
      """  Condition Code entry field  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  Associates the assembly record back its parent JobHead record.  Not directly maintainable.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  The sequence of the operation record within the specific Job/Assembly to which this serial no condition applies.  """  
      self.FSAdditionalDetails:str = obj["FSAdditionalDetails"]
      """  Field for recording additional details about the asset condition which explain why it has taken the value assigned.  For example, if the asset condition is fully serviceable but requires attention at next service the text box might have an entry like 'Hydraulic ram rubber boot split: will require replacement during next service'  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SerialNoListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number.  This is part is the unique index for this table.  It can contain prefixes and sufixxes determined during setup of the part.  """  
      self.SNStatus:str = obj["SNStatus"]
      """   INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED,PACKED = assigned in shipment process but not yet shipped; CONSUMED = issued as raw material to a job parent assembly if full serial tracking or assigned as a child component if outbound tracking.

Add new status codes to Code/Desc and Description:
PACKED`Packed
CONSUMED`Consumed  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  The job number that this item is linked to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the Assembly record within the JobNum/LotNum. This can be user assigned or assigned by the system. The system assigns the next available number during add mode if its left blank.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Seq # of specific material or subcontract operation record.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing Slip.  The Packing slip number that this serial numbered item shiped on.  """  
      self.PackLine:int = obj["PackLine"]
      """  The packing slip line that this serial numbered item shipped on.  """  
      self.Voided:bool = obj["Voided"]
      """  Indicates that this serial number has been voided.  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Indicates that this serial numbered item has been scrapped.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.PackSlipLine:int = obj["PackSlipLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip.  """  
      self.PrevSNStatus:str = obj["PrevSNStatus"]
      """  The status of this serial numbered item prior to its current status.  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number of Serial Number, needed mainly for adding ranges of numbers.  """  
      self.ScrapReasonCode:str = obj["ScrapReasonCode"]
      """  The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred.  """  
      self.SNReference:str = obj["SNReference"]
      """  A generic fill-in field that could be used to allow the user to enter data.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Authorization Number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line # of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA receipt  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  """  
      self.DMRActionNum:int = obj["DMRActionNum"]
      """  DMR action number.  """  
      self.FailSelect:bool = obj["FailSelect"]
      """  Indicates that this item has failed inspection.  """  
      self.LineDetailNum:int = obj["LineDetailNum"]
      """  Identifies the contract record along with Company, contractNum, ContractLine.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  Used to tie back to the related RMADisp record.  """  
      self.NonConfNum:int = obj["NonConfNum"]
      """  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse that transaction is applied to  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that this transaction affected.  """  
      self.WarrExpiration:str = obj["WarrExpiration"]
      """  The latest of the 3 warranty expiration dates  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.ShippedFrom:str = obj["ShippedFrom"]
      """  Indicates where the serial#  was shipped from, (I)nventory or (W)ip.  """  
      self.TranAdd:bool = obj["TranAdd"]
      """  Added at shipment  """  
      self.TFPackNum:int = obj["TFPackNum"]
      """  Transfer Order packing slip.  """  
      self.TFPackLine:int = obj["TFPackLine"]
      """  Transfer Order packing slip Line.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Related (OrderHed) Sales Order number  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Related (OrderDtl) sales order line number  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  related (OrderRel) order release number  """  
      self.FullyMatched:bool = obj["FullyMatched"]
      """  This flag will indicate whether the lower level serial numbers have been fully matched for a parent serial created by a job.  """  
      self.AddedByMatching:bool = obj["AddedByMatching"]
      """  Indicates that this child serial number was manually added in the Serial Matching UI using the New Child Part option as opposed to being generated based on Job or Part BOM.  """  
      self.SubConOprSeq:int = obj["SubConOprSeq"]
      """  When the serial number is shipped by Subcontract Shipment this field holds the JobOper.OprSeq the shipment was made for.  """  
      self.ScrapLaborHedSeq:int = obj["ScrapLaborHedSeq"]
      """  The LaborHedSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  """  
      self.ScrapLaborDtlSeq:int = obj["ScrapLaborDtlSeq"]
      """  The LaborDtlSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  """  
      self.LastLbrOprSeq:int = obj["LastLbrOprSeq"]
      """  The last OperSeq in Labor entry where this serial number was flagged as completed.  """  
      self.LotNum:str = obj["LotNum"]
      """  LotNumber assigned to the serial number in cycle count/Physical Inventory.  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  Drop Shipment Pack Line  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Cross Reference Part Type  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Cross Reference Part Number  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.NextLbrAssySeq:int = obj["NextLbrAssySeq"]
      """  Next Labor Operation Sequence  """  
      self.NextLbrOprSeq:int = obj["NextLbrOprSeq"]
      """  Next Labor Assembly Sequence  """  
      self.Latitude:int = obj["Latitude"]
      """  Latitude of Mobile FS Asset  """  
      self.Longitude:int = obj["Longitude"]
      """  Longitude of Mobile FS Asset  """  
      self.Altitude:int = obj["Altitude"]
      """  Altitude of Mobile FS Asset  """  
      self.FSAssetClassCode:str = obj["FSAssetClassCode"]
      """  Class Code Entry Field  """  
      self.FSServiceLevelAgreement:str = obj["FSServiceLevelAgreement"]
      """  Field Service Level Agreement Text  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  Related (TFOrdHed) Transfer Order number  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  Related (TFOrdLine) Transfer Order Line number  """  
      self.SelectedForCurrentTran:bool = obj["SelectedForCurrentTran"]
      """  Logical indicating the current serial number is selected for the current transaction.  Flag indicating the UI/BL needs to process this serial number.  """  
      self.ScrapReasonCodeDesc:str = obj["ScrapReasonCodeDesc"]
      """  Scrap Reason Code Description  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID  """  
      self.VendorID:str = obj["VendorID"]
      """  Vendor ID  """  
      self.CustIDBTName:str = obj["CustIDBTName"]
      """  CustIDBTName  """  
      self.CustIDCustID:str = obj["CustIDCustID"]
      """  CustIDCustID  """  
      self.CustIDName:str = obj["CustIDName"]
      """  CustIDName  """  
      self.VendorIDAddress1:str = obj["VendorIDAddress1"]
      """  VendorIDAddress1  """  
      self.VendorIDAddress2:str = obj["VendorIDAddress2"]
      """  VendorIDAddress2  """  
      self.VendorIDAddress3:str = obj["VendorIDAddress3"]
      """  VendorIDAddress3  """  
      self.VendorIDCity:str = obj["VendorIDCity"]
      """  VendorIDCity  """  
      self.VendorIDCountry:str = obj["VendorIDCountry"]
      """  VendorIDCountry  """  
      self.VendorIDCurrencyCode:str = obj["VendorIDCurrencyCode"]
      """  VendorIDCurrencyCode  """  
      self.VendorIDDefaultFOB:str = obj["VendorIDDefaultFOB"]
      """  VendorIDDefaultFOB  """  
      self.VendorIDName:str = obj["VendorIDName"]
      """  VendorIDName  """  
      self.VendorIDState:str = obj["VendorIDState"]
      """  VendorIDState  """  
      self.VendorIDTermsCode:str = obj["VendorIDTermsCode"]
      """  VendorIDTermsCode  """  
      self.VendorIDVendorID:str = obj["VendorIDVendorID"]
      """  VendorIDVendorID  """  
      self.VendorIDZIP:str = obj["VendorIDZIP"]
      """  VendorIDZIP  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SerialNoRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number.  This is part is the unique index for this table.  It can contain prefixes and sufixxes determined during setup of the part.  """  
      self.SNStatus:str = obj["SNStatus"]
      """   INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED,PACKED = assigned in shipment process but not yet shipped; CONSUMED = issued as raw material to a job parent assembly if full serial tracking or assigned as a child component if outbound tracking.

Add new status codes to Code/Desc and Description:
PACKED`Packed
CONSUMED`Consumed  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  The job number that this item is linked to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the Assembly record within the JobNum/LotNum. This can be user assigned or assigned by the system. The system assigns the next available number during add mode if its left blank.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Seq # of specific material or subcontract operation record.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing Slip.  The Packing slip number that this serial numbered item shiped on.  """  
      self.PackLine:int = obj["PackLine"]
      """  The packing slip line that this serial numbered item shipped on.  """  
      self.Voided:bool = obj["Voided"]
      """  Indicates that this serial number has been voided.  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Indicates that this serial numbered item has been scrapped.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.PackSlipLine:int = obj["PackSlipLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip.  """  
      self.Selected:bool = obj["Selected"]
      """  if false idicates that this record can be used.  """  
      self.PrevSNStatus:str = obj["PrevSNStatus"]
      """  The status of this serial numbered item prior to its current status.  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  A Standard prefix that will be attached to all Serial Numbers for a particular part.  """  
      self.SNFormat:str = obj["SNFormat"]
      """  Format of the Base number.  """  
      self.SNBaseStructure:str = obj["SNBaseStructure"]
      """  Information about serail number formatting.  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number of Serial Number, needed mainly for adding ranges of numbers.  """  
      self.ScrapReasonCode:str = obj["ScrapReasonCode"]
      """  The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred.  """  
      self.SNReference:str = obj["SNReference"]
      """  A generic fill-in field that could be used to allow the user to enter data.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Authorization Number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line # of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA receipt  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date that this serial numbered was created.  """  
      self.DMRActionNum:int = obj["DMRActionNum"]
      """  DMR action number.  """  
      self.FailSelect:bool = obj["FailSelect"]
      """  Indicates that this item has failed inspection.  """  
      self.LineDetailNum:int = obj["LineDetailNum"]
      """  Identifies the contract record along with Company, contractNum, ContractLine.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  Used to tie back to the related RMADisp record.  """  
      self.NonConfNum:int = obj["NonConfNum"]
      """  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse that transaction is applied to  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that this transaction affected.  """  
      self.WarrExpiration:str = obj["WarrExpiration"]
      """  The latest of the 3 warranty expiration dates  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Created By  """  
      self.ModifiedBy:str = obj["ModifiedBy"]
      """  Modified By  """  
      self.ModifiedDate:str = obj["ModifiedDate"]
      """  Modification Date  """  
      self.ModifiedTime:int = obj["ModifiedTime"]
      """  Modification Time  """  
      self.ShippedFrom:str = obj["ShippedFrom"]
      """  Indicates where the serial#  was shipped from, (I)nventory or (W)ip.  """  
      self.TranAdd:bool = obj["TranAdd"]
      """  Added at shipment  """  
      self.TempTranID:int = obj["TempTranID"]
      """  Used to assign/relate the serial number with a non-document type of transaction, such as inventory issue. Only has a value during the transaction entry process, once the transaction is update this field is set back to zero.  """  
      self.TFPackNum:int = obj["TFPackNum"]
      """  Transfer Order packing slip.  """  
      self.TFPackLine:int = obj["TFPackLine"]
      """  Transfer Order packing slip Line.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Related (OrderHed) Sales Order number  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Related (OrderDtl) sales order line number  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  related (OrderRel) order release number  """  
      self.FullyMatched:bool = obj["FullyMatched"]
      """  This flag will indicate whether the lower level serial numbers have been fully matched for a parent serial created by a job.  """  
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a mask was being used where characters were stripped (using ~ in the mask).  """  
      self.SNMask:str = obj["SNMask"]
      """  The Serial Mask ID that was used when a serial number was created.  """  
      self.AddedByMatching:bool = obj["AddedByMatching"]
      """  Indicates that this child serial number was manually added in the Serial Matching UI using the New Child Part option as opposed to being generated based on Job or Part BOM.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  The suffix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  """  
      self.SubConOprSeq:int = obj["SubConOprSeq"]
      """  When the serial number is shipped by Subcontract Shipment this field holds the JobOper.OprSeq the shipment was made for.  """  
      self.ScrapLaborHedSeq:int = obj["ScrapLaborHedSeq"]
      """  The LaborHedSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  """  
      self.ScrapLaborDtlSeq:int = obj["ScrapLaborDtlSeq"]
      """  The LaborDtlSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  """  
      self.CreatedInPlant:str = obj["CreatedInPlant"]
      """  Indicates which Site?s SNFormat data was used to generate this serial number.  """  
      self.LastLbrOprSeq:int = obj["LastLbrOprSeq"]
      """  The last OperSeq in Labor entry where this serial number was flagged as completed.  """  
      self.LotNum:str = obj["LotNum"]
      """  LotNumber assigned to the serial number in cycle count/Physical Inventory.  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  Drop Shipment Pack Line  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Cross Reference Part Type  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Cross Reference Part Number  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.NextLbrAssySeq:int = obj["NextLbrAssySeq"]
      """  Next Labor Operation Sequence  """  
      self.NextLbrOprSeq:int = obj["NextLbrOprSeq"]
      """  Next Labor Assembly Sequence  """  
      self.Latitude:int = obj["Latitude"]
      """  Latitude of Mobile FS Asset  """  
      self.Longitude:int = obj["Longitude"]
      """  Longitude of Mobile FS Asset  """  
      self.Altitude:int = obj["Altitude"]
      """  Altitude of Mobile FS Asset  """  
      self.FSAssetClassCode:str = obj["FSAssetClassCode"]
      """  Class Code Entry Field  """  
      self.FSServiceLevelAgreement:str = obj["FSServiceLevelAgreement"]
      """  Field Service Level Agreement Text  """  
      self.Accuracy:int = obj["Accuracy"]
      """  Accuracy  """  
      self.MeterReading:int = obj["MeterReading"]
      """  MeterReading  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OTS:bool = obj["OTS"]
      """  One time shipto flag  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  OTS Address 1  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  OTS Address 2  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  OTS Address 3  """  
      self.OTSCity:str = obj["OTSCity"]
      """  OTS City  """  
      self.OTSContact:str = obj["OTSContact"]
      """  OTS Contact  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  OTS Country Number  """  
      self.OTSCustSaved:bool = obj["OTSCustSaved"]
      """  OTS Country Number  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  One Time fax number  """  
      self.OTSName:str = obj["OTSName"]
      """  OTS Name  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  OTS Phone Number  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  OTS Resale ID  """  
      self.OTSSaveAs:str = obj["OTSSaveAs"]
      """  Indicates if/how the OTS is saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  """  
      self.OTSSaveCustID:str = obj["OTSSaveCustID"]
      """  CustID to be used if the OTS is used to create a customer record.  """  
      self.OTSShipToNum:str = obj["OTSShipToNum"]
      """  OTS Ship To Num  """  
      self.OTSState:str = obj["OTSState"]
      """  OTS State  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  OTS Tax Region Code  """  
      self.OTSZip:str = obj["OTSZip"]
      """  OTS Zip  """  
      self.PriorJobNum:str = obj["PriorJobNum"]
      """  PriorJobNum  """  
      self.PriorAssemblySeq:int = obj["PriorAssemblySeq"]
      """  PriorAssemblySeq  """  
      self.PriorMtlSeq:int = obj["PriorMtlSeq"]
      """  PriorMtlSeq  """  
      self.PriorPartNum:str = obj["PriorPartNum"]
      """  PriorPartNum  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.MscPackNum:int = obj["MscPackNum"]
      """  Misc Shipment Pack Num if related to a misc shipment  """  
      self.MscPackLine:int = obj["MscPackLine"]
      """  Misc Shipment Pack Line if related to a Misc Shipment  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Identifier of the asset this Serial Number is associated to. when the SNStatus = INVENTORY this means the SN has been selected for an Asset Addition that has not yet been posted.  """  
      self.AdditionNum:int = obj["AdditionNum"]
      """  Addition Number of the asset the Serial Number is associated to. when the SNStatus = INVENTORY this means the SN has been selected for an Asset Addition that has not yet been posted.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  DisposalNum  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the serial number has to be synchronized with Epicor FSA application.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  Related (TFOrdHed) Transfer Order number  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  Related (TFOrdLine) Transfer Order Line number  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.AllowOTS:bool = obj["AllowOTS"]
      self.CustID:str = obj["CustID"]
      """  Customer ID  """  
      self.CustIDBTName:str = obj["CustIDBTName"]
      """  CustIDBTName  """  
      self.CustIDCustID:str = obj["CustIDCustID"]
      """  CustIDCustID  """  
      self.CustIDName:str = obj["CustIDName"]
      """  CustIDName  """  
      self.OTSSaved:bool = obj["OTSSaved"]
      self.ScrapReasonCodeDesc:str = obj["ScrapReasonCodeDesc"]
      """  Scrap reason code description  """  
      self.ShipToCustID:str = obj["ShipToCustID"]
      """  Shipt To Customer ID  """  
      self.ShipToName:str = obj["ShipToName"]
      self.SNStatusTrans:str = obj["SNStatusTrans"]
      """  INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED  """  
      self.TransactionSource:str = obj["TransactionSource"]
      """  Source of transaction  """  
      self.VendorID:str = obj["VendorID"]
      """  Vendor ID  """  
      self.VendorIDAddress1:str = obj["VendorIDAddress1"]
      """  VendorIDAddress1  """  
      self.VendorIDAddress2:str = obj["VendorIDAddress2"]
      """  VendorIDAddress2  """  
      self.VendorIDAddress3:str = obj["VendorIDAddress3"]
      """  VendorIDAddress3  """  
      self.VendorIDCity:str = obj["VendorIDCity"]
      """  VendorIDCity  """  
      self.VendorIDCountry:str = obj["VendorIDCountry"]
      """  VendorIDCountry  """  
      self.VendorIDCurrencyCode:str = obj["VendorIDCurrencyCode"]
      """  VendorIDCurrencyCode  """  
      self.VendorIDDefaultFOB:str = obj["VendorIDDefaultFOB"]
      """  VendorIDDefaultFOB  """  
      self.VendorIDName:str = obj["VendorIDName"]
      """  VendorIDName  """  
      self.VendorIDState:str = obj["VendorIDState"]
      """  VendorIDState  """  
      self.VendorIDTermsCode:str = obj["VendorIDTermsCode"]
      """  VendorIDTermsCode  """  
      self.VendorIDVendorID:str = obj["VendorIDVendorID"]
      """  VendorIDVendorID  """  
      self.VendorIDZIP:str = obj["VendorIDZIP"]
      """  VendorIDZIP  """  
      self.FullFromShipToAddr:str = obj["FullFromShipToAddr"]
      """  Displays formatted full from ship address. Only for information cannot be modified  """  
      self.FullToShipToAddr:str = obj["FullToShipToAddr"]
      """  Displays formatted full to ship address. Only for information cannot be modified  """  
      self.ToCustID:str = obj["ToCustID"]
      """  External field to define the Customer to which we want to transfer the serial number  """  
      self.ToCustNum:int = obj["ToCustNum"]
      """  External field to define the Customer to which we want to transfer the serial number  """  
      self.ToShipToNum:str = obj["ToShipToNum"]
      """  External field to define the Ship to ID,  to which we want to transfer the serial number  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.CustNumInactive:bool = obj["CustNumInactive"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumAllowShipTo3:bool = obj["CustNumAllowShipTo3"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.FSAssetClassCodeFSAssetClassDesc:str = obj["FSAssetClassCodeFSAssetClassDesc"]
      self.MtlSeqDescription:str = obj["MtlSeqDescription"]
      self.MtlSeqSalvageDescription:str = obj["MtlSeqSalvageDescription"]
      self.NonConfNumDescription:str = obj["NonConfNumDescription"]
      self.OTSCntryISOCode:str = obj["OTSCntryISOCode"]
      self.OTSCntryDescription:str = obj["OTSCntryDescription"]
      self.OTSCntryEUMember:bool = obj["OTSCntryEUMember"]
      self.PackNumShipStatus:str = obj["PackNumShipStatus"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      self.ScrapReasonCodeDescription:str = obj["ScrapReasonCodeDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.ShipToCustName:str = obj["ShipToCustName"]
      self.ShipToCustNumInactive:bool = obj["ShipToCustNumInactive"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.WareHouseCodeDescription:str = obj["WareHouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeAssemblySeqAssetCond_input:
   """ Required : 
   proposedAsmSeq
   ds
   """  
   def __init__(self, obj):
      self.proposedAsmSeq:int = obj["proposedAsmSeq"]
      """  The proposed Job Assembly Seq  """  
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class ChangeAssemblySeqAssetCond_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeAssemblySeq_input:
   """ Required : 
   proposedAsmSeq
   ds
   """  
   def __init__(self, obj):
      self.proposedAsmSeq:int = obj["proposedAsmSeq"]
      """  The proposed Job Assembly Seq  """  
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class ChangeAssemblySeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCustomerID_input:
   """ Required : 
   proposedCustID
   ds
   """  
   def __init__(self, obj):
      self.proposedCustID:str = obj["proposedCustID"]
      """  The proposed Customer ID  """  
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class ChangeCustomerID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDMRAction_input:
   """ Required : 
   proposedDMRAction
   ds
   """  
   def __init__(self, obj):
      self.proposedDMRAction:int = obj["proposedDMRAction"]
      """  The proposed DMR Action  """  
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class ChangeDMRAction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDMRNum_input:
   """ Required : 
   proposedDMRNum
   ds
   """  
   def __init__(self, obj):
      self.proposedDMRNum:int = obj["proposedDMRNum"]
      """  The proposed DMR Number  """  
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class ChangeDMRNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeJobNumAssetCond_input:
   """ Required : 
   proposedJobNum
   ds
   """  
   def __init__(self, obj):
      self.proposedJobNum:str = obj["proposedJobNum"]
      """  The proposed Job Number  """  
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class ChangeJobNumAssetCond_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeJobNum_input:
   """ Required : 
   proposedJobNum
   ds
   """  
   def __init__(self, obj):
      self.proposedJobNum:str = obj["proposedJobNum"]
      """  The proposed Job Number  """  
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class ChangeJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeMtlSeq_input:
   """ Required : 
   proposedMtlSeq
   ds
   """  
   def __init__(self, obj):
      self.proposedMtlSeq:int = obj["proposedMtlSeq"]
      """  The proposed Job Assembly Seq  """  
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class ChangeMtlSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOprSeqAssetCond_input:
   """ Required : 
   proposedOprSeq
   ds
   """  
   def __init__(self, obj):
      self.proposedOprSeq:int = obj["proposedOprSeq"]
      """  The proposed Job Opr Seq  """  
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class ChangeOprSeqAssetCond_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePCID_input:
   """ Required : 
   pcProposedPCID
   ds
   """  
   def __init__(self, obj):
      self.pcProposedPCID:str = obj["pcProposedPCID"]
      """  The proposed PCID  """  
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class ChangePCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePackLine_input:
   """ Required : 
   proposedPackLine
   ds
   """  
   def __init__(self, obj):
      self.proposedPackLine:int = obj["proposedPackLine"]
      """  The proposed Ship To Pack Line  """  
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class ChangePackLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePackNum_input:
   """ Required : 
   proposedPackNum
   ds
   """  
   def __init__(self, obj):
      self.proposedPackNum:int = obj["proposedPackNum"]
      """  The proposed Ship To Packing Number  """  
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class ChangePackNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePackSlipLine_input:
   """ Required : 
   proposedPackSlipLine
   ds
   """  
   def __init__(self, obj):
      self.proposedPackSlipLine:int = obj["proposedPackSlipLine"]
      """  The proposed Receiving Packing Slip Line  """  
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class ChangePackSlipLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePackSlip_input:
   """ Required : 
   proposedPackSlip
   ds
   """  
   def __init__(self, obj):
      self.proposedPackSlip:str = obj["proposedPackSlip"]
      """  The proposed Receiving Packing Slip  """  
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class ChangePackSlip_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePartNum_input:
   """ Required : 
   pcProposedPartNum
   ds
   """  
   def __init__(self, obj):
      self.pcProposedPartNum:str = obj["pcProposedPartNum"]
      """  The proposed Part Number  """  
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class ChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRMALine_input:
   """ Required : 
   proposedRMALine
   ds
   """  
   def __init__(self, obj):
      self.proposedRMALine:int = obj["proposedRMALine"]
      """  The proposed RMA Line  """  
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class ChangeRMALine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRMANum_input:
   """ Required : 
   proposedRMANum
   ds
   """  
   def __init__(self, obj):
      self.proposedRMANum:int = obj["proposedRMANum"]
      """  The proposed RMA Number  """  
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class ChangeRMANum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRMAReceipt_input:
   """ Required : 
   proposedRMAReceipt
   ds
   """  
   def __init__(self, obj):
      self.proposedRMAReceipt:int = obj["proposedRMAReceipt"]
      """  The proposed RMA Receipt  """  
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class ChangeRMAReceipt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeShipToCustID_input:
   """ Required : 
   proposedShipToCustID
   ds
   """  
   def __init__(self, obj):
      self.proposedShipToCustID:str = obj["proposedShipToCustID"]
      """  /// The proposed Ship To CustID  """  
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class ChangeShipToCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeShipToNum_input:
   """ Required : 
   proposedShipToNum
   ds
   """  
   def __init__(self, obj):
      self.proposedShipToNum:str = obj["proposedShipToNum"]
      """  The proposed Ship To Number  """  
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class ChangeShipToNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeToData_input:
   """ Required : 
   CustID
   ShipTo
   OrderNum
   OrderLine
   OrderRelNum
   ds
   """  
   def __init__(self, obj):
      self.CustID:str = obj["CustID"]
      self.ShipTo:str = obj["ShipTo"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderLine:int = obj["OrderLine"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class ChangeToData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeUseOTS_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class ChangeUseOTS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeVendorID_input:
   """ Required : 
   proposedVendorID
   ds
   """  
   def __init__(self, obj):
      self.proposedVendorID:str = obj["proposedVendorID"]
      """  The proposed Vendor ID  """  
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class ChangeVendorID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeVendorPP_input:
   """ Required : 
   proposedPurPoint
   ds
   """  
   def __init__(self, obj):
      self.proposedPurPoint:str = obj["proposedPurPoint"]
      """  The proposed Vendor Purchase Point  """  
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class ChangeVendorPP_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   partNum
   serialNumber
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.serialNumber:str = obj["serialNumber"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_AltSerialNORow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number.  This is part is the unique index for this table.  It can contain prefixes and sufixxes determined during setup of the part.  """  
      self.SNStatus:str = obj["SNStatus"]
      """   INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED,PACKED = assigned in shipment process but not yet shipped; CONSUMED = issued as raw material to a job parent assembly if full serial tracking or assigned as a child component if outbound tracking.

Add new status codes to Code/Desc and Description:
PACKED`Packed
CONSUMED`Consumed  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  The job number that this item is linked to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the Assembly record within the JobNum/LotNum. This can be user assigned or assigned by the system. The system assigns the next available number during add mode if its left blank.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Seq # of specific material or subcontract operation record.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing Slip.  The Packing slip number that this serial numbered item shiped on.  """  
      self.PackLine:int = obj["PackLine"]
      """  The packing slip line that this serial numbered item shipped on.  """  
      self.Voided:bool = obj["Voided"]
      """  Indicates that this serial number has been voided.  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Indicates that this serial numbered item has been scrapped.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.PackSlipLine:int = obj["PackSlipLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip.  """  
      self.Selected:bool = obj["Selected"]
      """  if false idicates that this record can be used.  """  
      self.PrevSNStatus:str = obj["PrevSNStatus"]
      """  The status of this serial numbered item prior to its current status.  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  A Standard prefix that will be attached to all Serial Numbers for a particular part.  """  
      self.SNFormat:str = obj["SNFormat"]
      """  Format of the Base number.  """  
      self.SNBaseStructure:str = obj["SNBaseStructure"]
      """  Information about serail number formatting.  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number of Serial Number, needed mainly for adding ranges of numbers.  """  
      self.ScrapReasonCode:str = obj["ScrapReasonCode"]
      """  The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred.  """  
      self.SNReference:str = obj["SNReference"]
      """  A generic fill-in field that could be used to allow the user to enter data.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Authorization Number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line # of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA receipt  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date that this serial numbered was created.  """  
      self.DMRActionNum:int = obj["DMRActionNum"]
      """  DMR action number.  """  
      self.FailSelect:bool = obj["FailSelect"]
      """  Indicates that this item has failed inspection.  """  
      self.LineDetailNum:int = obj["LineDetailNum"]
      """  Identifies the contract record along with Company, contractNum, ContractLine.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  Used to tie back to the related RMADisp record.  """  
      self.NonConfNum:int = obj["NonConfNum"]
      """  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse that transaction is applied to  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that this transaction affected.  """  
      self.WarrExpiration:str = obj["WarrExpiration"]
      """  The latest of the 3 warranty expiration dates  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Created By  """  
      self.ModifiedBy:str = obj["ModifiedBy"]
      """  Modified By  """  
      self.ModifiedDate:str = obj["ModifiedDate"]
      """  Modification Date  """  
      self.ModifiedTime:int = obj["ModifiedTime"]
      """  Modification Time  """  
      self.ShippedFrom:str = obj["ShippedFrom"]
      """  Indicates where the serial#  was shipped from, (I)nventory or (W)ip.  """  
      self.TranAdd:bool = obj["TranAdd"]
      """  Added at shipment  """  
      self.TempTranID:int = obj["TempTranID"]
      """  Used to assign/relate the serial number with a non-document type of transaction, such as inventory issue. Only has a value during the transaction entry process, once the transaction is update this field is set back to zero.  """  
      self.TFPackNum:int = obj["TFPackNum"]
      """  Transfer Order packing slip.  """  
      self.TFPackLine:int = obj["TFPackLine"]
      """  Transfer Order packing slip Line.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Related (OrderHed) Sales Order number  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Related (OrderDtl) sales order line number  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  related (OrderRel) order release number  """  
      self.FullyMatched:bool = obj["FullyMatched"]
      """  This flag will indicate whether the lower level serial numbers have been fully matched for a parent serial created by a job.  """  
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a mask was being used where characters were stripped (using ~ in the mask).  """  
      self.SNMask:str = obj["SNMask"]
      """  The Serial Mask ID that was used when a serial number was created.  """  
      self.AddedByMatching:bool = obj["AddedByMatching"]
      """  Indicates that this child serial number was manually added in the Serial Matching UI using the New Child Part option as opposed to being generated based on Job or Part BOM.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  The suffix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  """  
      self.SubConOprSeq:int = obj["SubConOprSeq"]
      """  When the serial number is shipped by Subcontract Shipment this field holds the JobOper.OprSeq the shipment was made for.  """  
      self.ScrapLaborHedSeq:int = obj["ScrapLaborHedSeq"]
      """  The LaborHedSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  """  
      self.ScrapLaborDtlSeq:int = obj["ScrapLaborDtlSeq"]
      """  The LaborDtlSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  """  
      self.CreatedInPlant:str = obj["CreatedInPlant"]
      """  Indicates which Site?s SNFormat data was used to generate this serial number.  """  
      self.LastLbrOprSeq:int = obj["LastLbrOprSeq"]
      """  The last OperSeq in Labor entry where this serial number was flagged as completed.  """  
      self.LotNum:str = obj["LotNum"]
      """  LotNumber assigned to the serial number in cycle count/Physical Inventory.  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  Drop Shipment Pack Line  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Cross Reference Part Type  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Cross Reference Part Number  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.NextLbrAssySeq:int = obj["NextLbrAssySeq"]
      """  Next Labor Operation Sequence  """  
      self.NextLbrOprSeq:int = obj["NextLbrOprSeq"]
      """  Next Labor Assembly Sequence  """  
      self.Latitude:int = obj["Latitude"]
      """  Latitude of Mobile FS Asset  """  
      self.Longitude:int = obj["Longitude"]
      """  Longitude of Mobile FS Asset  """  
      self.Altitude:int = obj["Altitude"]
      """  Altitude of Mobile FS Asset  """  
      self.FSAssetClassCode:str = obj["FSAssetClassCode"]
      """  Class Code Entry Field  """  
      self.FSServiceLevelAgreement:str = obj["FSServiceLevelAgreement"]
      """  Field Service Level Agreement Text  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Identifier of the asset this Serial Number is associated to. when the SNStatus = INVENTORY this means the SN has been selected for an Asset Addition that has not yet been posted.  """  
      self.AdditionNum:int = obj["AdditionNum"]
      """  Addition Number of the asset the Serial Number is associated to. when the SNStatus = INVENTORY this means the SN has been selected for an Asset Addition that has not yet been posted.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  DisposalNum  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  Related (TFOrdHed) Transfer Order number  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  Related (TFOrdLine) Transfer Order Line number  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.CustID:str = obj["CustID"]
      self.CustIDName:str = obj["CustIDName"]
      self.Description:str = obj["Description"]
      self.ScrapReasonCodeDesc:str = obj["ScrapReasonCodeDesc"]
      self.ShipToCustID:str = obj["ShipToCustID"]
      self.TransactionSource:str = obj["TransactionSource"]
      self.VendorID:str = obj["VendorID"]
      self.VendorIDCurrencyCode:str = obj["VendorIDCurrencyCode"]
      self.VendorIDName:str = obj["VendorIDName"]
      self.VendorIDTermsCode:str = obj["VendorIDTermsCode"]
      self.VendorIDVendorID:str = obj["VendorIDVendorID"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumName:str = obj["CustNumName"]
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      self.MtlSeqDescription:str = obj["MtlSeqDescription"]
      self.MtlSeqSalvageDescription:str = obj["MtlSeqSalvageDescription"]
      self.NonConfNumDescription:str = obj["NonConfNumDescription"]
      self.PackNumShipStatus:str = obj["PackNumShipStatus"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      self.ScrapReasonCodeDescription:str = obj["ScrapReasonCodeDescription"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.WareHouseCodeDescription:str = obj["WareHouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AltSerialNoTableset:
   def __init__(self, obj):
      self.AltSerialNO:list[Erp_Tablesets_AltSerialNORow] = obj["AltSerialNO"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SerialNoAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.SerialNumber:str = obj["SerialNumber"]
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

class Erp_Tablesets_SerialNoConditionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number.  This is part is the unique index for this table.  It can contain prefixes and sufixxes determined during setup of the part.  """  
      self.FSConditionID:int = obj["FSConditionID"]
      """  System Generated Unique ID  """  
      self.FSConditionDate:str = obj["FSConditionDate"]
      """  Date condition was observed  """  
      self.FSAssetConditionCode:str = obj["FSAssetConditionCode"]
      """  Condition Code entry field  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  Associates the assembly record back its parent JobHead record.  Not directly maintainable.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  The sequence of the operation record within the specific Job/Assembly to which this serial no condition applies.  """  
      self.FSAdditionalDetails:str = obj["FSAdditionalDetails"]
      """  Field for recording additional details about the asset condition which explain why it has taken the value assigned.  For example, if the asset condition is fully serviceable but requires attention at next service the text box might have an entry like 'Hydraulic ram rubber boot split: will require replacement during next service'  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SerialNoListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number.  This is part is the unique index for this table.  It can contain prefixes and sufixxes determined during setup of the part.  """  
      self.SNStatus:str = obj["SNStatus"]
      """   INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED,PACKED = assigned in shipment process but not yet shipped; CONSUMED = issued as raw material to a job parent assembly if full serial tracking or assigned as a child component if outbound tracking.

Add new status codes to Code/Desc and Description:
PACKED`Packed
CONSUMED`Consumed  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  The job number that this item is linked to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the Assembly record within the JobNum/LotNum. This can be user assigned or assigned by the system. The system assigns the next available number during add mode if its left blank.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Seq # of specific material or subcontract operation record.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing Slip.  The Packing slip number that this serial numbered item shiped on.  """  
      self.PackLine:int = obj["PackLine"]
      """  The packing slip line that this serial numbered item shipped on.  """  
      self.Voided:bool = obj["Voided"]
      """  Indicates that this serial number has been voided.  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Indicates that this serial numbered item has been scrapped.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.PackSlipLine:int = obj["PackSlipLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip.  """  
      self.PrevSNStatus:str = obj["PrevSNStatus"]
      """  The status of this serial numbered item prior to its current status.  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number of Serial Number, needed mainly for adding ranges of numbers.  """  
      self.ScrapReasonCode:str = obj["ScrapReasonCode"]
      """  The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred.  """  
      self.SNReference:str = obj["SNReference"]
      """  A generic fill-in field that could be used to allow the user to enter data.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Authorization Number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line # of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA receipt  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  """  
      self.DMRActionNum:int = obj["DMRActionNum"]
      """  DMR action number.  """  
      self.FailSelect:bool = obj["FailSelect"]
      """  Indicates that this item has failed inspection.  """  
      self.LineDetailNum:int = obj["LineDetailNum"]
      """  Identifies the contract record along with Company, contractNum, ContractLine.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  Used to tie back to the related RMADisp record.  """  
      self.NonConfNum:int = obj["NonConfNum"]
      """  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse that transaction is applied to  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that this transaction affected.  """  
      self.WarrExpiration:str = obj["WarrExpiration"]
      """  The latest of the 3 warranty expiration dates  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.ShippedFrom:str = obj["ShippedFrom"]
      """  Indicates where the serial#  was shipped from, (I)nventory or (W)ip.  """  
      self.TranAdd:bool = obj["TranAdd"]
      """  Added at shipment  """  
      self.TFPackNum:int = obj["TFPackNum"]
      """  Transfer Order packing slip.  """  
      self.TFPackLine:int = obj["TFPackLine"]
      """  Transfer Order packing slip Line.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Related (OrderHed) Sales Order number  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Related (OrderDtl) sales order line number  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  related (OrderRel) order release number  """  
      self.FullyMatched:bool = obj["FullyMatched"]
      """  This flag will indicate whether the lower level serial numbers have been fully matched for a parent serial created by a job.  """  
      self.AddedByMatching:bool = obj["AddedByMatching"]
      """  Indicates that this child serial number was manually added in the Serial Matching UI using the New Child Part option as opposed to being generated based on Job or Part BOM.  """  
      self.SubConOprSeq:int = obj["SubConOprSeq"]
      """  When the serial number is shipped by Subcontract Shipment this field holds the JobOper.OprSeq the shipment was made for.  """  
      self.ScrapLaborHedSeq:int = obj["ScrapLaborHedSeq"]
      """  The LaborHedSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  """  
      self.ScrapLaborDtlSeq:int = obj["ScrapLaborDtlSeq"]
      """  The LaborDtlSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  """  
      self.LastLbrOprSeq:int = obj["LastLbrOprSeq"]
      """  The last OperSeq in Labor entry where this serial number was flagged as completed.  """  
      self.LotNum:str = obj["LotNum"]
      """  LotNumber assigned to the serial number in cycle count/Physical Inventory.  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  Drop Shipment Pack Line  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Cross Reference Part Type  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Cross Reference Part Number  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.NextLbrAssySeq:int = obj["NextLbrAssySeq"]
      """  Next Labor Operation Sequence  """  
      self.NextLbrOprSeq:int = obj["NextLbrOprSeq"]
      """  Next Labor Assembly Sequence  """  
      self.Latitude:int = obj["Latitude"]
      """  Latitude of Mobile FS Asset  """  
      self.Longitude:int = obj["Longitude"]
      """  Longitude of Mobile FS Asset  """  
      self.Altitude:int = obj["Altitude"]
      """  Altitude of Mobile FS Asset  """  
      self.FSAssetClassCode:str = obj["FSAssetClassCode"]
      """  Class Code Entry Field  """  
      self.FSServiceLevelAgreement:str = obj["FSServiceLevelAgreement"]
      """  Field Service Level Agreement Text  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  Related (TFOrdHed) Transfer Order number  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  Related (TFOrdLine) Transfer Order Line number  """  
      self.SelectedForCurrentTran:bool = obj["SelectedForCurrentTran"]
      """  Logical indicating the current serial number is selected for the current transaction.  Flag indicating the UI/BL needs to process this serial number.  """  
      self.ScrapReasonCodeDesc:str = obj["ScrapReasonCodeDesc"]
      """  Scrap Reason Code Description  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID  """  
      self.VendorID:str = obj["VendorID"]
      """  Vendor ID  """  
      self.CustIDBTName:str = obj["CustIDBTName"]
      """  CustIDBTName  """  
      self.CustIDCustID:str = obj["CustIDCustID"]
      """  CustIDCustID  """  
      self.CustIDName:str = obj["CustIDName"]
      """  CustIDName  """  
      self.VendorIDAddress1:str = obj["VendorIDAddress1"]
      """  VendorIDAddress1  """  
      self.VendorIDAddress2:str = obj["VendorIDAddress2"]
      """  VendorIDAddress2  """  
      self.VendorIDAddress3:str = obj["VendorIDAddress3"]
      """  VendorIDAddress3  """  
      self.VendorIDCity:str = obj["VendorIDCity"]
      """  VendorIDCity  """  
      self.VendorIDCountry:str = obj["VendorIDCountry"]
      """  VendorIDCountry  """  
      self.VendorIDCurrencyCode:str = obj["VendorIDCurrencyCode"]
      """  VendorIDCurrencyCode  """  
      self.VendorIDDefaultFOB:str = obj["VendorIDDefaultFOB"]
      """  VendorIDDefaultFOB  """  
      self.VendorIDName:str = obj["VendorIDName"]
      """  VendorIDName  """  
      self.VendorIDState:str = obj["VendorIDState"]
      """  VendorIDState  """  
      self.VendorIDTermsCode:str = obj["VendorIDTermsCode"]
      """  VendorIDTermsCode  """  
      self.VendorIDVendorID:str = obj["VendorIDVendorID"]
      """  VendorIDVendorID  """  
      self.VendorIDZIP:str = obj["VendorIDZIP"]
      """  VendorIDZIP  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SerialNoListTableset:
   def __init__(self, obj):
      self.SerialNoList:list[Erp_Tablesets_SerialNoListRow] = obj["SerialNoList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SerialNoRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number.  This is part is the unique index for this table.  It can contain prefixes and sufixxes determined during setup of the part.  """  
      self.SNStatus:str = obj["SNStatus"]
      """   INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED,PACKED = assigned in shipment process but not yet shipped; CONSUMED = issued as raw material to a job parent assembly if full serial tracking or assigned as a child component if outbound tracking.

Add new status codes to Code/Desc and Description:
PACKED`Packed
CONSUMED`Consumed  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  The job number that this item is linked to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the Assembly record within the JobNum/LotNum. This can be user assigned or assigned by the system. The system assigns the next available number during add mode if its left blank.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Seq # of specific material or subcontract operation record.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing Slip.  The Packing slip number that this serial numbered item shiped on.  """  
      self.PackLine:int = obj["PackLine"]
      """  The packing slip line that this serial numbered item shipped on.  """  
      self.Voided:bool = obj["Voided"]
      """  Indicates that this serial number has been voided.  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Indicates that this serial numbered item has been scrapped.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.PackSlipLine:int = obj["PackSlipLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip.  """  
      self.Selected:bool = obj["Selected"]
      """  if false idicates that this record can be used.  """  
      self.PrevSNStatus:str = obj["PrevSNStatus"]
      """  The status of this serial numbered item prior to its current status.  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  A Standard prefix that will be attached to all Serial Numbers for a particular part.  """  
      self.SNFormat:str = obj["SNFormat"]
      """  Format of the Base number.  """  
      self.SNBaseStructure:str = obj["SNBaseStructure"]
      """  Information about serail number formatting.  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number of Serial Number, needed mainly for adding ranges of numbers.  """  
      self.ScrapReasonCode:str = obj["ScrapReasonCode"]
      """  The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred.  """  
      self.SNReference:str = obj["SNReference"]
      """  A generic fill-in field that could be used to allow the user to enter data.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Authorization Number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line # of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA receipt  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date that this serial numbered was created.  """  
      self.DMRActionNum:int = obj["DMRActionNum"]
      """  DMR action number.  """  
      self.FailSelect:bool = obj["FailSelect"]
      """  Indicates that this item has failed inspection.  """  
      self.LineDetailNum:int = obj["LineDetailNum"]
      """  Identifies the contract record along with Company, contractNum, ContractLine.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  Used to tie back to the related RMADisp record.  """  
      self.NonConfNum:int = obj["NonConfNum"]
      """  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse that transaction is applied to  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that this transaction affected.  """  
      self.WarrExpiration:str = obj["WarrExpiration"]
      """  The latest of the 3 warranty expiration dates  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Created By  """  
      self.ModifiedBy:str = obj["ModifiedBy"]
      """  Modified By  """  
      self.ModifiedDate:str = obj["ModifiedDate"]
      """  Modification Date  """  
      self.ModifiedTime:int = obj["ModifiedTime"]
      """  Modification Time  """  
      self.ShippedFrom:str = obj["ShippedFrom"]
      """  Indicates where the serial#  was shipped from, (I)nventory or (W)ip.  """  
      self.TranAdd:bool = obj["TranAdd"]
      """  Added at shipment  """  
      self.TempTranID:int = obj["TempTranID"]
      """  Used to assign/relate the serial number with a non-document type of transaction, such as inventory issue. Only has a value during the transaction entry process, once the transaction is update this field is set back to zero.  """  
      self.TFPackNum:int = obj["TFPackNum"]
      """  Transfer Order packing slip.  """  
      self.TFPackLine:int = obj["TFPackLine"]
      """  Transfer Order packing slip Line.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Related (OrderHed) Sales Order number  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Related (OrderDtl) sales order line number  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  related (OrderRel) order release number  """  
      self.FullyMatched:bool = obj["FullyMatched"]
      """  This flag will indicate whether the lower level serial numbers have been fully matched for a parent serial created by a job.  """  
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a mask was being used where characters were stripped (using ~ in the mask).  """  
      self.SNMask:str = obj["SNMask"]
      """  The Serial Mask ID that was used when a serial number was created.  """  
      self.AddedByMatching:bool = obj["AddedByMatching"]
      """  Indicates that this child serial number was manually added in the Serial Matching UI using the New Child Part option as opposed to being generated based on Job or Part BOM.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  The suffix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  """  
      self.SubConOprSeq:int = obj["SubConOprSeq"]
      """  When the serial number is shipped by Subcontract Shipment this field holds the JobOper.OprSeq the shipment was made for.  """  
      self.ScrapLaborHedSeq:int = obj["ScrapLaborHedSeq"]
      """  The LaborHedSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  """  
      self.ScrapLaborDtlSeq:int = obj["ScrapLaborDtlSeq"]
      """  The LaborDtlSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  """  
      self.CreatedInPlant:str = obj["CreatedInPlant"]
      """  Indicates which Site?s SNFormat data was used to generate this serial number.  """  
      self.LastLbrOprSeq:int = obj["LastLbrOprSeq"]
      """  The last OperSeq in Labor entry where this serial number was flagged as completed.  """  
      self.LotNum:str = obj["LotNum"]
      """  LotNumber assigned to the serial number in cycle count/Physical Inventory.  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  Drop Shipment Pack Line  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Cross Reference Part Type  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Cross Reference Part Number  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.NextLbrAssySeq:int = obj["NextLbrAssySeq"]
      """  Next Labor Operation Sequence  """  
      self.NextLbrOprSeq:int = obj["NextLbrOprSeq"]
      """  Next Labor Assembly Sequence  """  
      self.Latitude:int = obj["Latitude"]
      """  Latitude of Mobile FS Asset  """  
      self.Longitude:int = obj["Longitude"]
      """  Longitude of Mobile FS Asset  """  
      self.Altitude:int = obj["Altitude"]
      """  Altitude of Mobile FS Asset  """  
      self.FSAssetClassCode:str = obj["FSAssetClassCode"]
      """  Class Code Entry Field  """  
      self.FSServiceLevelAgreement:str = obj["FSServiceLevelAgreement"]
      """  Field Service Level Agreement Text  """  
      self.Accuracy:int = obj["Accuracy"]
      """  Accuracy  """  
      self.MeterReading:int = obj["MeterReading"]
      """  MeterReading  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OTS:bool = obj["OTS"]
      """  One time shipto flag  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  OTS Address 1  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  OTS Address 2  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  OTS Address 3  """  
      self.OTSCity:str = obj["OTSCity"]
      """  OTS City  """  
      self.OTSContact:str = obj["OTSContact"]
      """  OTS Contact  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  OTS Country Number  """  
      self.OTSCustSaved:bool = obj["OTSCustSaved"]
      """  OTS Country Number  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  One Time fax number  """  
      self.OTSName:str = obj["OTSName"]
      """  OTS Name  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  OTS Phone Number  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  OTS Resale ID  """  
      self.OTSSaveAs:str = obj["OTSSaveAs"]
      """  Indicates if/how the OTS is saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  """  
      self.OTSSaveCustID:str = obj["OTSSaveCustID"]
      """  CustID to be used if the OTS is used to create a customer record.  """  
      self.OTSShipToNum:str = obj["OTSShipToNum"]
      """  OTS Ship To Num  """  
      self.OTSState:str = obj["OTSState"]
      """  OTS State  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  OTS Tax Region Code  """  
      self.OTSZip:str = obj["OTSZip"]
      """  OTS Zip  """  
      self.PriorJobNum:str = obj["PriorJobNum"]
      """  PriorJobNum  """  
      self.PriorAssemblySeq:int = obj["PriorAssemblySeq"]
      """  PriorAssemblySeq  """  
      self.PriorMtlSeq:int = obj["PriorMtlSeq"]
      """  PriorMtlSeq  """  
      self.PriorPartNum:str = obj["PriorPartNum"]
      """  PriorPartNum  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.MscPackNum:int = obj["MscPackNum"]
      """  Misc Shipment Pack Num if related to a misc shipment  """  
      self.MscPackLine:int = obj["MscPackLine"]
      """  Misc Shipment Pack Line if related to a Misc Shipment  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Identifier of the asset this Serial Number is associated to. when the SNStatus = INVENTORY this means the SN has been selected for an Asset Addition that has not yet been posted.  """  
      self.AdditionNum:int = obj["AdditionNum"]
      """  Addition Number of the asset the Serial Number is associated to. when the SNStatus = INVENTORY this means the SN has been selected for an Asset Addition that has not yet been posted.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  DisposalNum  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the serial number has to be synchronized with Epicor FSA application.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  Related (TFOrdHed) Transfer Order number  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  Related (TFOrdLine) Transfer Order Line number  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.AllowOTS:bool = obj["AllowOTS"]
      self.CustID:str = obj["CustID"]
      """  Customer ID  """  
      self.CustIDBTName:str = obj["CustIDBTName"]
      """  CustIDBTName  """  
      self.CustIDCustID:str = obj["CustIDCustID"]
      """  CustIDCustID  """  
      self.CustIDName:str = obj["CustIDName"]
      """  CustIDName  """  
      self.OTSSaved:bool = obj["OTSSaved"]
      self.ScrapReasonCodeDesc:str = obj["ScrapReasonCodeDesc"]
      """  Scrap reason code description  """  
      self.ShipToCustID:str = obj["ShipToCustID"]
      """  Shipt To Customer ID  """  
      self.ShipToName:str = obj["ShipToName"]
      self.SNStatusTrans:str = obj["SNStatusTrans"]
      """  INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED  """  
      self.TransactionSource:str = obj["TransactionSource"]
      """  Source of transaction  """  
      self.VendorID:str = obj["VendorID"]
      """  Vendor ID  """  
      self.VendorIDAddress1:str = obj["VendorIDAddress1"]
      """  VendorIDAddress1  """  
      self.VendorIDAddress2:str = obj["VendorIDAddress2"]
      """  VendorIDAddress2  """  
      self.VendorIDAddress3:str = obj["VendorIDAddress3"]
      """  VendorIDAddress3  """  
      self.VendorIDCity:str = obj["VendorIDCity"]
      """  VendorIDCity  """  
      self.VendorIDCountry:str = obj["VendorIDCountry"]
      """  VendorIDCountry  """  
      self.VendorIDCurrencyCode:str = obj["VendorIDCurrencyCode"]
      """  VendorIDCurrencyCode  """  
      self.VendorIDDefaultFOB:str = obj["VendorIDDefaultFOB"]
      """  VendorIDDefaultFOB  """  
      self.VendorIDName:str = obj["VendorIDName"]
      """  VendorIDName  """  
      self.VendorIDState:str = obj["VendorIDState"]
      """  VendorIDState  """  
      self.VendorIDTermsCode:str = obj["VendorIDTermsCode"]
      """  VendorIDTermsCode  """  
      self.VendorIDVendorID:str = obj["VendorIDVendorID"]
      """  VendorIDVendorID  """  
      self.VendorIDZIP:str = obj["VendorIDZIP"]
      """  VendorIDZIP  """  
      self.FullFromShipToAddr:str = obj["FullFromShipToAddr"]
      """  Displays formatted full from ship address. Only for information cannot be modified  """  
      self.FullToShipToAddr:str = obj["FullToShipToAddr"]
      """  Displays formatted full to ship address. Only for information cannot be modified  """  
      self.ToCustID:str = obj["ToCustID"]
      """  External field to define the Customer to which we want to transfer the serial number  """  
      self.ToCustNum:int = obj["ToCustNum"]
      """  External field to define the Customer to which we want to transfer the serial number  """  
      self.ToShipToNum:str = obj["ToShipToNum"]
      """  External field to define the Ship to ID,  to which we want to transfer the serial number  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.CustNumInactive:bool = obj["CustNumInactive"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumAllowShipTo3:bool = obj["CustNumAllowShipTo3"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.FSAssetClassCodeFSAssetClassDesc:str = obj["FSAssetClassCodeFSAssetClassDesc"]
      self.MtlSeqDescription:str = obj["MtlSeqDescription"]
      self.MtlSeqSalvageDescription:str = obj["MtlSeqSalvageDescription"]
      self.NonConfNumDescription:str = obj["NonConfNumDescription"]
      self.OTSCntryISOCode:str = obj["OTSCntryISOCode"]
      self.OTSCntryDescription:str = obj["OTSCntryDescription"]
      self.OTSCntryEUMember:bool = obj["OTSCntryEUMember"]
      self.PackNumShipStatus:str = obj["PackNumShipStatus"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      self.ScrapReasonCodeDescription:str = obj["ScrapReasonCodeDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.ShipToCustName:str = obj["ShipToCustName"]
      self.ShipToCustNumInactive:bool = obj["ShipToCustNumInactive"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.WareHouseCodeDescription:str = obj["WareHouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SerialNoTableset:
   def __init__(self, obj):
      self.SerialNo:list[Erp_Tablesets_SerialNoRow] = obj["SerialNo"]
      self.SerialNoAttch:list[Erp_Tablesets_SerialNoAttchRow] = obj["SerialNoAttch"]
      self.SerialNoCondition:list[Erp_Tablesets_SerialNoConditionRow] = obj["SerialNoCondition"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtSerialNoTableset:
   def __init__(self, obj):
      self.SerialNo:list[Erp_Tablesets_SerialNoRow] = obj["SerialNo"]
      self.SerialNoAttch:list[Erp_Tablesets_SerialNoAttchRow] = obj["SerialNoAttch"]
      self.SerialNoCondition:list[Erp_Tablesets_SerialNoConditionRow] = obj["SerialNoCondition"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class FindPart_input:
   """ Required : 
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      pass

class FindPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPartNum:str = obj["parameters"]
      self.opUOM:str = obj["parameters"]
      self.opMatchType:str = obj["parameters"]
      pass

      """  output parameters  """  

class FormatOTSAddress_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class FormatOTSAddress_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   partNum
   serialNumber
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.serialNumber:str = obj["serialNumber"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SerialNoTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SerialNoTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SerialNoTableset] = obj["returnObj"]
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

class GetListCustom_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Where clause for SerialNo table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetListCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SerialNoListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListForOperation_input:
   """ Required : 
   whereClauseSerialNo
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSerialNo:str = obj["whereClauseSerialNo"]
      """  Whereclause for SNList  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetListForOperation_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SerialNoListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListInclReassigned_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   reassignedFromJob
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Where clause for SerialNo table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page Size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute Page  """  
      self.reassignedFromJob:str = obj["reassignedFromJob"]
      """  Includes reassigned serial numbers from this job  """  
      pass

class GetListInclReassigned_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SerialNoListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListServiceCall_input:
   """ Required : 
   whereClauseSerialNo
   pageSize
   absolutePage
   contractNum
   contractLine
   """  
   def __init__(self, obj):
      self.whereClauseSerialNo:str = obj["whereClauseSerialNo"]
      """  Whereclause for SNList  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      self.contractNum:int = obj["contractNum"]
      """  Contract Num.  """  
      self.contractLine:int = obj["contractLine"]
      """  Contract Line.  """  
      pass

class GetListServiceCall_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SerialNoListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
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
      self.returnObj:list[Erp_Tablesets_SerialNoListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewSerialNoAttch_input:
   """ Required : 
   ds
   partNum
   serialNumber
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      self.serialNumber:str = obj["serialNumber"]
      pass

class GetNewSerialNoAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSerialNoCondition_input:
   """ Required : 
   ds
   partNum
   serialNumber
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      self.serialNumber:str = obj["serialNumber"]
      pass

class GetNewSerialNoCondition_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSerialNo_input:
   """ Required : 
   ds
   partNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      pass

class GetNewSerialNo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPartFromRowId_input:
   """ Required : 
   ipRowType
   ipRowID
   """  
   def __init__(self, obj):
      self.ipRowType:str = obj["ipRowType"]
      self.ipRowID:str = obj["ipRowID"]
      pass

class GetPartFromRowId_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPartNum:str = obj["parameters"]
      self.opUOM:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPartXRefInfo_input:
   """ Required : 
   partNum
   SysRowID
   rowType
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Proposed PartNumber change  """  
      self.SysRowID:str = obj["SysRowID"]
      """  RowID of the selected record. Skips find part logic if this has a value.  """  
      self.rowType:str = obj["rowType"]
      """  RowType of the selected record. Only used with sysRowID.  """  
      pass

class GetPartXRefInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partNum:str = obj["parameters"]
      self.serialWarning:str = obj["parameters"]
      self.questionString:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      pass

      """  output parameters  """  

class GetRowsPerPCID_input:
   """ Required : 
   paramPCID
   """  
   def __init__(self, obj):
      self.paramPCID:str = obj["paramPCID"]
      """  Unique identifier of the Plant, if it's an empty string it will search for all Plants  """  
      pass

class GetRowsPerPCID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SerialNoTableset] = obj["returnObj"]
      pass

class GetRowsPerPlantKinetic_input:
   """ Required : 
   partNum
   SNInWIP
   SNRejAdj
   SNShipped
   SNConsumed
   SNAsset
   SNWhsePlant
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.SNInWIP:bool = obj["SNInWIP"]
      self.SNRejAdj:bool = obj["SNRejAdj"]
      self.SNShipped:bool = obj["SNShipped"]
      self.SNConsumed:bool = obj["SNConsumed"]
      self.SNAsset:bool = obj["SNAsset"]
      self.SNWhsePlant:str = obj["SNWhsePlant"]
      pass

class GetRowsPerPlantKinetic_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AltSerialNoTableset] = obj["returnObj"]
      pass

class GetRowsPerPlant_input:
   """ Required : 
   paramWhereClause
   paramPlant
   """  
   def __init__(self, obj):
      self.paramWhereClause:str = obj["paramWhereClause"]
      """  String Representing the WHERE Clause, Company = cur-comp is already assumed  """  
      self.paramPlant:str = obj["paramPlant"]
      """  Unique identifier of the Plant, if it's an empty string it will search for all Plants  """  
      pass

class GetRowsPerPlant_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AltSerialNoTableset] = obj["returnObj"]
      pass

class GetRowsServiceCall_input:
   """ Required : 
   whereClauseSerialNo
   pageSize
   absolutePage
   contractNum
   contractLine
   """  
   def __init__(self, obj):
      self.whereClauseSerialNo:str = obj["whereClauseSerialNo"]
      """  Whereclause for SN  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page  """  
      self.contractNum:int = obj["contractNum"]
      """  Contract Num  """  
      self.contractLine:int = obj["contractLine"]
      """  Contract Line  """  
      pass

class GetRowsServiceCall_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SerialNoTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseSerialNo
   whereClauseSerialNoAttch
   whereClauseSerialNoCondition
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSerialNo:str = obj["whereClauseSerialNo"]
      self.whereClauseSerialNoAttch:str = obj["whereClauseSerialNoAttch"]
      self.whereClauseSerialNoCondition:str = obj["whereClauseSerialNoCondition"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SerialNoTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSerialNumbersNotCompleted_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Where clause for SNList  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetSerialNumbersNotCompleted_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SerialNoListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSerialsForCustShipTracker_input:
   """ Required : 
   ipPackNum
   ipPackLine
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      """  Packnum  """  
      self.ipPackLine:int = obj["ipPackLine"]
      """  PackLine  """  
      pass

class GetSerialsForCustShipTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SerialNoTableset] = obj["returnObj"]
      pass

class GetSerialsForJobTracker_input:
   """ Required : 
   ipCompany
   ipJobNum
   """  
   def __init__(self, obj):
      self.ipCompany:str = obj["ipCompany"]
      """  Company  """  
      self.ipJobNum:str = obj["ipJobNum"]
      """  Job Number  """  
      pass

class GetSerialsForJobTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SerialNoTableset] = obj["returnObj"]
      pass

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

class OnChangingAttributeSet_input:
   """ Required : 
   attributeSetID
   ds
   """  
   def __init__(self, obj):
      self.attributeSetID:int = obj["attributeSetID"]
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class OnChangingAttributeSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingRevisionNum_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class OnChangingRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PlantSerialTracking_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.plantTracking:bool = obj["plantTracking"]
      pass

      """  output parameters  """  

class SerialNumberExists_input:
   """ Required : 
   serialNumber
   """  
   def __init__(self, obj):
      self.serialNumber:str = obj["serialNumber"]
      """  Serial Number  """  
      pass

class SerialNumberExists_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.snExists:bool = obj["snExists"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtSerialNoTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtSerialNoTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateOTSTaxID_input:
   """ Required : 
   ds
   manualValidation
   hmrcFraudPrevHeader
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      self.manualValidation:bool = obj["manualValidation"]
      self.hmrcFraudPrevHeader:str = obj["hmrcFraudPrevHeader"]
      pass

class ValidateOTSTaxID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoTableset] = obj["ds"]
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

