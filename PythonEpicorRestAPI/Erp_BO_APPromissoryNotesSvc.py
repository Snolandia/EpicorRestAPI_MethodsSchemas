import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.APPromissoryNotesSvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_APPromissoryNotes(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APPromissoryNotes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APPromissoryNotes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes",headers=creds) as resp:
           return await resp.json()

async def post_APPromissoryNotes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APPromissoryNotes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APPNHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APPNHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APPromissoryNotes_Company_GroupID_HeadNum(Company, GroupID, HeadNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APPromissoryNote item
   Description: Calls GetByID to retrieve the APPromissoryNote item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPromissoryNote
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APPNHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APPromissoryNotes_Company_GroupID_HeadNum(Company, GroupID, HeadNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APPromissoryNote for the service
   Description: Calls UpdateExt to update APPromissoryNote. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APPromissoryNote
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APPNHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APPromissoryNotes_Company_GroupID_HeadNum(Company, GroupID, HeadNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APPromissoryNote item
   Description: Call UpdateExt to delete APPromissoryNote item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APPromissoryNote
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_APPromissoryNotes_Company_GroupID_HeadNum_APPNDtls(Company, GroupID, HeadNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get APPNDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APPNDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/APPNDtls",headers=creds) as resp:
           return await resp.json()

async def get_APPromissoryNotes_Company_GroupID_HeadNum_APPNDtls_Company_GroupID_HeadNum_InvoiceNum_AdjustmentSeq(Company, GroupID, HeadNum, InvoiceNum, AdjustmentSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APPNDtl item
   Description: Calls GetByID to retrieve the APPNDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPNDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param AdjustmentSeq: Desc: AdjustmentSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APPNDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/APPNDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + AdjustmentSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_APPromissoryNotes_Company_GroupID_HeadNum_BankTrans(Company, GroupID, HeadNum, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BankTrans items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BankTrans1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/BankTrans",headers=creds) as resp:
           return await resp.json()

async def get_APPromissoryNotes_Company_GroupID_HeadNum_BankTrans_Company_BankAcctID_TranNum_Voided(Company, GroupID, HeadNum, BankAcctID, TranNum, Voided, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BankTran item
   Description: Calls GetByID to retrieve the BankTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankTran1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")",headers=creds) as resp:
           return await resp.json()

async def get_APPromissoryNotes_Company_GroupID_HeadNum_APPNHeadTGLCs(Company, GroupID, HeadNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get APPNHeadTGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APPNHeadTGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNHeadTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/APPNHeadTGLCs",headers=creds) as resp:
           return await resp.json()

async def get_APPromissoryNotes_Company_GroupID_HeadNum_APPNHeadTGLCs_Company_GroupID_HeadNum_TGLCTranNum(Company, GroupID, HeadNum, TGLCTranNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APPNHeadTGLC item
   Description: Calls GetByID to retrieve the APPNHeadTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPNHeadTGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param TGLCTranNum: Desc: TGLCTranNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APPNHeadTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/APPNHeadTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + TGLCTranNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_APPromissoryNotes_Company_GroupID_HeadNum_EntityGLCs(Company, GroupID, HeadNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EntityGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def get_APPromissoryNotes_Company_GroupID_HeadNum_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, GroupID, HeadNum, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_APPromissoryNotes_Company_GroupID_HeadNum_APPNHeadAttches(Company, GroupID, HeadNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get APPNHeadAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APPNHeadAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/APPNHeadAttches",headers=creds) as resp:
           return await resp.json()

async def get_APPromissoryNotes_Company_GroupID_HeadNum_APPNHeadAttches_Company_GroupID_HeadNum_DrawingSeq(Company, GroupID, HeadNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APPNHeadAttch item
   Description: Calls GetByID to retrieve the APPNHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPNHeadAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APPNHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPromissoryNotes(" + Company + "," + GroupID + "," + HeadNum + ")/APPNHeadAttches(" + Company + "," + GroupID + "," + HeadNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_APPNDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APPNDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APPNDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNDtls",headers=creds) as resp:
           return await resp.json()

async def post_APPNDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APPNDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APPNDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APPNDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APPNDtls_Company_GroupID_HeadNum_InvoiceNum_AdjustmentSeq(Company, GroupID, HeadNum, InvoiceNum, AdjustmentSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APPNDtl item
   Description: Calls GetByID to retrieve the APPNDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPNDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param AdjustmentSeq: Desc: AdjustmentSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APPNDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + AdjustmentSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APPNDtls_Company_GroupID_HeadNum_InvoiceNum_AdjustmentSeq(Company, GroupID, HeadNum, InvoiceNum, AdjustmentSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APPNDtl for the service
   Description: Calls UpdateExt to update APPNDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APPNDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param AdjustmentSeq: Desc: AdjustmentSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APPNDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + AdjustmentSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APPNDtls_Company_GroupID_HeadNum_InvoiceNum_AdjustmentSeq(Company, GroupID, HeadNum, InvoiceNum, AdjustmentSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APPNDtl item
   Description: Call UpdateExt to delete APPNDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APPNDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param AdjustmentSeq: Desc: AdjustmentSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + AdjustmentSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_BankTrans(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BankTrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankTrans
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/BankTrans",headers=creds) as resp:
           return await resp.json()

async def post_BankTrans(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BankTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BankTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BankTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/BankTrans", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BankTrans_Company_BankAcctID_TranNum_Voided(Company, BankAcctID, TranNum, Voided, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BankTran item
   Description: Calls GetByID to retrieve the BankTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BankTrans_Company_BankAcctID_TranNum_Voided(Company, BankAcctID, TranNum, Voided, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BankTran for the service
   Description: Calls UpdateExt to update BankTran. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BankTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BankTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BankTrans_Company_BankAcctID_TranNum_Voided(Company, BankAcctID, TranNum, Voided, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BankTran item
   Description: Call UpdateExt to delete BankTran item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")",headers=creds) as resp:
           return await resp.json()

async def get_BankTrans_Company_BankAcctID_TranNum_Voided_BankTranGLCs(Company, BankAcctID, TranNum, Voided, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BankTranGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BankTranGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranGLCs",headers=creds) as resp:
           return await resp.json()

async def get_BankTrans_Company_BankAcctID_TranNum_Voided_BankTranGLCs_Company_BankAcctID_TranNum_Voided_SysRowID(Company, BankAcctID, TranNum, Voided, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BankTranGLC item
   Description: Calls GetByID to retrieve the BankTranGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankTranGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankTranGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BankTranGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BankTranGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankTranGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/BankTranGLCs",headers=creds) as resp:
           return await resp.json()

async def post_BankTranGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BankTranGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BankTranGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BankTranGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/BankTranGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BankTranGLCs_Company_BankAcctID_TranNum_Voided_SysRowID(Company, BankAcctID, TranNum, Voided, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BankTranGLC item
   Description: Calls GetByID to retrieve the BankTranGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankTranGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankTranGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/BankTranGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BankTranGLCs_Company_BankAcctID_TranNum_Voided_SysRowID(Company, BankAcctID, TranNum, Voided, SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BankTranGLC for the service
   Description: Calls UpdateExt to update BankTranGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BankTranGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BankTranGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/BankTranGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BankTranGLCs_Company_BankAcctID_TranNum_Voided_SysRowID(Company, BankAcctID, TranNum, Voided, SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BankTranGLC item
   Description: Call UpdateExt to delete BankTranGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankTranGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/BankTranGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_APPNHeadTGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APPNHeadTGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APPNHeadTGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNHeadTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNHeadTGLCs",headers=creds) as resp:
           return await resp.json()

async def post_APPNHeadTGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APPNHeadTGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APPNHeadTGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APPNHeadTGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNHeadTGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APPNHeadTGLCs_Company_GroupID_HeadNum_TGLCTranNum(Company, GroupID, HeadNum, TGLCTranNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APPNHeadTGLC item
   Description: Calls GetByID to retrieve the APPNHeadTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPNHeadTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param TGLCTranNum: Desc: TGLCTranNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APPNHeadTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNHeadTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + TGLCTranNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APPNHeadTGLCs_Company_GroupID_HeadNum_TGLCTranNum(Company, GroupID, HeadNum, TGLCTranNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APPNHeadTGLC for the service
   Description: Calls UpdateExt to update APPNHeadTGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APPNHeadTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param TGLCTranNum: Desc: TGLCTranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APPNHeadTGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNHeadTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + TGLCTranNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APPNHeadTGLCs_Company_GroupID_HeadNum_TGLCTranNum(Company, GroupID, HeadNum, TGLCTranNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APPNHeadTGLC item
   Description: Call UpdateExt to delete APPNHeadTGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APPNHeadTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param TGLCTranNum: Desc: TGLCTranNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNHeadTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + TGLCTranNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_EntityGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EntityGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EntityGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def post_EntityGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EntityGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/EntityGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EntityGLC for the service
   Description: Calls UpdateExt to update EntityGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EntityGLC item
   Description: Call UpdateExt to delete EntityGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_APPNHeadAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APPNHeadAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APPNHeadAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNHeadAttches",headers=creds) as resp:
           return await resp.json()

async def post_APPNHeadAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APPNHeadAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APPNHeadAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APPNHeadAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNHeadAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APPNHeadAttches_Company_GroupID_HeadNum_DrawingSeq(Company, GroupID, HeadNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APPNHeadAttch item
   Description: Calls GetByID to retrieve the APPNHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPNHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APPNHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNHeadAttches(" + Company + "," + GroupID + "," + HeadNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APPNHeadAttches_Company_GroupID_HeadNum_DrawingSeq(Company, GroupID, HeadNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APPNHeadAttch for the service
   Description: Calls UpdateExt to update APPNHeadAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APPNHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APPNHeadAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNHeadAttches(" + Company + "," + GroupID + "," + HeadNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APPNHeadAttches_Company_GroupID_HeadNum_DrawingSeq(Company, GroupID, HeadNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APPNHeadAttch item
   Description: Call UpdateExt to delete APPNHeadAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APPNHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/APPNHeadAttches(" + Company + "," + GroupID + "," + HeadNum + "," + DrawingSeq + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/LegalNumGenOpts",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/LegalNumGenOpts", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PITotals(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PITotals items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PITotals
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PITotalsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/PITotals",headers=creds) as resp:
           return await resp.json()

async def post_PITotals(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PITotals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PITotalsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PITotalsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/PITotals", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PITotals_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PITotal item
   Description: Calls GetByID to retrieve the PITotal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PITotal
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PITotalsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/PITotals(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PITotals_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PITotal for the service
   Description: Calls UpdateExt to update PITotal. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PITotal
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PITotalsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/PITotals(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PITotals_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PITotal item
   Description: Call UpdateExt to delete PITotal item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PITotal
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/PITotals(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseAPPNHead, whereClauseAPPNHeadAttch, whereClauseAPPNDtl, whereClauseBankTran, whereClauseBankTranGLC, whereClauseAPPNHeadTGLC, whereClauseEntityGLC, whereClauseLegalNumGenOpts, whereClausePITotals, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseAPPNHead=" + whereClauseAPPNHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAPPNHeadAttch=" + whereClauseAPPNHeadAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAPPNDtl=" + whereClauseAPPNDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBankTran=" + whereClauseBankTran
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBankTranGLC=" + whereClauseBankTranGLC
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAPPNHeadTGLC=" + whereClauseAPPNHeadTGLC
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEntityGLC=" + whereClauseEntityGLC
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
   params += "whereClausePITotals=" + whereClausePITotals
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(groupID, headNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "groupID=" + groupID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "headNum=" + headNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ApplyInvoiceToGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ApplyInvoiceToGroup
   Description: Create Vendor Checks for selected invoice.
   OperationID: ApplyInvoiceToGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ApplyInvoiceToGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApplyInvoiceToGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssignLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignLegalNumber
   Description: Assigns a legal number to the miscellaneous shipment.
   OperationID: AssignLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetEndorsedARPILegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetEndorsedARPILegalNumGenOpts
   Description: Returns the legal number generation options for AR Promissory Note movement.
   OperationID: GetEndorsedARPILegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEndorsedARPILegalNumGenOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEndorsedARPILegalNumGenOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssignEndorsedARPILegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignEndorsedARPILegalNumber
   Description: Assigns a legal number to AR Promissory Note movement.
   OperationID: AssignEndorsedARPILegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignEndorsedARPILegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignEndorsedARPILegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePIType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePIType
   Description: Call method when the user changes APPNHead.TransDate.
   OperationID: ChangePIType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePIType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePIType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTranAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTranAmt
   Description: This method updates the BankTran amounts when the adjustment amount changes or
the currency switch toggles.
   OperationID: ChangeTranAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTranAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTranAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckDocumentIsLocked(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDocumentIsLocked
   Description: Method to call when it is necessary to check if document is lock, before doing smth.
   OperationID: CheckDocumentIsLocked
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDocumentIsLocked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDocumentIsLocked_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateAPPNHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateAPPNHead
   Description: Create Vendor Checks for selected invoices.
   OperationID: CreateAPPNHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateAPPNHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateAPPNHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidAPPNMoveLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidAPPNMoveLegalNumber
   Description: Voids legal number generated on a status change
   OperationID: VoidAPPNMoveLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidAPPNMoveLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidAPPNMoveLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteAPPNMove(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteAPPNMove
   Description: Deletes a status change movement
   OperationID: DeleteAPPNMove
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteAPPNMove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteAPPNMove_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateStatusAndType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateStatusAndType
   Description: Validates that status was changed
   OperationID: ValidateStatusAndType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateStatusAndType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateStatusAndType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateUnpostedMovement(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateUnpostedMovement
   Description: Validates if PI has an unposted movement and throws an error or returns a question to the user along with the unposted movement information.
   OperationID: ValidateUnpostedMovement
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateUnpostedMovement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateUnpostedMovement_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CancelStatusChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CancelStatusChange
   Description: Validates Lock Status, Voids Legal Number and Deletes APPNMove when cancelling Status Change.
   OperationID: CancelStatusChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CancelStatusChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CancelStatusChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateNewAPPNHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateNewAPPNHead
   Description: Create New CheckHed record.  To be used instead of GetNewCheckHed record.
   OperationID: CreateNewAPPNHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateNewAPPNHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateNewAPPNHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateNewAPPNHeadEndorsement(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateNewAPPNHeadEndorsement
   Description: Create New APPNHead record based on endorsed AR Promissory Note.
   OperationID: CreateNewAPPNHeadEndorsement
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateNewAPPNHeadEndorsement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateNewAPPNHeadEndorsement_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteNegPayment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteNegPayment
   Description: DeleteNegPayments.  Deletes all checks in the group that have negative check.
amounts. Works the same as MassDelete but only deletes negative balance checks.
   OperationID: DeleteNegPayment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteNegPayment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteNegPayment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateAPPNDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateAPPNDtl
   Description: This method combines the GetNewAPPNDtl and Update() method into one routine
so that the user can run an "Auto Apply" Payment function
   OperationID: GenerateAPPNDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateAPPNDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateAPPNDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAPPNMove(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAPPNMove
   Description: Get the APPNMove records for an APPromissoryNotes.
   OperationID: GetAPPNMove
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAPPNMove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAPPNMove_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBankAcctInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBankAcctInfo
   Description: This method is called when the BankAcctID field is modified
   OperationID: GetBankAcctInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBankAcctInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBankAcctInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBankFeeDefaultAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBankFeeDefaultAccount
   Description: This method is used to get the default account(s) for a Bank Fee
   OperationID: GetBankFeeDefaultAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBankFeeDefaultAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBankFeeDefaultAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetData4ARPITracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetData4ARPITracker
   Description: Get AP payment instrument data for AR Payment Instrument Tracker
   OperationID: GetData4ARPITracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetData4ARPITracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetData4ARPITracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGLJrnDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGLJrnDtl
   Description: Get the GLJrnDtl records for an APPromissoryNote.
   OperationID: GetGLJrnDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGLJrnDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGLJrnDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGroupIDForPI(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGroupIDForPI
   Description: This method will retrieve the GroupID for an APPNHead record that's for the
APPromNoteID supplied.
   OperationID: GetGroupIDForPI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGroupIDForPI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGroupIDForPI_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGroupIDForPNI(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGroupIDForPNI
   OperationID: GetGroupIDForPNI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGroupIDForPNI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGroupIDForPNI_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultMoveTranDocType(epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultMoveTranDocType
   Description: Restores Default Document Type when user leaves it blank
   OperationID: GetDefaultMoveTranDocType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultMoveTranDocType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_NeedsLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method NeedsLegalNumber
   Description: Validates if a Legal Number can be created for the selected document type
   OperationID: NeedsLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/NeedsLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/NeedsLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPPNHeadByGroupID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPPNHeadByGroupID
   OperationID: GetNewAPPNHeadByGroupID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPPNHeadByGroupID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPPNHeadByGroupID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPPNMoveByAPPNHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPPNMoveByAPPNHead
   OperationID: GetNewAPPNMoveByAPPNHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPPNMoveByAPPNHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPPNMoveByAPPNHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBankTranByHeadNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBankTranByHeadNum
   OperationID: GetNewBankTranByHeadNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBankTranByHeadNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankTranByHeadNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPostCodeByPIStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPostCodeByPIStatus
   Description: GetPostCodeByPIStatus
   OperationID: GetPostCodeByPIStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPostCodeByPIStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPostCodeByPIStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRestartAPPNPrinting(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRestartAPPNPrinting
   Description: Gets restart AP Promissory Note printing
   OperationID: GetRestartAPPNPrinting
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRestartAPPNPrinting_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRestartAPPNPrinting_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsTracker
   Description: Wrapper on GetRows for Trackers so Adjustment records are not deleted
   OperationID: GetRowsTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MassDelete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MassDelete
   Description: Mass Delete.  Delete all checks in the Group.
   OperationID: MassDelete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MassDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBankFeeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBankFeeID
   OperationID: OnChangeBankFeeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBankFeeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankFeeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDocTranAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDocTranAmt
   Description: Call method when the user changes the Doc Tran Amount.
   OperationID: OnChangeDocTranAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDocTranAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDocTranAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeInvoiceNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeInvoiceNum
   Description: Call this method when the user enters the Invoice Number in Pay Invoice screen.
   OperationID: OnChangeInvoiceNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeInvoiceNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInvoiceNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeInvSelPayment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeInvSelPayment
   Description: Call this method when the user changes either Gross Payment or Disc. Taken field.
Use this method with Payment maintenance screen for ApInvSelDataSet.
   OperationID: OnChangeInvSelPayment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeInvSelPayment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInvSelPayment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTransDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTransDate
   Description: Call method when the user changes APPNHead.TransDate.
   OperationID: OnChangeTransDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTransDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTransDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeVendBankAcctID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeVendBankAcctID
   Description: Call this method when the user enters the ttAPNHead.VendBankAcctID
   OperationID: OnChangeVendBankAcctID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeVendBankAcctID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVendBankAcctID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeVendor
   Description: Call this method when the user enters the ttAPNHead.VendorNum
   OperationID: OnChangeVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeType
   Description: OnChangeType
   OperationID: OnChangeType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrePost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrePost
   Description: Check APPNHead before posting
   OperationID: PrePost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrePost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SelectInvoices(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SelectInvoices
   Description: Read ApInvHed records and create ApinvSel records if they meet the selection criteria.
   OperationID: SelectInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SelectInvoiceToApplyToGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SelectInvoiceToApplyToGroup
   Description: Read ApInvHed records and create ApinvSel records if they meet the selection criteria.
   OperationID: SelectInvoiceToApplyToGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectInvoiceToApplyToGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectInvoiceToApplyToGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateAPPNMove4WriteOff(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateAPPNMove4WriteOff
   OperationID: UpdateAPPNMove4WriteOff
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateAPPNMove4WriteOff_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateAPPNMove4WriteOff_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateDueDateDescription(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateDueDateDescription
   Description: Purpose: Update DueDate and Description for APPNHead only.
Parameters:
inGroupID
inHeadNum
inDueDateNew new value of DueDate
inDescriptionNew new value of Description
define_output_parameter_dataset_for_APPromissoryNotesDataSet
Notes:
   OperationID: UpdateDueDateDescription
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateDueDateDescription_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateDueDateDescription_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidLegalNumber
   Description: Voids the legal number.
   OperationID: VoidLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_selectFilterPIPayMethod(epicorHeaders = None):
   """  
   Summary: Invoke method selectFilterPIPayMethod
   Description: Return the id’s for payment methods from AP
   OperationID: selectFilterPIPayMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/selectFilterPIPayMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ValidateRequiredFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateRequiredFields
   Description: ValidateRequiredFields
   OperationID: ValidateRequiredFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateRequiredFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRequiredFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateWithholdingExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateWithholdingExists
   Description: Method to validate if there is a withholding tax in either invoice or details.
   OperationID: ValidateWithholdingExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateWithholdingExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateWithholdingExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreUpdate
   Description: This method will return a record in the LegalNumGenOpts data table if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePaymentInstruments(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePaymentInstruments
   Description: Validate the PI Type Generation Options and Supplier Bank Required Flag
   OperationID: ValidatePaymentInstruments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePaymentInstruments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePaymentInstruments_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePIBeforePrint(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePIBeforePrint
   Description: Validate Payment Instruments are applied before printing, returns a warning if they are not.
   OperationID: ValidatePIBeforePrint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePIBeforePrint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePIBeforePrint_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPPNHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPPNHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPPNHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPPNHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPPNHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPPNHeadAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPPNHeadAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPPNHeadAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPPNHeadAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPPNHeadAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPPNDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPPNDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPPNDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPPNDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPPNDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBankTran(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBankTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBankTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBankTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBankTranGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBankTranGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBankTranGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBankTranGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankTranGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPPNHeadTGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPPNHeadTGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPPNHeadTGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPPNHeadTGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPPNHeadTGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEntityGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEntityGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEntityGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEntityGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEntityGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromissoryNotesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APPNDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APPNHeadAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APPNHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APPNHeadRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadTGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APPNHeadTGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BankTranGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BankTranRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EntityGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PITotalsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PITotalsRow] = obj["value"]
      pass

class Erp_Tablesets_APPNDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.APPNDtlLine:int = obj["APPNDtlLine"]
      """  Line  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID of the promissoiry note.  """  
      self.DiscAmt:int = obj["DiscAmt"]
      """  Discount Amount in base currency.  """  
      self.DocDiscAmt:int = obj["DocDiscAmt"]
      """  Discount Amount in invoice currency.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax amount in invoice currency.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Transaction amount in invoice currency.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Entry Person  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates that the promissory note is posted to the GL.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  AP Invoice Number linked to the promissory note.  """  
      self.RoundDiff:int = obj["RoundDiff"]
      """  Rounding Differences  """  
      self.Rpt1DiscAmt:int = obj["Rpt1DiscAmt"]
      """  Discount Amount in report currency 1.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Tax amount  in report currency 1.  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Transaction amount  in report currency 1.  """  
      self.Rpt2DiscAmt:int = obj["Rpt2DiscAmt"]
      """  Discount Amount in report currency 2.  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Tax amount  in report currency 2.  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Transaction amount  in report currency 2.  """  
      self.Rpt3DiscAmt:int = obj["Rpt3DiscAmt"]
      """  Discount Amount in report currency 3.  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Tax amount  in report currency 3.  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Transaction amount  in report currency 3.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Tax amount in base currency.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Tax Liability  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Transaction Amount in base currency.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction date.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier  """  
      self.HeadNum:int = obj["HeadNum"]
      """  If TranType = "Pay" or "ADJ" for a currency gain/loss  then this is a duplicate of the related CheckHed.HeadNum,  otherwise it is set to zero.  """  
      self.Voided:bool = obj["Voided"]
      """  Indicates if the promissory node is voided.  """  
      self.GroupID:str = obj["GroupID"]
      """  Group ID  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G\L fiscal period that this transaction is posted to. Updated by the check printing process for system printed checks or by the user for manually printed checks.  If entered must be valid in the Fiscal master.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal Year that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYear during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year to each record on the TranDate  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """   Fiscal Year Suffix that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYearSuffix during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year suffix to each record on the TranDate  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  """  
      self.Posted:bool = obj["Posted"]
      """  An internal flag which indicates if this check has been Posted.  If "NO" then it is considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process. This is only applicable for TranType = "Pay".  """  
      self.Description:str = obj["Description"]
      """  In the case of payment details this description is printed on the check stub. If referencing a invoice the APInvHed.Description is used as a default.  """  
      self.TranType:str = obj["TranType"]
      """  An internal flag which identifies the type of transaction. Valid types are "Pay" or "Adj".  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.FirstHeadNum:int = obj["FirstHeadNum"]
      """  Link To first checkhed record  """  
      self.GainLossType:str = obj["GainLossType"]
      """  "R" for realized or "U" for unrealized Gain/Loss  """  
      self.ReverseGL:bool = obj["ReverseGL"]
      """  Indicates if it's a reversing Gain/Loss adjustment  """  
      self.RevalueDate:str = obj["RevalueDate"]
      """  Revaluation date that generated the gain/loss record  """  
      self.RevalueBal:int = obj["RevalueBal"]
      """  PI Balance at the time of revaluation  """  
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      """  Document currency PI Balance at the time of revaluation  """  
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      """  Reporting currency PI Balance at the time of revaluation  """  
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      """  Reporting currency PI Balance at the time of revaluation  """  
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      """  Reporting currency PI Balance at the time of revaluation  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AdjustmentSeq:int = obj["AdjustmentSeq"]
      """  AdjustmentSeq  """  
      self.AmtToAP:int = obj["AmtToAP"]
      self.ApplyDate:str = obj["ApplyDate"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.BaseCurrSymbolCurrDesc:str = obj["BaseCurrSymbolCurrDesc"]
      self.BaseCurrSymbolCurrName:str = obj["BaseCurrSymbolCurrName"]
      self.BaseCurrSymbolCurrSymbol:str = obj["BaseCurrSymbolCurrSymbol"]
      self.BaseCurrSymbolDocumentDesc:str = obj["BaseCurrSymbolDocumentDesc"]
      self.BaseSelfAssessedTax:int = obj["BaseSelfAssessedTax"]
      self.CPayLinked:bool = obj["CPayLinked"]
      """  Indicates if the related invoice is linked to a Central Payment invoice  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencyGainLoss:int = obj["CurrencyGainLoss"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency.CurrSymbol from APInvHed  """  
      self.CurrSymbolCurrDesc:str = obj["CurrSymbolCurrDesc"]
      self.CurrSymbolCurrName:str = obj["CurrSymbolCurrName"]
      self.CurrSymbolCurrSymbol:str = obj["CurrSymbolCurrSymbol"]
      self.CurrSymbolDocumentDesc:str = obj["CurrSymbolDocumentDesc"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  The display gl account.  """  
      self.DispTranAmt:int = obj["DispTranAmt"]
      self.DocBaseSelfAssessedTax:int = obj["DocBaseSelfAssessedTax"]
      self.DocDispTranAmt:int = obj["DocDispTranAmt"]
      self.DocExpenseAmount:int = obj["DocExpenseAmount"]
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      self.DocNetAmount:int = obj["DocNetAmount"]
      self.DocNewBalance:int = obj["DocNewBalance"]
      self.DocUnPostedBal:int = obj["DocUnPostedBal"]
      self.DueDate:str = obj["DueDate"]
      self.ExchangeRate:int = obj["ExchangeRate"]
      self.ExpenseAmount:int = obj["ExpenseAmount"]
      self.FullyPaid:bool = obj["FullyPaid"]
      """  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  This is the source Company of the Central Payment linked invoice  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      self.InvoiceBal:int = obj["InvoiceBal"]
      self.InvoiceDate:str = obj["InvoiceDate"]
      self.LockRate:bool = obj["LockRate"]
      self.NetAmount:int = obj["NetAmount"]
      self.NewBalance:int = obj["NewBalance"]
      self.PostToGL:bool = obj["PostToGL"]
      """  Indicates if posting GL transactions.  """  
      self.TermsCode:str = obj["TermsCode"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.UnPostedBal:int = obj["UnPostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign.  """  
      self.WithHoldTax:int = obj["WithHoldTax"]
      self.DiscountDate:str = obj["DiscountDate"]
      self.ChangeExchangeRateResponse:str = obj["ChangeExchangeRateResponse"]
      """  Yes and No considered valid response.  All other values including blank treated as question was not posed to the user.  """  
      self.DocSelfAssessedTax:int = obj["DocSelfAssessedTax"]
      self.DocWithHoldTax:int = obj["DocWithHoldTax"]
      self.SelfAssessedTax:int = obj["SelfAssessedTax"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.APPromNoteID:str = obj["APPromNoteID"]
      self.PIStatus:str = obj["PIStatus"]
      self.PIStatusStatusDesc:str = obj["PIStatusStatusDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APPNHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
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

class Erp_Tablesets_APPNHeadListRow:
   def __init__(self, obj):
      self.AppliedAmount:int = obj["AppliedAmount"]
      """  Applied Amount. Base Currency.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account of the promissory note.  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Amount  """  
      self.BankSlip:str = obj["BankSlip"]
      """  Bank Slip Number of the promissory note.  """  
      self.BankTotalAmt:int = obj["BankTotalAmt"]
      """  Bank Total Amount.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  Cash book Number.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CompBankAcctID:str = obj["CompBankAcctID"]
      """  Bank Account ID of the company.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code of the promissory note.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount amount in base currency.  """  
      self.DocPNAmt:int = obj["DocPNAmt"]
      """  Promissory Note amount in document currency.  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the promissory note.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Entry Person.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate of the promissory note.  """  
      self.Paid:bool = obj["Paid"]
      """  Indicates if the promissory node is fully paid.  """  
      self.PNAmt:int = obj["PNAmt"]
      """  Promissory note amount in base currency.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates that the promissory note is posted.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group Code.  """  
      self.Rpt1PNAmt:int = obj["Rpt1PNAmt"]
      """  Promissory Note Amount in Report Currency 1.  """  
      self.Rpt1Discountamt:int = obj["Rpt1Discountamt"]
      """  Promissory Note Discount Amount in Report Currency 1.  """  
      self.Rpt1BankTotalAmt:int = obj["Rpt1BankTotalAmt"]
      """  Promissory Note Bank Total Amount in Report Currency 1.  """  
      self.Rpt2PNAmt:int = obj["Rpt2PNAmt"]
      """  Promissory Note Amount in Report Currency 2.  """  
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      """  Promissory Note Discount Amount in Report Currency 2.  """  
      self.Rpt2BankTotalAmt:int = obj["Rpt2BankTotalAmt"]
      """  Promissory Note Bank Total Amount in Report Currency 2.  """  
      self.Rpt3PNAmt:int = obj["Rpt3PNAmt"]
      """  Promissory Note Amount in Report Currency 3.  """  
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      """  Promissory Note Discount Amount in Report Currency 3.  """  
      self.Rpt3BankTotalAmt:int = obj["Rpt3BankTotalAmt"]
      """  Promissory Note Bank Total Amount in Report Currency 3.  """  
      self.Signed:bool = obj["Signed"]
      """  Indicates that the promissory note is signed.  """  
      self.TotalAPAmt:int = obj["TotalAPAmt"]
      """  Total AP Amount  """  
      self.TransDate:str = obj["TransDate"]
      """  Transaction date.  """  
      self.VendBankAcctID:str = obj["VendBankAcctID"]
      """  Supplier Bank Account ID  """  
      self.VendorID:str = obj["VendorID"]
      """  Supplier ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier number  """  
      self.Voided:bool = obj["Voided"]
      """  Voided Flag  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.APPromNoteID:str = obj["APPromNoteID"]
      """  AP Payment Instrument ID  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix  """  
      self.CompanyAddr1:str = obj["CompanyAddr1"]
      """  First company address line.  """  
      self.CompanyAddr2:str = obj["CompanyAddr2"]
      """  Second company address line.  """  
      self.CompanyAddr3:str = obj["CompanyAddr3"]
      """  Third company address line.  """  
      self.CompanyCity:str = obj["CompanyCity"]
      """  Company City portion of the address.  """  
      self.CompanyCountry:str = obj["CompanyCountry"]
      """  Company Country portion of the address.  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Company Name  """  
      self.CompanyPostalCode:str = obj["CompanyPostalCode"]
      """  Company Postal Code or Zip Code portion of the address.  """  
      self.CompanyState:str = obj["CompanyState"]
      """  Company State portion of the address.  """  
      self.SupplierAddr1:str = obj["SupplierAddr1"]
      """  First supplier address line.  """  
      self.SupplierAddr2:str = obj["SupplierAddr2"]
      """  Second supplier address line.  """  
      self.SupplierAddr3:str = obj["SupplierAddr3"]
      """  Third supplier address line.  """  
      self.SupplierCity:str = obj["SupplierCity"]
      """  Company City portion of the address.  """  
      self.SupplierState:str = obj["SupplierState"]
      """  Supplier State portion of the address.  """  
      self.SupplierPostalCode:str = obj["SupplierPostalCode"]
      """  Supplier Postal Code or Zip Code portion of the address.  """  
      self.SupplierName:str = obj["SupplierName"]
      """  Supplier Name  """  
      self.SupplierCountry:str = obj["SupplierCountry"]
      """  Supplier Country portion of the address.  """  
      self.PIStatus:str = obj["PIStatus"]
      """   Payment Instrument Status -
Values are:
Empty string - not linked to a Payment Instrument
"O" (letter o) - Paid by outstanding Payment Instrument
"C" - Paid by collected Payment Instrument  """  
      self.Type:str = obj["Type"]
      """  Promissory Note Type  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Issue Date  """  
      self.CompIBANCode:str = obj["CompIBANCode"]
      """  IBAN Code for company's bank.  """  
      self.CompBankBranchCode:str = obj["CompBankBranchCode"]
      """  Bank/Branch Code for company's bank.  """  
      self.CustBankBranchCode:str = obj["CustBankBranchCode"]
      """  Bank/Branch Code for customer's bank.  """  
      self.CustIBANCode:str = obj["CustIBANCode"]
      """  IBAN Code for customer's bank.  """  
      self.ForceDiscount:bool = obj["ForceDiscount"]
      """  When selected, this field will force the best discount percentage, according to the invoice?s terms definition, to be used.  """  
      self.PaymentTotal:int = obj["PaymentTotal"]
      """  Total paid amount in Base  """  
      self.Variance:int = obj["Variance"]
      """  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.IsEnterTotal:bool = obj["IsEnterTotal"]
      """  Enter Totals flag  """  
      self.Rpt1Variance:int = obj["Rpt1Variance"]
      """  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt2Variance:int = obj["Rpt2Variance"]
      """  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt3Variance:int = obj["Rpt3Variance"]
      """  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.DocVariance:int = obj["DocVariance"]
      """  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  """  
      self.DocPaymentTotal:int = obj["DocPaymentTotal"]
      """  Total paid amount in payment currency  """  
      self.PaymentBankRate:int = obj["PaymentBankRate"]
      """  Exchange rate from the payment currency to the Bank currency  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.Rpt1PaymentTotal:int = obj["Rpt1PaymentTotal"]
      """  Total paid amount in Rpt1 currency  """  
      self.Rpt2PaymentTotal:int = obj["Rpt2PaymentTotal"]
      """  Total paid amount in Rpt2 currency  """  
      self.Rpt3PaymentTotal:int = obj["Rpt3PaymentTotal"]
      """  Total paid amount in Rpt3 currency  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the payment instrument for.  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the payment instrument was cleared in the system (System Set).  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the payment instrument (System Set).  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the payment instrument was cleared on.  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.ClearedPI:bool = obj["ClearedPI"]
      """  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.DocClearedAmt:int = obj["DocClearedAmt"]
      """  Amount that the bank cleared the check for.(Vendors Currency)  """  
      self.Rpt1ClearedAmt:int = obj["Rpt1ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClearedAmt:int = obj["Rpt2ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClearedAmt:int = obj["Rpt3ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.FirstHeadNum:int = obj["FirstHeadNum"]
      """  Reference to the first checkhed  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if manually printed.  If manual then user must enter the APPRomNoteID  """  
      self.ChgComment:str = obj["ChgComment"]
      """  Reason to change the Customer or Company information  """  
      self.PymtCntr:bool = obj["PymtCntr"]
      """  Indicates APPRomNoteID was generated using AP CheckHed numbering  """  
      self.PIStage:str = obj["PIStage"]
      """  Payment Instrument Stage  """  
      self.LockRate:bool = obj["LockRate"]
      """  Lock Exchange Rate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.SupplierCountryNum:int = obj["SupplierCountryNum"]
      """  SupplierCountryNum  """  
      self.BankAccountEnabled:bool = obj["BankAccountEnabled"]
      """  Enable the Bank Account Search Button  """  
      self.BankCurrCode:str = obj["BankCurrCode"]
      """  Bank Currency Code  """  
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.PaymentAmount:int = obj["PaymentAmount"]
      self.PaymentStatus:str = obj["PaymentStatus"]
      self.CompanyBankAcct:str = obj["CompanyBankAcct"]
      self.CompanyBankIdentifier:str = obj["CompanyBankIdentifier"]
      self.CompanyBankName:str = obj["CompanyBankName"]
      self.VendBankName:str = obj["VendBankName"]
      self.VendBankAcct:str = obj["VendBankAcct"]
      self.VendBankIdentifier:str = obj["VendBankIdentifier"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.EnterPaymentTotal:bool = obj["EnterPaymentTotal"]
      self.FullyPaid:bool = obj["FullyPaid"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      self.XRateLabelPaymentBank:str = obj["XRateLabelPaymentBank"]
      self.XRateLabelPaymentBase:str = obj["XRateLabelPaymentBase"]
      self.VoidDate:str = obj["VoidDate"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for miscellaneous shipments  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.CompanyCountryNum:int = obj["CompanyCountryNum"]
      """  Field to bring the Company Country Name  """  
      self.TypeDesc:str = obj["TypeDesc"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.GainLossReal:int = obj["GainLossReal"]
      self.DocGainLossReal:int = obj["DocGainLossReal"]
      self.Rpt1GainLossReal:int = obj["Rpt1GainLossReal"]
      self.Rpt2GainLossReal:int = obj["Rpt2GainLossReal"]
      self.Rpt3GainLossReal:int = obj["Rpt3GainLossReal"]
      self.DocGainLossUnreal:int = obj["DocGainLossUnreal"]
      self.GainLossUnreal:int = obj["GainLossUnreal"]
      self.Rpt1GainLossUnreal:int = obj["Rpt1GainLossUnreal"]
      self.Rpt2GainLossUnreal:int = obj["Rpt2GainLossUnreal"]
      self.Rpt3GainLossUnreal:int = obj["Rpt3GainLossUnreal"]
      self.RevalDate:str = obj["RevalDate"]
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      """  The Bank's full name.  """  
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      """  Full description of the bank account.  """  
      self.BaseCurrSymbolDocumentDesc:str = obj["BaseCurrSymbolDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.BaseCurrSymbolCurrName:str = obj["BaseCurrSymbolCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.BaseCurrSymbolCurrDesc:str = obj["BaseCurrSymbolCurrDesc"]
      """  Description of the currency  """  
      self.BaseCurrSymbolCurrSymbol:str = obj["BaseCurrSymbolCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.BaseCurrSymbolCurrencyID:str = obj["BaseCurrSymbolCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.PIStatusStatusDesc:str = obj["PIStatusStatusDesc"]
      """  Status Description  """  
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      """  Description  """  
      self.VendBankAcctIDBankName:str = obj["VendBankAcctIDBankName"]
      """  Supplier Bank Name  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APPNHeadRow:
   def __init__(self, obj):
      self.AppliedAmount:int = obj["AppliedAmount"]
      """  Applied Amount. Base Currency.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account of the promissory note.  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Amount  """  
      self.BankSlip:str = obj["BankSlip"]
      """  Bank Slip Number of the promissory note.  """  
      self.BankTotalAmt:int = obj["BankTotalAmt"]
      """  Bank Total Amount.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  Cash book Number.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CompBankAcctID:str = obj["CompBankAcctID"]
      """  Bank Account ID of the company.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code of the promissory note.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount amount in base currency.  """  
      self.DocPNAmt:int = obj["DocPNAmt"]
      """  Promissory Note amount in document currency.  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the promissory note.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Entry Person.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate of the promissory note.  """  
      self.Paid:bool = obj["Paid"]
      """  Indicates if the promissory node is fully paid.  """  
      self.PNAmt:int = obj["PNAmt"]
      """  Promissory note amount in base currency.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates that the promissory note is posted.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group Code.  """  
      self.Rpt1PNAmt:int = obj["Rpt1PNAmt"]
      """  Promissory Note Amount in Report Currency 1.  """  
      self.Rpt1Discountamt:int = obj["Rpt1Discountamt"]
      """  Promissory Note Discount Amount in Report Currency 1.  """  
      self.Rpt1BankTotalAmt:int = obj["Rpt1BankTotalAmt"]
      """  Promissory Note Bank Total Amount in Report Currency 1.  """  
      self.Rpt2PNAmt:int = obj["Rpt2PNAmt"]
      """  Promissory Note Amount in Report Currency 2.  """  
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      """  Promissory Note Discount Amount in Report Currency 2.  """  
      self.Rpt2BankTotalAmt:int = obj["Rpt2BankTotalAmt"]
      """  Promissory Note Bank Total Amount in Report Currency 2.  """  
      self.Rpt3PNAmt:int = obj["Rpt3PNAmt"]
      """  Promissory Note Amount in Report Currency 3.  """  
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      """  Promissory Note Discount Amount in Report Currency 3.  """  
      self.Rpt3BankTotalAmt:int = obj["Rpt3BankTotalAmt"]
      """  Promissory Note Bank Total Amount in Report Currency 3.  """  
      self.Signed:bool = obj["Signed"]
      """  Indicates that the promissory note is signed.  """  
      self.TotalAPAmt:int = obj["TotalAPAmt"]
      """  Total AP Amount  """  
      self.TransDate:str = obj["TransDate"]
      """  Transaction date.  """  
      self.VendBankAcctID:str = obj["VendBankAcctID"]
      """  Supplier Bank Account ID  """  
      self.VendorID:str = obj["VendorID"]
      """  Supplier ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier number  """  
      self.Voided:bool = obj["Voided"]
      """  Voided Flag  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.APPromNoteID:str = obj["APPromNoteID"]
      """  AP Payment Instrument ID  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix  """  
      self.CompanyAddr1:str = obj["CompanyAddr1"]
      """  First company address line.  """  
      self.CompanyAddr2:str = obj["CompanyAddr2"]
      """  Second company address line.  """  
      self.CompanyAddr3:str = obj["CompanyAddr3"]
      """  Third company address line.  """  
      self.CompanyCity:str = obj["CompanyCity"]
      """  Company City portion of the address.  """  
      self.CompanyCountry:str = obj["CompanyCountry"]
      """  Company Country portion of the address.  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Company Name  """  
      self.CompanyPostalCode:str = obj["CompanyPostalCode"]
      """  Company Postal Code or Zip Code portion of the address.  """  
      self.CompanyState:str = obj["CompanyState"]
      """  Company State portion of the address.  """  
      self.SupplierAddr1:str = obj["SupplierAddr1"]
      """  First supplier address line.  """  
      self.SupplierAddr2:str = obj["SupplierAddr2"]
      """  Second supplier address line.  """  
      self.SupplierAddr3:str = obj["SupplierAddr3"]
      """  Third supplier address line.  """  
      self.SupplierCity:str = obj["SupplierCity"]
      """  Company City portion of the address.  """  
      self.SupplierState:str = obj["SupplierState"]
      """  Supplier State portion of the address.  """  
      self.SupplierPostalCode:str = obj["SupplierPostalCode"]
      """  Supplier Postal Code or Zip Code portion of the address.  """  
      self.SupplierName:str = obj["SupplierName"]
      """  Supplier Name  """  
      self.SupplierCountry:str = obj["SupplierCountry"]
      """  Supplier Country portion of the address.  """  
      self.PIStatus:str = obj["PIStatus"]
      """   Payment Instrument Status -
Values are:
Empty string - not linked to a Payment Instrument
"O" (letter o) - Paid by outstanding Payment Instrument
"C" - Paid by collected Payment Instrument  """  
      self.Type:str = obj["Type"]
      """  Promissory Note Type  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Issue Date  """  
      self.CompIBANCode:str = obj["CompIBANCode"]
      """  IBAN Code for company's bank.  """  
      self.CompBankBranchCode:str = obj["CompBankBranchCode"]
      """  Bank/Branch Code for company's bank.  """  
      self.CustBankBranchCode:str = obj["CustBankBranchCode"]
      """  Bank/Branch Code for customer's bank.  """  
      self.CustIBANCode:str = obj["CustIBANCode"]
      """  IBAN Code for customer's bank.  """  
      self.ForceDiscount:bool = obj["ForceDiscount"]
      """  When selected, this field will force the best discount percentage, according to the invoice?s terms definition, to be used.  """  
      self.PaymentTotal:int = obj["PaymentTotal"]
      """  Total paid amount in Base  """  
      self.Variance:int = obj["Variance"]
      """  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.IsEnterTotal:bool = obj["IsEnterTotal"]
      """  Enter Totals flag  """  
      self.Rpt1Variance:int = obj["Rpt1Variance"]
      """  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt2Variance:int = obj["Rpt2Variance"]
      """  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt3Variance:int = obj["Rpt3Variance"]
      """  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.DocVariance:int = obj["DocVariance"]
      """  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  """  
      self.DocPaymentTotal:int = obj["DocPaymentTotal"]
      """  Total paid amount in payment currency  """  
      self.PaymentBankRate:int = obj["PaymentBankRate"]
      """  Exchange rate from the payment currency to the Bank currency  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.Rpt1PaymentTotal:int = obj["Rpt1PaymentTotal"]
      """  Total paid amount in Rpt1 currency  """  
      self.Rpt2PaymentTotal:int = obj["Rpt2PaymentTotal"]
      """  Total paid amount in Rpt2 currency  """  
      self.Rpt3PaymentTotal:int = obj["Rpt3PaymentTotal"]
      """  Total paid amount in Rpt3 currency  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the payment instrument for.  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the payment instrument was cleared in the system (System Set).  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the payment instrument (System Set).  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the payment instrument was cleared on.  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.ClearedPI:bool = obj["ClearedPI"]
      """  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.DocClearedAmt:int = obj["DocClearedAmt"]
      """  Amount that the bank cleared the check for.(Vendors Currency)  """  
      self.Rpt1ClearedAmt:int = obj["Rpt1ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClearedAmt:int = obj["Rpt2ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClearedAmt:int = obj["Rpt3ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.FirstHeadNum:int = obj["FirstHeadNum"]
      """  Reference to the first checkhed  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if manually printed.  If manual then user must enter the APPRomNoteID  """  
      self.ChgComment:str = obj["ChgComment"]
      """  Reason to change the Customer or Company information  """  
      self.PymtCntr:bool = obj["PymtCntr"]
      """  Indicates APPRomNoteID was generated using AP CheckHed numbering  """  
      self.PIStage:str = obj["PIStage"]
      """  Payment Instrument Stage  """  
      self.LockRate:bool = obj["LockRate"]
      """  Lock Exchange Rate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankClearedAmt:int = obj["BankClearedAmt"]
      """  BankClearedAmt  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.SupplierCountryNum:int = obj["SupplierCountryNum"]
      """  SupplierCountryNum  """  
      self.EndorsedARPNGroupID:str = obj["EndorsedARPNGroupID"]
      """  Reference to Endorsed AR PI GroupID.  """  
      self.EndorsedARPNHeadNum:int = obj["EndorsedARPNHeadNum"]
      """  Reference to Endorsed AR PI HeadNum.  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.BankAccountEnabled:bool = obj["BankAccountEnabled"]
      """  Enable the Bank Account Search Button  """  
      self.BankCurrCode:str = obj["BankCurrCode"]
      """  Bank Currency Code  """  
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      self.BankFeeAmt:int = obj["BankFeeAmt"]
      self.BankRecGainLoss:int = obj["BankRecGainLoss"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CompanyBankAcct:str = obj["CompanyBankAcct"]
      self.CompanyBankIdentifier:str = obj["CompanyBankIdentifier"]
      self.CompanyBankName:str = obj["CompanyBankName"]
      self.CompanyCountryNum:int = obj["CompanyCountryNum"]
      """  Field to bring the Company Country Name  """  
      self.DisableBankAmt:bool = obj["DisableBankAmt"]
      """   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  """  
      self.DocAllocAmt:int = obj["DocAllocAmt"]
      self.DocBankFeeAmt:int = obj["DocBankFeeAmt"]
      self.DocBankRecGainLoss:int = obj["DocBankRecGainLoss"]
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      self.DocGainLossReal:int = obj["DocGainLossReal"]
      self.DocGainLossUnreal:int = obj["DocGainLossUnreal"]
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.EnterPaymentTotal:bool = obj["EnterPaymentTotal"]
      self.FullyPaid:bool = obj["FullyPaid"]
      self.GainLossReal:int = obj["GainLossReal"]
      self.GainLossUnreal:int = obj["GainLossUnreal"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for miscellaneous shipments  """  
      self.IsFiltered:bool = obj["IsFiltered"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.PaymentAmount:int = obj["PaymentAmount"]
      self.PaymentStatus:str = obj["PaymentStatus"]
      self.RevalDate:str = obj["RevalDate"]
      self.Rpt1AllocAmt:int = obj["Rpt1AllocAmt"]
      self.Rpt1BankFeeAmt:int = obj["Rpt1BankFeeAmt"]
      self.Rpt1BankRecGainLoss:int = obj["Rpt1BankRecGainLoss"]
      self.Rpt1GainLossReal:int = obj["Rpt1GainLossReal"]
      self.Rpt1GainLossUnreal:int = obj["Rpt1GainLossUnreal"]
      self.Rpt2AllocAmt:int = obj["Rpt2AllocAmt"]
      self.Rpt2BankFeeAmt:int = obj["Rpt2BankFeeAmt"]
      self.Rpt2BankRecGainLoss:int = obj["Rpt2BankRecGainLoss"]
      self.Rpt2GainLossReal:int = obj["Rpt2GainLossReal"]
      self.Rpt2GainLossUnreal:int = obj["Rpt2GainLossUnreal"]
      self.Rpt3AllocAmt:int = obj["Rpt3AllocAmt"]
      self.Rpt3BankFeeAmt:int = obj["Rpt3BankFeeAmt"]
      self.Rpt3BankRecGainLoss:int = obj["Rpt3BankRecGainLoss"]
      self.Rpt3GainLossReal:int = obj["Rpt3GainLossReal"]
      self.Rpt3GainLossUnreal:int = obj["Rpt3GainLossUnreal"]
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.StatusChgLegalNum:str = obj["StatusChgLegalNum"]
      self.StatusChgTranDocType:str = obj["StatusChgTranDocType"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      self.TypeDesc:str = obj["TypeDesc"]
      self.VendBankAcct:str = obj["VendBankAcct"]
      self.VendBankIdentifier:str = obj["VendBankIdentifier"]
      self.VendBankName:str = obj["VendBankName"]
      self.VoidDate:str = obj["VoidDate"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.XRateLabelPaymentBank:str = obj["XRateLabelPaymentBank"]
      self.XRateLabelPaymentBase:str = obj["XRateLabelPaymentBase"]
      self.AllocAmt:int = obj["AllocAmt"]
      self.EndorsedARPNStatus:str = obj["EndorsedARPNStatus"]
      """  Endorsed AR PI Status  """  
      self.EndorsedARPNStatusChgTranDocType:str = obj["EndorsedARPNStatusChgTranDocType"]
      """  Endorsed AR PI Status Change Transaction Document Type.  """  
      self.EndorsedARPNStatusChgLegalNum:str = obj["EndorsedARPNStatusChgLegalNum"]
      """  Endorsed AR PI Status Change Legal Number.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BaseCurrSymbolCurrencyID:str = obj["BaseCurrSymbolCurrencyID"]
      self.BaseCurrSymbolCurrSymbol:str = obj["BaseCurrSymbolCurrSymbol"]
      self.BaseCurrSymbolCurrDesc:str = obj["BaseCurrSymbolCurrDesc"]
      self.BaseCurrSymbolDocumentDesc:str = obj["BaseCurrSymbolDocumentDesc"]
      self.BaseCurrSymbolCurrName:str = obj["BaseCurrSymbolCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.PIStatusStatusDesc:str = obj["PIStatusStatusDesc"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APPNHeadTGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.TGLCTranNum:int = obj["TGLCTranNum"]
      """  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  """  
      self.GLAcctContext:str = obj["GLAcctContext"]
      """  String identifier of the account context.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  """  
      self.COACode:str = obj["COACode"]
      """  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  """  
      self.UserCanModify:bool = obj["UserCanModify"]
      """  Indicates if the user can update or delete this record.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  Segement Value 1 of the account for this context.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  Segement Value 2 of the account for this context.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  Segement Value 3 of the account for this context.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  Segement Value 4 of the account for this context.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  Segement Value 5 of the account for this context.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  Segement Value 6 of the account for this context.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  Segement Value 7 of the account for this context.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  Segement Value 8 of the account for this context.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  Segement Value 9 of the account for this context.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  Segement Value 10 of the account for this context.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  Segement Value 11 of the account for this context.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  Segement Value 12 of the account for this context.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  Segement Value 13 of the account for this context.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  Segement Value 14 of the account for this context.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  Segement Value 15 of the account for this context.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  Segement Value 16 of the account for this context.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  Segement Value 17 of the account for this context.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  Segement Value 18 of the account for this context.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  Segement Value 19 of the account for this context.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  Segement Value 20 of the account for this context.  """  
      self.SysGLControlType:str = obj["SysGLControlType"]
      """  Unique Identifier of the system GL Control Type.  """  
      self.SysGLControlCode:str = obj["SysGLControlCode"]
      """  System generated GL Control Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year of the related GLJrnDtl.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode of the related GLJrnDtl.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal number of the related GLJrnDtl.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  JournalLine of the related GLJrnDtl.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction date of the transaction.  This is used in order to display the transactions in date order.  """  
      self.TranSource:str = obj["TranSource"]
      """   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.SysDate:str = obj["SysDate"]
      """  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.SysTime:int = obj["SysTime"]
      """  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.TranNum:int = obj["TranNum"]
      """  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  """  
      self.TransAmt:int = obj["TransAmt"]
      """  Transaction amount that this transaction posted to the related GlJrnDtl.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line Number associated with this GL Journal  """  
      self.SeqNum:int = obj["SeqNum"]
      """  The sequence number associated with this GL journal  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  Credit Amount.  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  Debit Amount.  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  BookCreditAmount  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  Book Debit Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.RecordType:str = obj["RecordType"]
      """   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equals ABTUID which was created during posting  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Technical identifier.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.IsModifiedByUser:bool = obj["IsModifiedByUser"]
      """  IsModifiedByUser  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.MovementType:str = obj["MovementType"]
      """  MovementType  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum of APNHead  """  
      self.IsFiltered:bool = obj["IsFiltered"]
      self.GroupID:str = obj["GroupID"]
      """  GroupID for APPNHead  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BankTranGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.TGLCTranNum:int = obj["TGLCTranNum"]
      """  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  """  
      self.GLAcctContext:str = obj["GLAcctContext"]
      """  String identifier of the account context.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  """  
      self.COACode:str = obj["COACode"]
      """  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  """  
      self.UserCanModify:bool = obj["UserCanModify"]
      """  Indicates if the user can update or delete this record.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  Segement Value 1 of the account for this context.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  Segement Value 2 of the account for this context.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  Segement Value 3 of the account for this context.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  Segement Value 4 of the account for this context.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  Segement Value 5 of the account for this context.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  Segement Value 6 of the account for this context.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  Segement Value 7 of the account for this context.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  Segement Value 8 of the account for this context.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  Segement Value 9 of the account for this context.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  Segement Value 10 of the account for this context.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  Segement Value 11 of the account for this context.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  Segement Value 12 of the account for this context.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  Segement Value 13 of the account for this context.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  Segement Value 14 of the account for this context.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  Segement Value 15 of the account for this context.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  Segement Value 16 of the account for this context.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  Segement Value 17 of the account for this context.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  Segement Value 18 of the account for this context.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  Segement Value 19 of the account for this context.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  Segement Value 20 of the account for this context.  """  
      self.SysGLControlType:str = obj["SysGLControlType"]
      """  Unique Identifier of the system GL Control Type.  """  
      self.SysGLControlCode:str = obj["SysGLControlCode"]
      """  System generated GL Control Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year of the related GLJrnDtl.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode of the related GLJrnDtl.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal number of the related GLJrnDtl.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  JournalLine of the related GLJrnDtl.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction date of the transaction.  This is used in order to display the transactions in date order.  """  
      self.TranSource:str = obj["TranSource"]
      """   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.SysDate:str = obj["SysDate"]
      """  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.SysTime:int = obj["SysTime"]
      """  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.TranNum:int = obj["TranNum"]
      """  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  """  
      self.TransAmt:int = obj["TransAmt"]
      """  Transaction amount that this transaction posted to the related GlJrnDtl.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line Number associated with this GL Journal  """  
      self.SeqNum:int = obj["SeqNum"]
      """  The sequence number associated with this GL journal  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  Credit Amount.  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  Debit Amount.  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  BookCreditAmount  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  Book Debit Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.RecordType:str = obj["RecordType"]
      """   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equals ABTUID which was created during posting  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Technical identifier.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.IsModifiedByUser:bool = obj["IsModifiedByUser"]
      """  IsModifiedByUser  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.MovementType:str = obj["MovementType"]
      """  MovementType  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.Voided:bool = obj["Voided"]
      self.BankAcctID:str = obj["BankAcctID"]
      """  Added to fix generation bug only. (for relation LRBankTranBankTranGLC)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BankTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Relates record to a BankAcct.  """  
      self.TranNum:int = obj["TranNum"]
      """  Unique ID of the Transaction.  """  
      self.TranDate:str = obj["TranDate"]
      """  Date that the transaction took place.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Amount of the Transaction  """  
      self.TranRef:str = obj["TranRef"]
      """  Transaction Reference  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates that the Transaction (not cleared variance) has been posted to G/L.  When the Bank Statement is posted all Non-G/L Posted adjustments for the bank are posted to G/L using the Bank Account's Cash and Bank Fee Accounts. G/L Posted Transactions cannot be deleted. (System Set)  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Person who entered the transaction (System Set).  """  
      self.EntryDate:str = obj["EntryDate"]
      """  Date that the Transaction was entered into the system (System Set).  """  
      self.EntryTime:str = obj["EntryTime"]
      """  Time that the transaction was entered into the system - in HH:MM:SS format (System Set).  """  
      self.TranCleared:bool = obj["TranCleared"]
      """  Indicates the transaction's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.TranClearPending:bool = obj["TranClearPending"]
      """  Indicates that the transaction is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.TranClearedAmt:int = obj["TranClearedAmt"]
      """  Amount that the Transaction was cleared for.  """  
      self.TranClearedPerson:str = obj["TranClearedPerson"]
      """  Person who cleared the transaction (System Set).  """  
      self.TranClearedDate:str = obj["TranClearedDate"]
      """  Date that the Transaction was cleared in the system (System Set).  """  
      self.TranClearedTime:str = obj["TranClearedTime"]
      """  Time that the transaction was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.BankSlip:str = obj["BankSlip"]
      """  The identifier of the Bank Slip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year that entry applies to.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period the transaction was posted to. Only pertains to when posted to GL.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal Number of related GLJrnDtl.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code of the related GLJrnDtl.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Document amount of the Transaction  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange rate that is used for this bank transaction.  """  
      self.DocTranClearedAmt:int = obj["DocTranClearedAmt"]
      """  Document amount that the Transaction was cleared for.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "group" that the transaction is assigned to.  All transactions belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post the transactions.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.GLRefType:str = obj["GLRefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.GLRefCode:str = obj["GLRefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.GLRefCodeDesc:str = obj["GLRefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranClearedAmt:int = obj["Rpt1TranClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranClearedAmt:int = obj["Rpt2TranClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranClearedAmt:int = obj["Rpt3TranClearedAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix that entry applies to.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      """  Unique ID of the Fee  """  
      self.BankFeeAmt:int = obj["BankFeeAmt"]
      """  The Fee amount; this amount plus the Fee tax amount will compose the total of the charge on the statement  """  
      self.BankFeeTaxAmt:int = obj["BankFeeTaxAmt"]
      """  The Tax Amount that has been charged to the fee  """  
      self.DocBankFeeAmt:int = obj["DocBankFeeAmt"]
      """  The Fee amount in Base Currency  """  
      self.DocBankFeeTaxAmt:int = obj["DocBankFeeTaxAmt"]
      """  The Tax Amount that has been charged to the fee in Base Currency  """  
      self.Rpt1BankFeeAmt:int = obj["Rpt1BankFeeAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2BankFeeAmt:int = obj["Rpt2BankFeeAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3BankFeeAmt:int = obj["Rpt3BankFeeAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1BankFeeTaxAmt:int = obj["Rpt1BankFeeTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2BankFeeTaxAmt:int = obj["Rpt2BankFeeTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3BankFeeTaxAmt:int = obj["Rpt3BankFeeTaxAmt"]
      """  Reporting currency value of this field  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Used for Bank Fee Functionality, indicates the module that created this BankFee.  This is assigned by the system.
Values can be; AR, AP and BA.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Consecutive from the AP and AR transactions, this field is used to identify the AP or AR transaction that created this Bank Fee  """  
      self.Voided:bool = obj["Voided"]
      """  Indiates if the BankTran has been voided.  The TranNum field will be the same as the original transaction  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.GainLossType:str = obj["GainLossType"]
      """  "R" for realized or "U" for unrealized Gain/Loss  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.ReverseGL:bool = obj["ReverseGL"]
      """  Indicates if it's a reversing Gain/Loss adjustment  """  
      self.RevalueDate:str = obj["RevalueDate"]
      """  Revaluation date that generated the gain/loss record  """  
      self.RevalueBal:int = obj["RevalueBal"]
      """  Bank Balance at the time of revaluation  """  
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      """  Document currency Bank Balance at the time of revaluation  """  
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      """  Reporting currency Bank Balance at the time of revaluation  """  
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      """  Reporting currency Bank Balance at the time of revaluation  """  
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      """  Reporting currency Bank Balance at the time of revaluation  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number for the record.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document for the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CNCFICode:str = obj["CNCFICode"]
      """  CNCFICode  """  
      self.CNToCFICode:str = obj["CNToCFICode"]
      """  CNToCFICode  """  
      self.BankRecGainLoss:int = obj["BankRecGainLoss"]
      """  BankRecGainLoss  """  
      self.Rpt1BankRecGainLoss:int = obj["Rpt1BankRecGainLoss"]
      """  Rpt1BankRecGainLoss  """  
      self.Rpt2BankRecGainLoss:int = obj["Rpt2BankRecGainLoss"]
      """  Rpt2BankRecGainLoss  """  
      self.Rpt3BankRecGainLoss:int = obj["Rpt3BankRecGainLoss"]
      """  Rpt3BankRecGainLoss  """  
      self.BalanceUpdated:int = obj["BalanceUpdated"]
      """  BalanceUpdated  """  
      self.DocBankRecGainLoss:int = obj["DocBankRecGainLoss"]
      """  DocBankRecGainLoss  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.BankBatchExcluded:bool = obj["BankBatchExcluded"]
      """  Indicates that transaction is currently excluded from batch in Bank Statement Processing.  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.ABTUID:str = obj["ABTUID"]
      """  ABTUID  """  
      self.Plant:str = obj["Plant"]
      """  Multi-Site related Site  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.CNCFICodeDescription:str = obj["CNCFICodeDescription"]
      self.CRCurrCode:str = obj["CRCurrCode"]
      """  Cash Receipt currency code  """  
      self.CRRateGrpCode:str = obj["CRRateGrpCode"]
      """  Cash Receipt Rate group code  """  
      self.CRTranAmt:int = obj["CRTranAmt"]
      """  Cash Receipt Tran amount  """  
      self.CRTranClearedAmt:int = obj["CRTranClearedAmt"]
      """  Cash Receipt Transaction Cleared Amount  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currency Switch  """  
      self.DisableBankAmt:bool = obj["DisableBankAmt"]
      """   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  """  
      self.DispAmtReverse:bool = obj["DispAmtReverse"]
      """  The flag to indicate if the Display amount is supposed to be reversed  """  
      self.DispDocTranAmt:int = obj["DispDocTranAmt"]
      self.DispDocTranClearedAmt:int = obj["DispDocTranClearedAmt"]
      self.DispTranAmt:int = obj["DispTranAmt"]
      self.DispTranClearedAmt:int = obj["DispTranClearedAmt"]
      self.InternalDate:str = obj["InternalDate"]
      """  Used for tree structure/parent view definition in Petty Cash Entry  """  
      self.IsFiltered:bool = obj["IsFiltered"]
      self.IsLockedBankRec:bool = obj["IsLockedBankRec"]
      """  Indicates if the record is locked by review journal for bank reconciliation  """  
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      """  Indicates if the legal number is manually generated or system generated  """  
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      """  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  """  
      self.Rpt1DispTranAmt:int = obj["Rpt1DispTranAmt"]
      self.Rpt1DispTranClearedAmt:int = obj["Rpt1DispTranClearedAmt"]
      self.Rpt2DispTranAmt:int = obj["Rpt2DispTranAmt"]
      self.Rpt2DispTranClearedAmt:int = obj["Rpt2DispTranClearedAmt"]
      self.Rpt3DispTranAmt:int = obj["Rpt3DispTranAmt"]
      self.Rpt3DispTranClearedAmt:int = obj["Rpt3DispTranClearedAmt"]
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      self.GLAccount:str = obj["GLAccount"]
      """  Display GL Account  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.BankFeeIDDescription:str = obj["BankFeeIDDescription"]
      self.BankFeeIDTaxCode:str = obj["BankFeeIDTaxCode"]
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  GL Control Identifier.  """  
      self.BusinessEntity:str = obj["BusinessEntity"]
      """  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.GlobalEntityGLC:bool = obj["GlobalEntityGLC"]
      """  Marks this EntityGLC as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the related BankAcct record.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      self.CallCode:str = obj["CallCode"]
      """  CallCode of the related FSCallCd record.  """  
      self.ChargeCode:str = obj["ChargeCode"]
      self.ClassCode:str = obj["ClassCode"]
      """  ClassCode of the related FAClass record.  """  
      self.ClassID:str = obj["ClassID"]
      """  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  """  
      self.ContractCode:str = obj["ContractCode"]
      """  ContractCode of the related FSContCd record.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode of the related Currency record.  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum of the related Customer record  """  
      self.DeductionID:str = obj["DeductionID"]
      """  DeductionID of PRClsDed or PRDeduct.  """  
      self.EmpID:str = obj["EmpID"]
      """  EmpID of the related PREmpMas record.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode of PayTLbr, LabExpCd  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID of ExtCompany table  """  
      self.FromPlant:str = obj["FromPlant"]
      """  FromPlant value of the related PlntTranDef record.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  GroupCode of the related FAGroup record.  """  
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.JCDept:str = obj["JCDept"]
      """  JCDept of the related JCDept record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode of the related MiscChrg or PurMisc record.  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum of the related Part record.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """  PayTypeID of PayType  """  
      self.PerConName:str = obj["PerConName"]
      self.PIStatus:str = obj["PIStatus"]
      """  PI Status  """  
      self.Plant:str = obj["Plant"]
      """  Plant of the related PlantConfCtrl record.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode of the related ProdGrup record.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID of the related Project record.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  PurchCode of the related GLPurch record.  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode of the related GLRate record.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode of the related Reason record.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  ReasonType of the related Reason record.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID of the related SalesCat record.  """  
      self.Shift:int = obj["Shift"]
      """  Shift value of the related JCShift record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode of the related SalesTax record.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  TaxTblID of PRTaxMas or PRClsTax.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  ToPlant value of the related PlntTranDef record.  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  TransferMethod of ExtCompany table  """  
      self.TypeID:str = obj["TypeID"]
      """  Type ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum of the related Vendor record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode of the related Warehse record.  """  
      self.ExpenseTypeCode:str = obj["ExpenseTypeCode"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.OprTypeCode:str = obj["OprTypeCode"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.TIN:str = obj["TIN"]
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
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

class Erp_Tablesets_PITotalsRow:
   def __init__(self, obj):
      self.CashRcv:int = obj["CashRcv"]
      self.DocCashRcv:int = obj["DocCashRcv"]
      self.DocDscTaken:int = obj["DocDscTaken"]
      self.DocGainReal:int = obj["DocGainReal"]
      self.DocGainUnreal:int = obj["DocGainUnreal"]
      self.DscTaken:int = obj["DscTaken"]
      self.GainReal:int = obj["GainReal"]
      self.GainUnreal:int = obj["GainUnreal"]
      self.RevalDate:str = obj["RevalDate"]
      self.Rpt1CashRcv:int = obj["Rpt1CashRcv"]
      self.Rpt1DscTaken:int = obj["Rpt1DscTaken"]
      self.Rpt1GainReal:int = obj["Rpt1GainReal"]
      self.Rpt1GainUnreal:int = obj["Rpt1GainUnreal"]
      self.Rpt2CashRcv:int = obj["Rpt2CashRcv"]
      self.Rpt2DscTaken:int = obj["Rpt2DscTaken"]
      self.Rpt2GainReal:int = obj["Rpt2GainReal"]
      self.Rpt2GainUnreal:int = obj["Rpt2GainUnreal"]
      self.Rpt3CashRcv:int = obj["Rpt3CashRcv"]
      self.Rpt3DscTaken:int = obj["Rpt3DscTaken"]
      self.Rpt3GainReal:int = obj["Rpt3GainReal"]
      self.Rpt3GainUnreal:int = obj["Rpt3GainUnreal"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ApplyInvoiceToGroup_input:
   """ Required : 
   ipGroupID
   ds
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  AP Promissory Note  Group ID  """  
      self.ds:list[Erp_Tablesets_APInvSelTableset] = obj["ds"]
      pass

class ApplyInvoiceToGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APInvSelTableset] = obj["ds"]
      pass

      """  output parameters  """  

class AssignEndorsedARPILegalNumber_input:
   """ Required : 
   ipGroupID
   ipHeadNum
   ipStatusChange
   ds
   dsAPPromNote
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  AP Payment Instrument Group ID  """  
      self.ipHeadNum:int = obj["ipHeadNum"]
      """  AP Payment Instrument Head Number  """  
      self.ipStatusChange:bool = obj["ipStatusChange"]
      """  Call from AP Status Change  """  
      self.ds:list[Erp_Tablesets_LegalNumGenOptsTableset] = obj["ds"]
      self.dsAPPromNote:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["dsAPPromNote"]
      pass

class AssignEndorsedARPILegalNumber_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumGenOptsTableset] = obj["ds"]
      self.dsAPPromNote:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["dsAPPromNote"]
      self.opLegalNumMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class AssignLegalNumber_input:
   """ Required : 
   ipGroupID
   ipHeadNum
   ds
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  Group ID number  """  
      self.ipHeadNum:int = obj["ipHeadNum"]
      """  Header number  """  
      self.ds:list[Erp_Tablesets_LegalNumGenOptsTableset] = obj["ds"]
      pass

class AssignLegalNumber_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumGenOptsTableset] = obj["ds"]
      self.opLegalNumMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CancelStatusChange_input:
   """ Required : 
   groupId
   headNum
   unpostedSeqNum
   """  
   def __init__(self, obj):
      self.groupId:str = obj["groupId"]
      """  Group ID  """  
      self.headNum:int = obj["headNum"]
      """  HeadNum  """  
      self.unpostedSeqNum:int = obj["unpostedSeqNum"]
      """  unpostedSeqNum  """  
      pass

class CancelStatusChange_output:
   def __init__(self, obj):
      pass

class ChangePIType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

class ChangePIType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTranAmt_input:
   """ Required : 
   ipTranAmtType
   proposedTranAmt
   ds
   """  
   def __init__(self, obj):
      self.ipTranAmtType:str = obj["ipTranAmtType"]
      """  Indicate which of the transaction amount is changed.
            Valid values are: 'B' for Base Tran Amount and 'D' for Doc Tran Amount  """  
      self.proposedTranAmt:int = obj["proposedTranAmt"]
      """  The proposed Transaction Amount  """  
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

class ChangeTranAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckDocumentIsLocked_input:
   """ Required : 
   keyValue
   keyValue2
   """  
   def __init__(self, obj):
      self.keyValue:str = obj["keyValue"]
      """  GroupID  """  
      self.keyValue2:str = obj["keyValue2"]
      """  HeadNum  """  
      pass

class CheckDocumentIsLocked_output:
   def __init__(self, obj):
      pass

class CreateAPPNHead_input:
   """ Required : 
   pcGroupID
   ds
   """  
   def __init__(self, obj):
      self.pcGroupID:str = obj["pcGroupID"]
      """  AP Promissory Note  Group ID  """  
      self.ds:list[Erp_Tablesets_APInvSelTableset] = obj["ds"]
      pass

class CreateAPPNHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APInvSelTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateNewAPPNHeadEndorsement_input:
   """ Required : 
   groupID
   endorsedARPNGroupID
   endorsedARPNHeadNum
   ds
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  AP Promissory Note Group ID  """  
      self.endorsedARPNGroupID:str = obj["endorsedARPNGroupID"]
      """  Endorsed AR Promissory Note Group ID  """  
      self.endorsedARPNHeadNum:int = obj["endorsedARPNHeadNum"]
      """  Endorsed AR Promissory Note HeadNum  """  
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

class CreateNewAPPNHeadEndorsement_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateNewAPPNHead_input:
   """ Required : 
   pcGroupID
   ds
   """  
   def __init__(self, obj):
      self.pcGroupID:str = obj["pcGroupID"]
      """  AP Promissory Note Group ID  """  
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

class CreateNewAPPNHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteAPPNMove_input:
   """ Required : 
   groupId
   headNum
   seqNum
   """  
   def __init__(self, obj):
      self.groupId:str = obj["groupId"]
      """  Group ID  """  
      self.headNum:int = obj["headNum"]
      """  HeadNum  """  
      self.seqNum:int = obj["seqNum"]
      """  Seq  """  
      pass

class DeleteAPPNMove_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   groupID
   headNum
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteNegPayment_input:
   """ Required : 
   pcGroupID
   """  
   def __init__(self, obj):
      self.pcGroupID:str = obj["pcGroupID"]
      """  AP Check Group ID  """  
      pass

class DeleteNegPayment_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_APInvSelAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Name:str = obj["Name"]
      self.VendorNum:int = obj["VendorNum"]
      self.DueDate:str = obj["DueDate"]
      self.InvoiceNum:str = obj["InvoiceNum"]
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

class Erp_Tablesets_APInvSelRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Selected:bool = obj["Selected"]
      """  Logical flag indicating if this record is or is not selected to be written to the check files.  """  
      self.Name:str = obj["Name"]
      """  Vendors name. Duplicated from the Vendor.Name. Used as part of the index to organize by name order.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum an element of the foreign key that relates this selection record to the Vendor and APInvHed master files. Duplicated from APInvHed.VendorNum. Also used as an element of  the unique file index.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number. An element of the foreign key  that relates this selection record back to the APInvHed record. Duplicated from the APInvHed.InvoiceNum.  """  
      self.GrossPay:int = obj["GrossPay"]
      """  The Gross Payment that is to be paid against this invoice. When Selected this is set to APInvSel.AmtDue + APInvSel.DiscAvailable as the default.  """  
      self.DocGrossPay:int = obj["DocGrossPay"]
      """  The Gross Payment that is to be paid against this invoice(Vendor Currency). When Selected this is set to APInvSel.AmtDue + APInvSel.DiscAvailable as the default.  """  
      self.DiscAmt:int = obj["DiscAmt"]
      """  Prompt Payment discount to be taken. When selected this field is set to APInvSel.DiscAvailable as a default.  """  
      self.DocDiscAmt:int = obj["DocDiscAmt"]
      """  Prompt Payment discount to be taken(Vendor Currency). When selected this field is set to APInvSel.DiscAvailable as a default.  """  
      self.DueDate:str = obj["DueDate"]
      """  Payment due date of this invoice. Set to APInvHed.DueDate.  """  
      self.NetPay:int = obj["NetPay"]
      """  The Net Payment that is to be made against this invoice.  Set as GrossPay - DiscAmt.  """  
      self.DocNetPay:int = obj["DocNetPay"]
      """  The Net Payment that is to be made against this invoice(Vendor Currency).  Set as GrossPay - DiscAmt.  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """   Total original  invoice Amount.
Duplicated from InvcHead.InvoiceAmt.  """  
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """   Total original  invoice Amount(Vendor Currency).
Duplicated from InvcHead.InvoiceAmt.  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative). Duplicated from InvcHead.InvoiceBal.  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Current outstanding balance(Vendor Currency). Carries a true sign. (Credit memos are negative). Duplicated from InvcHead.InvoiceBal.  """  
      self.AmtDue:int = obj["AmtDue"]
      """  Current payment amount due. This is calculated as the payment schedule amounts that are due - prior payments.  """  
      self.DocAmtDue:int = obj["DocAmtDue"]
      """  Current payment amount due(Vendor Currency). This is calulate as the payment schedule amounts that are due - prior payments.  """  
      self.LastPayDate:str = obj["LastPayDate"]
      """  Last date that a payment was made against this invoice. This is set by finding the last APTran for this invoice.  """  
      self.DiscAvailable:int = obj["DiscAvailable"]
      """  Available Prompt Payment discount. Set during the build selection process. The system can be configured to "Always take discount" or allow the system to determine if discount is only taken when the APInvHed.DiscDate is <= the check date. In either case Discounts are only taken if this is the first payment against this invoice (APInvHed.InvoiceAmt = InvoiceBa). If Discounts are taken then this field is set to APInvHed.DiscAmt.  """  
      self.DocDiscAvailable:int = obj["DocDiscAvailable"]
      """  Available Prompt Payment discount(Vendor Currency). Set during the build selection process. The system can be configured to "Always take discount" or allow the system to determine if discount is only taken when the APInvHed.DiscDate is <= the check date. In either case Discounts are only taken if this is the first payment against this invoice (APInvHed.InvoiceAmt = InvoiceBa). If Discounts are taken then this field is set to APInvHed.DiscAmt.  """  
      self.DebitMemo:bool = obj["DebitMemo"]
      """   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign but will entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  """  
      self.DiscountDate:str = obj["DiscountDate"]
      """  Prompt payment discount due date. The date according to the terms when you are allowed to take the prompt payment discount (if any) given by the vendor. This date is NOT directly maintainable. It is calculated using the InvoiceDate + PurTerms.DiscountDays. If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then this is not applicable and is set to ? (null value).  Copied from APInvHed.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.Rpt1AmtDue:int = obj["Rpt1AmtDue"]
      """  Reporting currency value of this field  """  
      self.Rpt2AmtDue:int = obj["Rpt2AmtDue"]
      """  Reporting currency value of this field  """  
      self.Rpt3AmtDue:int = obj["Rpt3AmtDue"]
      """  Reporting currency value of this field  """  
      self.Rpt1DiscAmt:int = obj["Rpt1DiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscAmt:int = obj["Rpt2DiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscAmt:int = obj["Rpt3DiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1DiscAvailable:int = obj["Rpt1DiscAvailable"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscAvailable:int = obj["Rpt2DiscAvailable"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscAvailable:int = obj["Rpt3DiscAvailable"]
      """  Reporting currency value of this field  """  
      self.Rpt1GrossPay:int = obj["Rpt1GrossPay"]
      """  Reporting currency value of this field  """  
      self.Rpt2GrossPay:int = obj["Rpt2GrossPay"]
      """  Reporting currency value of this field  """  
      self.Rpt3GrossPay:int = obj["Rpt3GrossPay"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt1NetPay:int = obj["Rpt1NetPay"]
      """  Reporting currency value of this field  """  
      self.Rpt2NetPay:int = obj["Rpt2NetPay"]
      """  Reporting currency value of this field  """  
      self.Rpt3NetPay:int = obj["Rpt3NetPay"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.PrePayment:bool = obj["PrePayment"]
      """  Prepayment flag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PEIsDetractionPayment:bool = obj["PEIsDetractionPayment"]
      """  PEIsDetractionPayment  """  
      self.CPayLinked:bool = obj["CPayLinked"]
      """  Indicates if the related invoice is linked to a Central Payment invoice  """  
      self.DiscountAvailable:bool = obj["DiscountAvailable"]
      """  Used by UI to highlight the row if discount is available.  """  
      self.DocNewBalance:int = obj["DocNewBalance"]
      self.GlbCompany:str = obj["GlbCompany"]
      """  This is the source Company of the Central Payment linked invoice  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      self.isDiscountforDebitM:bool = obj["isDiscountforDebitM"]
      self.IsUrgentPayment:bool = obj["IsUrgentPayment"]
      """  CSF Switzerland - Urgent Payment flag from Invoice.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      self.NewBalance:int = obj["NewBalance"]
      self.PayMethod:str = obj["PayMethod"]
      """  Payment Method Name.  """  
      self.Rpt1NewBalance:int = obj["Rpt1NewBalance"]
      self.Rpt2NewBalance:int = obj["Rpt2NewBalance"]
      self.Rpt3NewBalance:int = obj["Rpt3NewBalance"]
      self.TermsCode:str = obj["TermsCode"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      """  TermsCodeDescription  """  
      self.VendorBankID:str = obj["VendorBankID"]
      self.VendorBankName:str = obj["VendorBankName"]
      self.JPBillingNumber:str = obj["JPBillingNumber"]
      self.JPProposalDate:str = obj["JPProposalDate"]
      self.JPSummarizationDate:str = obj["JPSummarizationDate"]
      self.HasWithholdings:bool = obj["HasWithholdings"]
      """  Invoice Has Withholdings  """  
      self.SourcePlant:str = obj["SourcePlant"]
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APInvSelTableset:
   def __init__(self, obj):
      self.APInvSel:list[Erp_Tablesets_APInvSelRow] = obj["APInvSel"]
      self.APInvSelAttch:list[Erp_Tablesets_APInvSelAttchRow] = obj["APInvSelAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_APPNDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.APPNDtlLine:int = obj["APPNDtlLine"]
      """  Line  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID of the promissoiry note.  """  
      self.DiscAmt:int = obj["DiscAmt"]
      """  Discount Amount in base currency.  """  
      self.DocDiscAmt:int = obj["DocDiscAmt"]
      """  Discount Amount in invoice currency.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax amount in invoice currency.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Transaction amount in invoice currency.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Entry Person  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates that the promissory note is posted to the GL.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  AP Invoice Number linked to the promissory note.  """  
      self.RoundDiff:int = obj["RoundDiff"]
      """  Rounding Differences  """  
      self.Rpt1DiscAmt:int = obj["Rpt1DiscAmt"]
      """  Discount Amount in report currency 1.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Tax amount  in report currency 1.  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Transaction amount  in report currency 1.  """  
      self.Rpt2DiscAmt:int = obj["Rpt2DiscAmt"]
      """  Discount Amount in report currency 2.  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Tax amount  in report currency 2.  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Transaction amount  in report currency 2.  """  
      self.Rpt3DiscAmt:int = obj["Rpt3DiscAmt"]
      """  Discount Amount in report currency 3.  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Tax amount  in report currency 3.  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Transaction amount  in report currency 3.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Tax amount in base currency.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Tax Liability  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Transaction Amount in base currency.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction date.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier  """  
      self.HeadNum:int = obj["HeadNum"]
      """  If TranType = "Pay" or "ADJ" for a currency gain/loss  then this is a duplicate of the related CheckHed.HeadNum,  otherwise it is set to zero.  """  
      self.Voided:bool = obj["Voided"]
      """  Indicates if the promissory node is voided.  """  
      self.GroupID:str = obj["GroupID"]
      """  Group ID  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G\L fiscal period that this transaction is posted to. Updated by the check printing process for system printed checks or by the user for manually printed checks.  If entered must be valid in the Fiscal master.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal Year that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYear during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year to each record on the TranDate  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """   Fiscal Year Suffix that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYearSuffix during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year suffix to each record on the TranDate  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  """  
      self.Posted:bool = obj["Posted"]
      """  An internal flag which indicates if this check has been Posted.  If "NO" then it is considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process. This is only applicable for TranType = "Pay".  """  
      self.Description:str = obj["Description"]
      """  In the case of payment details this description is printed on the check stub. If referencing a invoice the APInvHed.Description is used as a default.  """  
      self.TranType:str = obj["TranType"]
      """  An internal flag which identifies the type of transaction. Valid types are "Pay" or "Adj".  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.FirstHeadNum:int = obj["FirstHeadNum"]
      """  Link To first checkhed record  """  
      self.GainLossType:str = obj["GainLossType"]
      """  "R" for realized or "U" for unrealized Gain/Loss  """  
      self.ReverseGL:bool = obj["ReverseGL"]
      """  Indicates if it's a reversing Gain/Loss adjustment  """  
      self.RevalueDate:str = obj["RevalueDate"]
      """  Revaluation date that generated the gain/loss record  """  
      self.RevalueBal:int = obj["RevalueBal"]
      """  PI Balance at the time of revaluation  """  
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      """  Document currency PI Balance at the time of revaluation  """  
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      """  Reporting currency PI Balance at the time of revaluation  """  
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      """  Reporting currency PI Balance at the time of revaluation  """  
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      """  Reporting currency PI Balance at the time of revaluation  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AdjustmentSeq:int = obj["AdjustmentSeq"]
      """  AdjustmentSeq  """  
      self.AmtToAP:int = obj["AmtToAP"]
      self.ApplyDate:str = obj["ApplyDate"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.BaseCurrSymbolCurrDesc:str = obj["BaseCurrSymbolCurrDesc"]
      self.BaseCurrSymbolCurrName:str = obj["BaseCurrSymbolCurrName"]
      self.BaseCurrSymbolCurrSymbol:str = obj["BaseCurrSymbolCurrSymbol"]
      self.BaseCurrSymbolDocumentDesc:str = obj["BaseCurrSymbolDocumentDesc"]
      self.BaseSelfAssessedTax:int = obj["BaseSelfAssessedTax"]
      self.CPayLinked:bool = obj["CPayLinked"]
      """  Indicates if the related invoice is linked to a Central Payment invoice  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencyGainLoss:int = obj["CurrencyGainLoss"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency.CurrSymbol from APInvHed  """  
      self.CurrSymbolCurrDesc:str = obj["CurrSymbolCurrDesc"]
      self.CurrSymbolCurrName:str = obj["CurrSymbolCurrName"]
      self.CurrSymbolCurrSymbol:str = obj["CurrSymbolCurrSymbol"]
      self.CurrSymbolDocumentDesc:str = obj["CurrSymbolDocumentDesc"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  The display gl account.  """  
      self.DispTranAmt:int = obj["DispTranAmt"]
      self.DocBaseSelfAssessedTax:int = obj["DocBaseSelfAssessedTax"]
      self.DocDispTranAmt:int = obj["DocDispTranAmt"]
      self.DocExpenseAmount:int = obj["DocExpenseAmount"]
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      self.DocNetAmount:int = obj["DocNetAmount"]
      self.DocNewBalance:int = obj["DocNewBalance"]
      self.DocUnPostedBal:int = obj["DocUnPostedBal"]
      self.DueDate:str = obj["DueDate"]
      self.ExchangeRate:int = obj["ExchangeRate"]
      self.ExpenseAmount:int = obj["ExpenseAmount"]
      self.FullyPaid:bool = obj["FullyPaid"]
      """  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  This is the source Company of the Central Payment linked invoice  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      self.InvoiceBal:int = obj["InvoiceBal"]
      self.InvoiceDate:str = obj["InvoiceDate"]
      self.LockRate:bool = obj["LockRate"]
      self.NetAmount:int = obj["NetAmount"]
      self.NewBalance:int = obj["NewBalance"]
      self.PostToGL:bool = obj["PostToGL"]
      """  Indicates if posting GL transactions.  """  
      self.TermsCode:str = obj["TermsCode"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.UnPostedBal:int = obj["UnPostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign.  """  
      self.WithHoldTax:int = obj["WithHoldTax"]
      self.DiscountDate:str = obj["DiscountDate"]
      self.ChangeExchangeRateResponse:str = obj["ChangeExchangeRateResponse"]
      """  Yes and No considered valid response.  All other values including blank treated as question was not posed to the user.  """  
      self.DocSelfAssessedTax:int = obj["DocSelfAssessedTax"]
      self.DocWithHoldTax:int = obj["DocWithHoldTax"]
      self.SelfAssessedTax:int = obj["SelfAssessedTax"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.APPromNoteID:str = obj["APPromNoteID"]
      self.PIStatus:str = obj["PIStatus"]
      self.PIStatusStatusDesc:str = obj["PIStatusStatusDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APPNHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
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

class Erp_Tablesets_APPNHeadListRow:
   def __init__(self, obj):
      self.AppliedAmount:int = obj["AppliedAmount"]
      """  Applied Amount. Base Currency.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account of the promissory note.  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Amount  """  
      self.BankSlip:str = obj["BankSlip"]
      """  Bank Slip Number of the promissory note.  """  
      self.BankTotalAmt:int = obj["BankTotalAmt"]
      """  Bank Total Amount.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  Cash book Number.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CompBankAcctID:str = obj["CompBankAcctID"]
      """  Bank Account ID of the company.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code of the promissory note.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount amount in base currency.  """  
      self.DocPNAmt:int = obj["DocPNAmt"]
      """  Promissory Note amount in document currency.  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the promissory note.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Entry Person.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate of the promissory note.  """  
      self.Paid:bool = obj["Paid"]
      """  Indicates if the promissory node is fully paid.  """  
      self.PNAmt:int = obj["PNAmt"]
      """  Promissory note amount in base currency.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates that the promissory note is posted.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group Code.  """  
      self.Rpt1PNAmt:int = obj["Rpt1PNAmt"]
      """  Promissory Note Amount in Report Currency 1.  """  
      self.Rpt1Discountamt:int = obj["Rpt1Discountamt"]
      """  Promissory Note Discount Amount in Report Currency 1.  """  
      self.Rpt1BankTotalAmt:int = obj["Rpt1BankTotalAmt"]
      """  Promissory Note Bank Total Amount in Report Currency 1.  """  
      self.Rpt2PNAmt:int = obj["Rpt2PNAmt"]
      """  Promissory Note Amount in Report Currency 2.  """  
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      """  Promissory Note Discount Amount in Report Currency 2.  """  
      self.Rpt2BankTotalAmt:int = obj["Rpt2BankTotalAmt"]
      """  Promissory Note Bank Total Amount in Report Currency 2.  """  
      self.Rpt3PNAmt:int = obj["Rpt3PNAmt"]
      """  Promissory Note Amount in Report Currency 3.  """  
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      """  Promissory Note Discount Amount in Report Currency 3.  """  
      self.Rpt3BankTotalAmt:int = obj["Rpt3BankTotalAmt"]
      """  Promissory Note Bank Total Amount in Report Currency 3.  """  
      self.Signed:bool = obj["Signed"]
      """  Indicates that the promissory note is signed.  """  
      self.TotalAPAmt:int = obj["TotalAPAmt"]
      """  Total AP Amount  """  
      self.TransDate:str = obj["TransDate"]
      """  Transaction date.  """  
      self.VendBankAcctID:str = obj["VendBankAcctID"]
      """  Supplier Bank Account ID  """  
      self.VendorID:str = obj["VendorID"]
      """  Supplier ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier number  """  
      self.Voided:bool = obj["Voided"]
      """  Voided Flag  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.APPromNoteID:str = obj["APPromNoteID"]
      """  AP Payment Instrument ID  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix  """  
      self.CompanyAddr1:str = obj["CompanyAddr1"]
      """  First company address line.  """  
      self.CompanyAddr2:str = obj["CompanyAddr2"]
      """  Second company address line.  """  
      self.CompanyAddr3:str = obj["CompanyAddr3"]
      """  Third company address line.  """  
      self.CompanyCity:str = obj["CompanyCity"]
      """  Company City portion of the address.  """  
      self.CompanyCountry:str = obj["CompanyCountry"]
      """  Company Country portion of the address.  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Company Name  """  
      self.CompanyPostalCode:str = obj["CompanyPostalCode"]
      """  Company Postal Code or Zip Code portion of the address.  """  
      self.CompanyState:str = obj["CompanyState"]
      """  Company State portion of the address.  """  
      self.SupplierAddr1:str = obj["SupplierAddr1"]
      """  First supplier address line.  """  
      self.SupplierAddr2:str = obj["SupplierAddr2"]
      """  Second supplier address line.  """  
      self.SupplierAddr3:str = obj["SupplierAddr3"]
      """  Third supplier address line.  """  
      self.SupplierCity:str = obj["SupplierCity"]
      """  Company City portion of the address.  """  
      self.SupplierState:str = obj["SupplierState"]
      """  Supplier State portion of the address.  """  
      self.SupplierPostalCode:str = obj["SupplierPostalCode"]
      """  Supplier Postal Code or Zip Code portion of the address.  """  
      self.SupplierName:str = obj["SupplierName"]
      """  Supplier Name  """  
      self.SupplierCountry:str = obj["SupplierCountry"]
      """  Supplier Country portion of the address.  """  
      self.PIStatus:str = obj["PIStatus"]
      """   Payment Instrument Status -
Values are:
Empty string - not linked to a Payment Instrument
"O" (letter o) - Paid by outstanding Payment Instrument
"C" - Paid by collected Payment Instrument  """  
      self.Type:str = obj["Type"]
      """  Promissory Note Type  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Issue Date  """  
      self.CompIBANCode:str = obj["CompIBANCode"]
      """  IBAN Code for company's bank.  """  
      self.CompBankBranchCode:str = obj["CompBankBranchCode"]
      """  Bank/Branch Code for company's bank.  """  
      self.CustBankBranchCode:str = obj["CustBankBranchCode"]
      """  Bank/Branch Code for customer's bank.  """  
      self.CustIBANCode:str = obj["CustIBANCode"]
      """  IBAN Code for customer's bank.  """  
      self.ForceDiscount:bool = obj["ForceDiscount"]
      """  When selected, this field will force the best discount percentage, according to the invoice?s terms definition, to be used.  """  
      self.PaymentTotal:int = obj["PaymentTotal"]
      """  Total paid amount in Base  """  
      self.Variance:int = obj["Variance"]
      """  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.IsEnterTotal:bool = obj["IsEnterTotal"]
      """  Enter Totals flag  """  
      self.Rpt1Variance:int = obj["Rpt1Variance"]
      """  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt2Variance:int = obj["Rpt2Variance"]
      """  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt3Variance:int = obj["Rpt3Variance"]
      """  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.DocVariance:int = obj["DocVariance"]
      """  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  """  
      self.DocPaymentTotal:int = obj["DocPaymentTotal"]
      """  Total paid amount in payment currency  """  
      self.PaymentBankRate:int = obj["PaymentBankRate"]
      """  Exchange rate from the payment currency to the Bank currency  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.Rpt1PaymentTotal:int = obj["Rpt1PaymentTotal"]
      """  Total paid amount in Rpt1 currency  """  
      self.Rpt2PaymentTotal:int = obj["Rpt2PaymentTotal"]
      """  Total paid amount in Rpt2 currency  """  
      self.Rpt3PaymentTotal:int = obj["Rpt3PaymentTotal"]
      """  Total paid amount in Rpt3 currency  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the payment instrument for.  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the payment instrument was cleared in the system (System Set).  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the payment instrument (System Set).  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the payment instrument was cleared on.  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.ClearedPI:bool = obj["ClearedPI"]
      """  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.DocClearedAmt:int = obj["DocClearedAmt"]
      """  Amount that the bank cleared the check for.(Vendors Currency)  """  
      self.Rpt1ClearedAmt:int = obj["Rpt1ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClearedAmt:int = obj["Rpt2ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClearedAmt:int = obj["Rpt3ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.FirstHeadNum:int = obj["FirstHeadNum"]
      """  Reference to the first checkhed  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if manually printed.  If manual then user must enter the APPRomNoteID  """  
      self.ChgComment:str = obj["ChgComment"]
      """  Reason to change the Customer or Company information  """  
      self.PymtCntr:bool = obj["PymtCntr"]
      """  Indicates APPRomNoteID was generated using AP CheckHed numbering  """  
      self.PIStage:str = obj["PIStage"]
      """  Payment Instrument Stage  """  
      self.LockRate:bool = obj["LockRate"]
      """  Lock Exchange Rate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.SupplierCountryNum:int = obj["SupplierCountryNum"]
      """  SupplierCountryNum  """  
      self.BankAccountEnabled:bool = obj["BankAccountEnabled"]
      """  Enable the Bank Account Search Button  """  
      self.BankCurrCode:str = obj["BankCurrCode"]
      """  Bank Currency Code  """  
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.PaymentAmount:int = obj["PaymentAmount"]
      self.PaymentStatus:str = obj["PaymentStatus"]
      self.CompanyBankAcct:str = obj["CompanyBankAcct"]
      self.CompanyBankIdentifier:str = obj["CompanyBankIdentifier"]
      self.CompanyBankName:str = obj["CompanyBankName"]
      self.VendBankName:str = obj["VendBankName"]
      self.VendBankAcct:str = obj["VendBankAcct"]
      self.VendBankIdentifier:str = obj["VendBankIdentifier"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.EnterPaymentTotal:bool = obj["EnterPaymentTotal"]
      self.FullyPaid:bool = obj["FullyPaid"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      self.XRateLabelPaymentBank:str = obj["XRateLabelPaymentBank"]
      self.XRateLabelPaymentBase:str = obj["XRateLabelPaymentBase"]
      self.VoidDate:str = obj["VoidDate"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for miscellaneous shipments  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.CompanyCountryNum:int = obj["CompanyCountryNum"]
      """  Field to bring the Company Country Name  """  
      self.TypeDesc:str = obj["TypeDesc"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.GainLossReal:int = obj["GainLossReal"]
      self.DocGainLossReal:int = obj["DocGainLossReal"]
      self.Rpt1GainLossReal:int = obj["Rpt1GainLossReal"]
      self.Rpt2GainLossReal:int = obj["Rpt2GainLossReal"]
      self.Rpt3GainLossReal:int = obj["Rpt3GainLossReal"]
      self.DocGainLossUnreal:int = obj["DocGainLossUnreal"]
      self.GainLossUnreal:int = obj["GainLossUnreal"]
      self.Rpt1GainLossUnreal:int = obj["Rpt1GainLossUnreal"]
      self.Rpt2GainLossUnreal:int = obj["Rpt2GainLossUnreal"]
      self.Rpt3GainLossUnreal:int = obj["Rpt3GainLossUnreal"]
      self.RevalDate:str = obj["RevalDate"]
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      """  The Bank's full name.  """  
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      """  Full description of the bank account.  """  
      self.BaseCurrSymbolDocumentDesc:str = obj["BaseCurrSymbolDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.BaseCurrSymbolCurrName:str = obj["BaseCurrSymbolCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.BaseCurrSymbolCurrDesc:str = obj["BaseCurrSymbolCurrDesc"]
      """  Description of the currency  """  
      self.BaseCurrSymbolCurrSymbol:str = obj["BaseCurrSymbolCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.BaseCurrSymbolCurrencyID:str = obj["BaseCurrSymbolCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.PIStatusStatusDesc:str = obj["PIStatusStatusDesc"]
      """  Status Description  """  
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      """  Description  """  
      self.VendBankAcctIDBankName:str = obj["VendBankAcctIDBankName"]
      """  Supplier Bank Name  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APPNHeadListTableset:
   def __init__(self, obj):
      self.APPNHeadList:list[Erp_Tablesets_APPNHeadListRow] = obj["APPNHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_APPNHeadRow:
   def __init__(self, obj):
      self.AppliedAmount:int = obj["AppliedAmount"]
      """  Applied Amount. Base Currency.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account of the promissory note.  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Amount  """  
      self.BankSlip:str = obj["BankSlip"]
      """  Bank Slip Number of the promissory note.  """  
      self.BankTotalAmt:int = obj["BankTotalAmt"]
      """  Bank Total Amount.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  Cash book Number.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CompBankAcctID:str = obj["CompBankAcctID"]
      """  Bank Account ID of the company.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code of the promissory note.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount amount in base currency.  """  
      self.DocPNAmt:int = obj["DocPNAmt"]
      """  Promissory Note amount in document currency.  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the promissory note.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Entry Person.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate of the promissory note.  """  
      self.Paid:bool = obj["Paid"]
      """  Indicates if the promissory node is fully paid.  """  
      self.PNAmt:int = obj["PNAmt"]
      """  Promissory note amount in base currency.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates that the promissory note is posted.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group Code.  """  
      self.Rpt1PNAmt:int = obj["Rpt1PNAmt"]
      """  Promissory Note Amount in Report Currency 1.  """  
      self.Rpt1Discountamt:int = obj["Rpt1Discountamt"]
      """  Promissory Note Discount Amount in Report Currency 1.  """  
      self.Rpt1BankTotalAmt:int = obj["Rpt1BankTotalAmt"]
      """  Promissory Note Bank Total Amount in Report Currency 1.  """  
      self.Rpt2PNAmt:int = obj["Rpt2PNAmt"]
      """  Promissory Note Amount in Report Currency 2.  """  
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      """  Promissory Note Discount Amount in Report Currency 2.  """  
      self.Rpt2BankTotalAmt:int = obj["Rpt2BankTotalAmt"]
      """  Promissory Note Bank Total Amount in Report Currency 2.  """  
      self.Rpt3PNAmt:int = obj["Rpt3PNAmt"]
      """  Promissory Note Amount in Report Currency 3.  """  
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      """  Promissory Note Discount Amount in Report Currency 3.  """  
      self.Rpt3BankTotalAmt:int = obj["Rpt3BankTotalAmt"]
      """  Promissory Note Bank Total Amount in Report Currency 3.  """  
      self.Signed:bool = obj["Signed"]
      """  Indicates that the promissory note is signed.  """  
      self.TotalAPAmt:int = obj["TotalAPAmt"]
      """  Total AP Amount  """  
      self.TransDate:str = obj["TransDate"]
      """  Transaction date.  """  
      self.VendBankAcctID:str = obj["VendBankAcctID"]
      """  Supplier Bank Account ID  """  
      self.VendorID:str = obj["VendorID"]
      """  Supplier ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier number  """  
      self.Voided:bool = obj["Voided"]
      """  Voided Flag  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.APPromNoteID:str = obj["APPromNoteID"]
      """  AP Payment Instrument ID  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix  """  
      self.CompanyAddr1:str = obj["CompanyAddr1"]
      """  First company address line.  """  
      self.CompanyAddr2:str = obj["CompanyAddr2"]
      """  Second company address line.  """  
      self.CompanyAddr3:str = obj["CompanyAddr3"]
      """  Third company address line.  """  
      self.CompanyCity:str = obj["CompanyCity"]
      """  Company City portion of the address.  """  
      self.CompanyCountry:str = obj["CompanyCountry"]
      """  Company Country portion of the address.  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Company Name  """  
      self.CompanyPostalCode:str = obj["CompanyPostalCode"]
      """  Company Postal Code or Zip Code portion of the address.  """  
      self.CompanyState:str = obj["CompanyState"]
      """  Company State portion of the address.  """  
      self.SupplierAddr1:str = obj["SupplierAddr1"]
      """  First supplier address line.  """  
      self.SupplierAddr2:str = obj["SupplierAddr2"]
      """  Second supplier address line.  """  
      self.SupplierAddr3:str = obj["SupplierAddr3"]
      """  Third supplier address line.  """  
      self.SupplierCity:str = obj["SupplierCity"]
      """  Company City portion of the address.  """  
      self.SupplierState:str = obj["SupplierState"]
      """  Supplier State portion of the address.  """  
      self.SupplierPostalCode:str = obj["SupplierPostalCode"]
      """  Supplier Postal Code or Zip Code portion of the address.  """  
      self.SupplierName:str = obj["SupplierName"]
      """  Supplier Name  """  
      self.SupplierCountry:str = obj["SupplierCountry"]
      """  Supplier Country portion of the address.  """  
      self.PIStatus:str = obj["PIStatus"]
      """   Payment Instrument Status -
Values are:
Empty string - not linked to a Payment Instrument
"O" (letter o) - Paid by outstanding Payment Instrument
"C" - Paid by collected Payment Instrument  """  
      self.Type:str = obj["Type"]
      """  Promissory Note Type  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Issue Date  """  
      self.CompIBANCode:str = obj["CompIBANCode"]
      """  IBAN Code for company's bank.  """  
      self.CompBankBranchCode:str = obj["CompBankBranchCode"]
      """  Bank/Branch Code for company's bank.  """  
      self.CustBankBranchCode:str = obj["CustBankBranchCode"]
      """  Bank/Branch Code for customer's bank.  """  
      self.CustIBANCode:str = obj["CustIBANCode"]
      """  IBAN Code for customer's bank.  """  
      self.ForceDiscount:bool = obj["ForceDiscount"]
      """  When selected, this field will force the best discount percentage, according to the invoice?s terms definition, to be used.  """  
      self.PaymentTotal:int = obj["PaymentTotal"]
      """  Total paid amount in Base  """  
      self.Variance:int = obj["Variance"]
      """  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.IsEnterTotal:bool = obj["IsEnterTotal"]
      """  Enter Totals flag  """  
      self.Rpt1Variance:int = obj["Rpt1Variance"]
      """  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt2Variance:int = obj["Rpt2Variance"]
      """  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt3Variance:int = obj["Rpt3Variance"]
      """  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.DocVariance:int = obj["DocVariance"]
      """  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  """  
      self.DocPaymentTotal:int = obj["DocPaymentTotal"]
      """  Total paid amount in payment currency  """  
      self.PaymentBankRate:int = obj["PaymentBankRate"]
      """  Exchange rate from the payment currency to the Bank currency  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.Rpt1PaymentTotal:int = obj["Rpt1PaymentTotal"]
      """  Total paid amount in Rpt1 currency  """  
      self.Rpt2PaymentTotal:int = obj["Rpt2PaymentTotal"]
      """  Total paid amount in Rpt2 currency  """  
      self.Rpt3PaymentTotal:int = obj["Rpt3PaymentTotal"]
      """  Total paid amount in Rpt3 currency  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the payment instrument for.  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the payment instrument was cleared in the system (System Set).  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the payment instrument (System Set).  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the payment instrument was cleared on.  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.ClearedPI:bool = obj["ClearedPI"]
      """  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.DocClearedAmt:int = obj["DocClearedAmt"]
      """  Amount that the bank cleared the check for.(Vendors Currency)  """  
      self.Rpt1ClearedAmt:int = obj["Rpt1ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClearedAmt:int = obj["Rpt2ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClearedAmt:int = obj["Rpt3ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.FirstHeadNum:int = obj["FirstHeadNum"]
      """  Reference to the first checkhed  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if manually printed.  If manual then user must enter the APPRomNoteID  """  
      self.ChgComment:str = obj["ChgComment"]
      """  Reason to change the Customer or Company information  """  
      self.PymtCntr:bool = obj["PymtCntr"]
      """  Indicates APPRomNoteID was generated using AP CheckHed numbering  """  
      self.PIStage:str = obj["PIStage"]
      """  Payment Instrument Stage  """  
      self.LockRate:bool = obj["LockRate"]
      """  Lock Exchange Rate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankClearedAmt:int = obj["BankClearedAmt"]
      """  BankClearedAmt  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.SupplierCountryNum:int = obj["SupplierCountryNum"]
      """  SupplierCountryNum  """  
      self.EndorsedARPNGroupID:str = obj["EndorsedARPNGroupID"]
      """  Reference to Endorsed AR PI GroupID.  """  
      self.EndorsedARPNHeadNum:int = obj["EndorsedARPNHeadNum"]
      """  Reference to Endorsed AR PI HeadNum.  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.BankAccountEnabled:bool = obj["BankAccountEnabled"]
      """  Enable the Bank Account Search Button  """  
      self.BankCurrCode:str = obj["BankCurrCode"]
      """  Bank Currency Code  """  
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      self.BankFeeAmt:int = obj["BankFeeAmt"]
      self.BankRecGainLoss:int = obj["BankRecGainLoss"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CompanyBankAcct:str = obj["CompanyBankAcct"]
      self.CompanyBankIdentifier:str = obj["CompanyBankIdentifier"]
      self.CompanyBankName:str = obj["CompanyBankName"]
      self.CompanyCountryNum:int = obj["CompanyCountryNum"]
      """  Field to bring the Company Country Name  """  
      self.DisableBankAmt:bool = obj["DisableBankAmt"]
      """   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  """  
      self.DocAllocAmt:int = obj["DocAllocAmt"]
      self.DocBankFeeAmt:int = obj["DocBankFeeAmt"]
      self.DocBankRecGainLoss:int = obj["DocBankRecGainLoss"]
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      self.DocGainLossReal:int = obj["DocGainLossReal"]
      self.DocGainLossUnreal:int = obj["DocGainLossUnreal"]
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.EnterPaymentTotal:bool = obj["EnterPaymentTotal"]
      self.FullyPaid:bool = obj["FullyPaid"]
      self.GainLossReal:int = obj["GainLossReal"]
      self.GainLossUnreal:int = obj["GainLossUnreal"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for miscellaneous shipments  """  
      self.IsFiltered:bool = obj["IsFiltered"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.PaymentAmount:int = obj["PaymentAmount"]
      self.PaymentStatus:str = obj["PaymentStatus"]
      self.RevalDate:str = obj["RevalDate"]
      self.Rpt1AllocAmt:int = obj["Rpt1AllocAmt"]
      self.Rpt1BankFeeAmt:int = obj["Rpt1BankFeeAmt"]
      self.Rpt1BankRecGainLoss:int = obj["Rpt1BankRecGainLoss"]
      self.Rpt1GainLossReal:int = obj["Rpt1GainLossReal"]
      self.Rpt1GainLossUnreal:int = obj["Rpt1GainLossUnreal"]
      self.Rpt2AllocAmt:int = obj["Rpt2AllocAmt"]
      self.Rpt2BankFeeAmt:int = obj["Rpt2BankFeeAmt"]
      self.Rpt2BankRecGainLoss:int = obj["Rpt2BankRecGainLoss"]
      self.Rpt2GainLossReal:int = obj["Rpt2GainLossReal"]
      self.Rpt2GainLossUnreal:int = obj["Rpt2GainLossUnreal"]
      self.Rpt3AllocAmt:int = obj["Rpt3AllocAmt"]
      self.Rpt3BankFeeAmt:int = obj["Rpt3BankFeeAmt"]
      self.Rpt3BankRecGainLoss:int = obj["Rpt3BankRecGainLoss"]
      self.Rpt3GainLossReal:int = obj["Rpt3GainLossReal"]
      self.Rpt3GainLossUnreal:int = obj["Rpt3GainLossUnreal"]
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.StatusChgLegalNum:str = obj["StatusChgLegalNum"]
      self.StatusChgTranDocType:str = obj["StatusChgTranDocType"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      self.TypeDesc:str = obj["TypeDesc"]
      self.VendBankAcct:str = obj["VendBankAcct"]
      self.VendBankIdentifier:str = obj["VendBankIdentifier"]
      self.VendBankName:str = obj["VendBankName"]
      self.VoidDate:str = obj["VoidDate"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.XRateLabelPaymentBank:str = obj["XRateLabelPaymentBank"]
      self.XRateLabelPaymentBase:str = obj["XRateLabelPaymentBase"]
      self.AllocAmt:int = obj["AllocAmt"]
      self.EndorsedARPNStatus:str = obj["EndorsedARPNStatus"]
      """  Endorsed AR PI Status  """  
      self.EndorsedARPNStatusChgTranDocType:str = obj["EndorsedARPNStatusChgTranDocType"]
      """  Endorsed AR PI Status Change Transaction Document Type.  """  
      self.EndorsedARPNStatusChgLegalNum:str = obj["EndorsedARPNStatusChgLegalNum"]
      """  Endorsed AR PI Status Change Legal Number.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BaseCurrSymbolCurrencyID:str = obj["BaseCurrSymbolCurrencyID"]
      self.BaseCurrSymbolCurrSymbol:str = obj["BaseCurrSymbolCurrSymbol"]
      self.BaseCurrSymbolCurrDesc:str = obj["BaseCurrSymbolCurrDesc"]
      self.BaseCurrSymbolDocumentDesc:str = obj["BaseCurrSymbolDocumentDesc"]
      self.BaseCurrSymbolCurrName:str = obj["BaseCurrSymbolCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.PIStatusStatusDesc:str = obj["PIStatusStatusDesc"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APPNHeadTGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.TGLCTranNum:int = obj["TGLCTranNum"]
      """  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  """  
      self.GLAcctContext:str = obj["GLAcctContext"]
      """  String identifier of the account context.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  """  
      self.COACode:str = obj["COACode"]
      """  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  """  
      self.UserCanModify:bool = obj["UserCanModify"]
      """  Indicates if the user can update or delete this record.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  Segement Value 1 of the account for this context.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  Segement Value 2 of the account for this context.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  Segement Value 3 of the account for this context.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  Segement Value 4 of the account for this context.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  Segement Value 5 of the account for this context.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  Segement Value 6 of the account for this context.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  Segement Value 7 of the account for this context.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  Segement Value 8 of the account for this context.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  Segement Value 9 of the account for this context.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  Segement Value 10 of the account for this context.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  Segement Value 11 of the account for this context.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  Segement Value 12 of the account for this context.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  Segement Value 13 of the account for this context.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  Segement Value 14 of the account for this context.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  Segement Value 15 of the account for this context.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  Segement Value 16 of the account for this context.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  Segement Value 17 of the account for this context.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  Segement Value 18 of the account for this context.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  Segement Value 19 of the account for this context.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  Segement Value 20 of the account for this context.  """  
      self.SysGLControlType:str = obj["SysGLControlType"]
      """  Unique Identifier of the system GL Control Type.  """  
      self.SysGLControlCode:str = obj["SysGLControlCode"]
      """  System generated GL Control Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year of the related GLJrnDtl.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode of the related GLJrnDtl.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal number of the related GLJrnDtl.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  JournalLine of the related GLJrnDtl.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction date of the transaction.  This is used in order to display the transactions in date order.  """  
      self.TranSource:str = obj["TranSource"]
      """   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.SysDate:str = obj["SysDate"]
      """  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.SysTime:int = obj["SysTime"]
      """  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.TranNum:int = obj["TranNum"]
      """  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  """  
      self.TransAmt:int = obj["TransAmt"]
      """  Transaction amount that this transaction posted to the related GlJrnDtl.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line Number associated with this GL Journal  """  
      self.SeqNum:int = obj["SeqNum"]
      """  The sequence number associated with this GL journal  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  Credit Amount.  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  Debit Amount.  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  BookCreditAmount  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  Book Debit Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.RecordType:str = obj["RecordType"]
      """   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equals ABTUID which was created during posting  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Technical identifier.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.IsModifiedByUser:bool = obj["IsModifiedByUser"]
      """  IsModifiedByUser  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.MovementType:str = obj["MovementType"]
      """  MovementType  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum of APNHead  """  
      self.IsFiltered:bool = obj["IsFiltered"]
      self.GroupID:str = obj["GroupID"]
      """  GroupID for APPNHead  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APPNMoveRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.Seq:int = obj["Seq"]
      """  Movement Order  """  
      self.CurGroupID:str = obj["CurGroupID"]
      """  Current Group ID  """  
      self.PIStatus:str = obj["PIStatus"]
      """  Status  """  
      self.PIStage:str = obj["PIStage"]
      """  Stage  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date created  """  
      self.CreateUser:str = obj["CreateUser"]
      """  Created By User  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.Type:str = obj["Type"]
      """  Move Type  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction date.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  Creation Time  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      """  Indicates if the legal number is manually generated or system generated  """  
      self.PostErrMess:str = obj["PostErrMess"]
      """  Posting Error Message  """  
      self.PostToGL:bool = obj["PostToGL"]
      """  Indicates if posting GL transactions.  """  
      self.StatusDesc:str = obj["StatusDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APPNMoveTableset:
   def __init__(self, obj):
      self.APPNMove:list[Erp_Tablesets_APPNMoveRow] = obj["APPNMove"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_APPromissoryNotesTableset:
   def __init__(self, obj):
      self.APPNHead:list[Erp_Tablesets_APPNHeadRow] = obj["APPNHead"]
      self.APPNHeadAttch:list[Erp_Tablesets_APPNHeadAttchRow] = obj["APPNHeadAttch"]
      self.APPNDtl:list[Erp_Tablesets_APPNDtlRow] = obj["APPNDtl"]
      self.BankTran:list[Erp_Tablesets_BankTranRow] = obj["BankTran"]
      self.BankTranGLC:list[Erp_Tablesets_BankTranGLCRow] = obj["BankTranGLC"]
      self.APPNHeadTGLC:list[Erp_Tablesets_APPNHeadTGLCRow] = obj["APPNHeadTGLC"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.PITotals:list[Erp_Tablesets_PITotalsRow] = obj["PITotals"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_BankTranGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.TGLCTranNum:int = obj["TGLCTranNum"]
      """  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  """  
      self.GLAcctContext:str = obj["GLAcctContext"]
      """  String identifier of the account context.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  """  
      self.COACode:str = obj["COACode"]
      """  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  """  
      self.UserCanModify:bool = obj["UserCanModify"]
      """  Indicates if the user can update or delete this record.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  Segement Value 1 of the account for this context.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  Segement Value 2 of the account for this context.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  Segement Value 3 of the account for this context.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  Segement Value 4 of the account for this context.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  Segement Value 5 of the account for this context.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  Segement Value 6 of the account for this context.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  Segement Value 7 of the account for this context.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  Segement Value 8 of the account for this context.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  Segement Value 9 of the account for this context.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  Segement Value 10 of the account for this context.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  Segement Value 11 of the account for this context.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  Segement Value 12 of the account for this context.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  Segement Value 13 of the account for this context.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  Segement Value 14 of the account for this context.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  Segement Value 15 of the account for this context.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  Segement Value 16 of the account for this context.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  Segement Value 17 of the account for this context.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  Segement Value 18 of the account for this context.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  Segement Value 19 of the account for this context.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  Segement Value 20 of the account for this context.  """  
      self.SysGLControlType:str = obj["SysGLControlType"]
      """  Unique Identifier of the system GL Control Type.  """  
      self.SysGLControlCode:str = obj["SysGLControlCode"]
      """  System generated GL Control Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year of the related GLJrnDtl.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode of the related GLJrnDtl.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal number of the related GLJrnDtl.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  JournalLine of the related GLJrnDtl.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction date of the transaction.  This is used in order to display the transactions in date order.  """  
      self.TranSource:str = obj["TranSource"]
      """   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.SysDate:str = obj["SysDate"]
      """  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.SysTime:int = obj["SysTime"]
      """  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.TranNum:int = obj["TranNum"]
      """  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  """  
      self.TransAmt:int = obj["TransAmt"]
      """  Transaction amount that this transaction posted to the related GlJrnDtl.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line Number associated with this GL Journal  """  
      self.SeqNum:int = obj["SeqNum"]
      """  The sequence number associated with this GL journal  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  Credit Amount.  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  Debit Amount.  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  BookCreditAmount  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  Book Debit Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.RecordType:str = obj["RecordType"]
      """   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equals ABTUID which was created during posting  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Technical identifier.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.IsModifiedByUser:bool = obj["IsModifiedByUser"]
      """  IsModifiedByUser  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.MovementType:str = obj["MovementType"]
      """  MovementType  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.Voided:bool = obj["Voided"]
      self.BankAcctID:str = obj["BankAcctID"]
      """  Added to fix generation bug only. (for relation LRBankTranBankTranGLC)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BankTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Relates record to a BankAcct.  """  
      self.TranNum:int = obj["TranNum"]
      """  Unique ID of the Transaction.  """  
      self.TranDate:str = obj["TranDate"]
      """  Date that the transaction took place.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Amount of the Transaction  """  
      self.TranRef:str = obj["TranRef"]
      """  Transaction Reference  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates that the Transaction (not cleared variance) has been posted to G/L.  When the Bank Statement is posted all Non-G/L Posted adjustments for the bank are posted to G/L using the Bank Account's Cash and Bank Fee Accounts. G/L Posted Transactions cannot be deleted. (System Set)  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Person who entered the transaction (System Set).  """  
      self.EntryDate:str = obj["EntryDate"]
      """  Date that the Transaction was entered into the system (System Set).  """  
      self.EntryTime:str = obj["EntryTime"]
      """  Time that the transaction was entered into the system - in HH:MM:SS format (System Set).  """  
      self.TranCleared:bool = obj["TranCleared"]
      """  Indicates the transaction's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.TranClearPending:bool = obj["TranClearPending"]
      """  Indicates that the transaction is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.TranClearedAmt:int = obj["TranClearedAmt"]
      """  Amount that the Transaction was cleared for.  """  
      self.TranClearedPerson:str = obj["TranClearedPerson"]
      """  Person who cleared the transaction (System Set).  """  
      self.TranClearedDate:str = obj["TranClearedDate"]
      """  Date that the Transaction was cleared in the system (System Set).  """  
      self.TranClearedTime:str = obj["TranClearedTime"]
      """  Time that the transaction was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.BankSlip:str = obj["BankSlip"]
      """  The identifier of the Bank Slip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year that entry applies to.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period the transaction was posted to. Only pertains to when posted to GL.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal Number of related GLJrnDtl.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code of the related GLJrnDtl.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Document amount of the Transaction  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange rate that is used for this bank transaction.  """  
      self.DocTranClearedAmt:int = obj["DocTranClearedAmt"]
      """  Document amount that the Transaction was cleared for.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "group" that the transaction is assigned to.  All transactions belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post the transactions.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.GLRefType:str = obj["GLRefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.GLRefCode:str = obj["GLRefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.GLRefCodeDesc:str = obj["GLRefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranClearedAmt:int = obj["Rpt1TranClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranClearedAmt:int = obj["Rpt2TranClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranClearedAmt:int = obj["Rpt3TranClearedAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix that entry applies to.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      """  Unique ID of the Fee  """  
      self.BankFeeAmt:int = obj["BankFeeAmt"]
      """  The Fee amount; this amount plus the Fee tax amount will compose the total of the charge on the statement  """  
      self.BankFeeTaxAmt:int = obj["BankFeeTaxAmt"]
      """  The Tax Amount that has been charged to the fee  """  
      self.DocBankFeeAmt:int = obj["DocBankFeeAmt"]
      """  The Fee amount in Base Currency  """  
      self.DocBankFeeTaxAmt:int = obj["DocBankFeeTaxAmt"]
      """  The Tax Amount that has been charged to the fee in Base Currency  """  
      self.Rpt1BankFeeAmt:int = obj["Rpt1BankFeeAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2BankFeeAmt:int = obj["Rpt2BankFeeAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3BankFeeAmt:int = obj["Rpt3BankFeeAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1BankFeeTaxAmt:int = obj["Rpt1BankFeeTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2BankFeeTaxAmt:int = obj["Rpt2BankFeeTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3BankFeeTaxAmt:int = obj["Rpt3BankFeeTaxAmt"]
      """  Reporting currency value of this field  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Used for Bank Fee Functionality, indicates the module that created this BankFee.  This is assigned by the system.
Values can be; AR, AP and BA.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Consecutive from the AP and AR transactions, this field is used to identify the AP or AR transaction that created this Bank Fee  """  
      self.Voided:bool = obj["Voided"]
      """  Indiates if the BankTran has been voided.  The TranNum field will be the same as the original transaction  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.GainLossType:str = obj["GainLossType"]
      """  "R" for realized or "U" for unrealized Gain/Loss  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.ReverseGL:bool = obj["ReverseGL"]
      """  Indicates if it's a reversing Gain/Loss adjustment  """  
      self.RevalueDate:str = obj["RevalueDate"]
      """  Revaluation date that generated the gain/loss record  """  
      self.RevalueBal:int = obj["RevalueBal"]
      """  Bank Balance at the time of revaluation  """  
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      """  Document currency Bank Balance at the time of revaluation  """  
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      """  Reporting currency Bank Balance at the time of revaluation  """  
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      """  Reporting currency Bank Balance at the time of revaluation  """  
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      """  Reporting currency Bank Balance at the time of revaluation  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number for the record.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document for the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CNCFICode:str = obj["CNCFICode"]
      """  CNCFICode  """  
      self.CNToCFICode:str = obj["CNToCFICode"]
      """  CNToCFICode  """  
      self.BankRecGainLoss:int = obj["BankRecGainLoss"]
      """  BankRecGainLoss  """  
      self.Rpt1BankRecGainLoss:int = obj["Rpt1BankRecGainLoss"]
      """  Rpt1BankRecGainLoss  """  
      self.Rpt2BankRecGainLoss:int = obj["Rpt2BankRecGainLoss"]
      """  Rpt2BankRecGainLoss  """  
      self.Rpt3BankRecGainLoss:int = obj["Rpt3BankRecGainLoss"]
      """  Rpt3BankRecGainLoss  """  
      self.BalanceUpdated:int = obj["BalanceUpdated"]
      """  BalanceUpdated  """  
      self.DocBankRecGainLoss:int = obj["DocBankRecGainLoss"]
      """  DocBankRecGainLoss  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.BankBatchExcluded:bool = obj["BankBatchExcluded"]
      """  Indicates that transaction is currently excluded from batch in Bank Statement Processing.  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.ABTUID:str = obj["ABTUID"]
      """  ABTUID  """  
      self.Plant:str = obj["Plant"]
      """  Multi-Site related Site  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.CNCFICodeDescription:str = obj["CNCFICodeDescription"]
      self.CRCurrCode:str = obj["CRCurrCode"]
      """  Cash Receipt currency code  """  
      self.CRRateGrpCode:str = obj["CRRateGrpCode"]
      """  Cash Receipt Rate group code  """  
      self.CRTranAmt:int = obj["CRTranAmt"]
      """  Cash Receipt Tran amount  """  
      self.CRTranClearedAmt:int = obj["CRTranClearedAmt"]
      """  Cash Receipt Transaction Cleared Amount  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currency Switch  """  
      self.DisableBankAmt:bool = obj["DisableBankAmt"]
      """   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  """  
      self.DispAmtReverse:bool = obj["DispAmtReverse"]
      """  The flag to indicate if the Display amount is supposed to be reversed  """  
      self.DispDocTranAmt:int = obj["DispDocTranAmt"]
      self.DispDocTranClearedAmt:int = obj["DispDocTranClearedAmt"]
      self.DispTranAmt:int = obj["DispTranAmt"]
      self.DispTranClearedAmt:int = obj["DispTranClearedAmt"]
      self.InternalDate:str = obj["InternalDate"]
      """  Used for tree structure/parent view definition in Petty Cash Entry  """  
      self.IsFiltered:bool = obj["IsFiltered"]
      self.IsLockedBankRec:bool = obj["IsLockedBankRec"]
      """  Indicates if the record is locked by review journal for bank reconciliation  """  
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      """  Indicates if the legal number is manually generated or system generated  """  
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      """  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  """  
      self.Rpt1DispTranAmt:int = obj["Rpt1DispTranAmt"]
      self.Rpt1DispTranClearedAmt:int = obj["Rpt1DispTranClearedAmt"]
      self.Rpt2DispTranAmt:int = obj["Rpt2DispTranAmt"]
      self.Rpt2DispTranClearedAmt:int = obj["Rpt2DispTranClearedAmt"]
      self.Rpt3DispTranAmt:int = obj["Rpt3DispTranAmt"]
      self.Rpt3DispTranClearedAmt:int = obj["Rpt3DispTranClearedAmt"]
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      self.GLAccount:str = obj["GLAccount"]
      """  Display GL Account  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.BankFeeIDDescription:str = obj["BankFeeIDDescription"]
      self.BankFeeIDTaxCode:str = obj["BankFeeIDTaxCode"]
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  GL Control Identifier.  """  
      self.BusinessEntity:str = obj["BusinessEntity"]
      """  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.GlobalEntityGLC:bool = obj["GlobalEntityGLC"]
      """  Marks this EntityGLC as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the related BankAcct record.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      self.CallCode:str = obj["CallCode"]
      """  CallCode of the related FSCallCd record.  """  
      self.ChargeCode:str = obj["ChargeCode"]
      self.ClassCode:str = obj["ClassCode"]
      """  ClassCode of the related FAClass record.  """  
      self.ClassID:str = obj["ClassID"]
      """  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  """  
      self.ContractCode:str = obj["ContractCode"]
      """  ContractCode of the related FSContCd record.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode of the related Currency record.  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum of the related Customer record  """  
      self.DeductionID:str = obj["DeductionID"]
      """  DeductionID of PRClsDed or PRDeduct.  """  
      self.EmpID:str = obj["EmpID"]
      """  EmpID of the related PREmpMas record.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode of PayTLbr, LabExpCd  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID of ExtCompany table  """  
      self.FromPlant:str = obj["FromPlant"]
      """  FromPlant value of the related PlntTranDef record.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  GroupCode of the related FAGroup record.  """  
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.JCDept:str = obj["JCDept"]
      """  JCDept of the related JCDept record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode of the related MiscChrg or PurMisc record.  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum of the related Part record.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """  PayTypeID of PayType  """  
      self.PerConName:str = obj["PerConName"]
      self.PIStatus:str = obj["PIStatus"]
      """  PI Status  """  
      self.Plant:str = obj["Plant"]
      """  Plant of the related PlantConfCtrl record.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode of the related ProdGrup record.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID of the related Project record.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  PurchCode of the related GLPurch record.  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode of the related GLRate record.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode of the related Reason record.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  ReasonType of the related Reason record.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID of the related SalesCat record.  """  
      self.Shift:int = obj["Shift"]
      """  Shift value of the related JCShift record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode of the related SalesTax record.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  TaxTblID of PRTaxMas or PRClsTax.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  ToPlant value of the related PlntTranDef record.  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  TransferMethod of ExtCompany table  """  
      self.TypeID:str = obj["TypeID"]
      """  Type ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum of the related Vendor record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode of the related Warehse record.  """  
      self.ExpenseTypeCode:str = obj["ExpenseTypeCode"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.OprTypeCode:str = obj["OprTypeCode"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.TIN:str = obj["TIN"]
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLJrnlDtlMovTableset:
   def __init__(self, obj):
      self.GLJrnlDtl:list[Erp_Tablesets_GLJrnlDtlRow] = obj["GLJrnlDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLJrnlDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year that entry applies to.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  """  
      self.Description:str = obj["Description"]
      """  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  """  
      self.JEDate:str = obj["JEDate"]
      """  Date for this journal transaction entry.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period that this journal entry applies to.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  User ID that posted this translation.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Date that this transaction was posted to the G/L files.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this entry has been posted to the G/L master balance files. Unposted entries are excluded from all G/L reports.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctId of the BankAcct master that this check was drawn  against.  """  
      self.CheckNum:int = obj["CheckNum"]
      """  Check number.  """  
      self.CRHeadNum:int = obj["CRHeadNum"]
      """  Cash Receipts reference field.  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  """  
      self.BankTranNum:int = obj["BankTranNum"]
      """  Bank Transaction Number.  Used when a transaction is a direct transfer from one bank account to another.  """  
      self.BankSlip:str = obj["BankSlip"]
      """   The identifier of the Bank Slip document (bank statement).  The user enters a bank slip during the reconciliation process.  This is then written into the related GLJrnDtl records.
Pertains to transactions related to a bank (checks, receipts, transfers, adjustments)  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.ExtRefType:str = obj["ExtRefType"]
      """  Multi-Company G/L Reference Type from the external company.  This is used by the Multi-Company Journal.  """  
      self.ExtRefCode:str = obj["ExtRefCode"]
      """  Multi-Company G/L Reference Code from the external company.  This is used by the Multi-Company Journal.  """  
      self.GlbJournalNum:int = obj["GlbJournalNum"]
      """  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  """  
      self.GlbJournalLine:int = obj["GlbJournalLine"]
      """  The Journal Line assigned at the destination or target company when this Multi-Company Journal is created.  """  
      self.GlbJournalCode:str = obj["GlbJournalCode"]
      """  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor number.  Used by Multi-Company Journal.  """  
      self.GlbAPInvoiceNum:str = obj["GlbAPInvoiceNum"]
      """  Global AP Invoice identifier.  Used by Multi-Company Journal.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Flag to indicate that a separate journal entry will be created at the target company for the Multi-Company G/L Account entered in this journal line.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to a Multi-Company Journal.  """  
      self.CommentText:str = obj["CommentText"]
      """  Extended text to describe the journal line entry.  Defaults from GLJrnHed.CommentText.  """  
      self.GlbCompanyID:str = obj["GlbCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.GlbFiscalYear:int = obj["GlbFiscalYear"]
      """  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  """  
      self.GlbFiscalPeriod:int = obj["GlbFiscalPeriod"]
      """  Fiscal period from the external company that this journal entry applies to.  """  
      self.GlbGroupID:str = obj["GlbGroupID"]
      """  The data entry Group from the external company that the journal entry is assigned to.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.ExtGLAccount:str = obj["ExtGLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.ExtSegValue1:str = obj["ExtSegValue1"]
      """  External Segment Value 1  """  
      self.ExtSegValue2:str = obj["ExtSegValue2"]
      """  External Segment Value 2  """  
      self.ExtSegValue3:str = obj["ExtSegValue3"]
      """  External Segment Value 3  """  
      self.ExtSegValue4:str = obj["ExtSegValue4"]
      """  External Segment Value 4  """  
      self.ExtSegValue5:str = obj["ExtSegValue5"]
      """  External Segment Value 5  """  
      self.ExtSegValue6:str = obj["ExtSegValue6"]
      """  External Segment Value 6  """  
      self.ExtSegValue7:str = obj["ExtSegValue7"]
      """  External Segment Value 7  """  
      self.ExtSegValue8:str = obj["ExtSegValue8"]
      """  External Segment Value 8  """  
      self.ExtSegValue9:str = obj["ExtSegValue9"]
      """  External Segment Value 9  """  
      self.ExtSegValue10:str = obj["ExtSegValue10"]
      """  External Segment Value 10  """  
      self.ExtSegValue11:str = obj["ExtSegValue11"]
      """  External Segment Value 11  """  
      self.ExtSegValue12:str = obj["ExtSegValue12"]
      """  External Segment Value 12  """  
      self.ExtSegValue13:str = obj["ExtSegValue13"]
      """  External Segment Value 13  """  
      self.ExtSegValue14:str = obj["ExtSegValue14"]
      """  External Segment Value 14  """  
      self.ExtSegValue15:str = obj["ExtSegValue15"]
      """  External Segment Value 15  """  
      self.ExtSegValue16:str = obj["ExtSegValue16"]
      """  External Segment Value 16  """  
      self.ExtSegValue17:str = obj["ExtSegValue17"]
      """  External Segment Value 17  """  
      self.ExtSegValue18:str = obj["ExtSegValue18"]
      """  External Segment Value 18  """  
      self.ExtSegValue19:str = obj["ExtSegValue19"]
      """  External Segment Value 19  """  
      self.ExtSegValue20:str = obj["ExtSegValue20"]
      """  External Segment Value 20  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number of source document  """  
      self.PerBalFlag:bool = obj["PerBalFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.TBFlag:bool = obj["TBFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.DailyBalFlag:bool = obj["DailyBalFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.GlbFiscalYearSuffix:str = obj["GlbFiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.GlbFiscalCalendarID:str = obj["GlbFiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.IntermediateProc:bool = obj["IntermediateProc"]
      """  Identifies the journal entry as one processed by consolidation posting mode where the data transfer is immediate and an intermediate book is used.  """  
      self.GenID:int = obj["GenID"]
      """  Internal system calculated sequence number not inteneded for external use.  """  
      self.SrcCompany:str = obj["SrcCompany"]
      """  Source Company Identifier.  Identifies the company where this GLJrnDtl originated from.  """  
      self.SrcBook:str = obj["SrcBook"]
      """  Unique Book Identifier  This is the book that is being consolidated into a target book.  """  
      self.SrcGLAccount:str = obj["SrcGLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.SrcJrnlCode:str = obj["SrcJrnlCode"]
      """  Source Journal Code  """  
      self.SrcJournalNum:int = obj["SrcJournalNum"]
      """  Source Journal Number  """  
      self.SrcJournalLine:int = obj["SrcJournalLine"]
      """  Source Journal Line  """  
      self.SrcType:str = obj["SrcType"]
      """   P = derived from Periodic Consolidation.
C = derived from GLJrnDtl via Continuous Consolidation.
A = derived from Advanced Allocations.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equas ABTUID which was created during posting  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  This field shows Debit value of transaction  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  This field shows Credit value of transaction  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  This field shows Debit value of transaction recalculated from DebitAmount according to Currency of mentioned Book  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  This field shows Credit value of transaction recalculated from CreditAmount according to Currency of mentioned Book  """  
      self.ParentRUID:str = obj["ParentRUID"]
      """  If the current line is reversal, then this field is used for link with original journal line. It equals SysRowID of original line.  """  
      self.HasReverseLine:bool = obj["HasReverseLine"]
      """  if has reverse line  """  
      self.BalanceAcct:str = obj["BalanceAcct"]
      """  This is the resolved balance account the period balance, currency balance and/or daily balance records were written under for this GL Journal Detail GL Account.  """  
      self.TrialAcct:str = obj["TrialAcct"]
      """  This is the resolved balance account the trial balance records were written under for this GL Journal Detail GL Account.  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.AllocationStamp:str = obj["AllocationStamp"]
      """  This is the last allocation stamp that affected this GLJrnDtl.  """  
      self.BatchID:str = obj["BatchID"]
      """  Identifies the allocation batch this journal entry was processed under.  """  
      self.AllocID:str = obj["AllocID"]
      """  This is the allocation id that processed this journal entry.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  The allocation run number is a unique sequential number that identifies which run of an allocation batch this journal entry was created under.  """  
      self.AllocRunNbr:int = obj["AllocRunNbr"]
      """  Intended for internal use only.  Updated by the Advanced Allocations Engine.  This identifies the last allocation run number that used this GLJrnDtl as a source record.  """  
      self.AllocTgtNbr:int = obj["AllocTgtNbr"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.AllocTgtSeq:int = obj["AllocTgtSeq"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.ExtCOACode:str = obj["ExtCOACode"]
      """  External COA Code  """  
      self.MatchCode:str = obj["MatchCode"]
      """  MatchCode is used to match two or more journal detail records together.  """  
      self.MatchDate:str = obj["MatchDate"]
      """  MatchDate is set when the journal detail record is matched to other journal detail records.  """  
      self.Reconciled:bool = obj["Reconciled"]
      """  Indicates whether or not the transaction has been flagged as reconciled.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Sequence:int = obj["Sequence"]
      """  Journal Sequence Number  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.CustNum:int = obj["CustNum"]
      """  The Internal CustNum that ties back to the Customer master file.  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  CloseFiscalPeriod  """  
      self.SourcePlant:str = obj["SourcePlant"]
      """  SourcePlant  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.ExtSysType:str = obj["ExtSysType"]
      """  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  """  
      self.ExtSysURL:str = obj["ExtSysURL"]
      """  URL for drill back to an integrated external system  """  
      self.StatAmount:int = obj["StatAmount"]
      self.BookCurrencyCode:str = obj["BookCurrencyCode"]
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.ExtRefCodeRefCodeDesc:str = obj["ExtRefCodeRefCodeDesc"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLRefCodeDescRefCodeDesc:str = obj["GLRefCodeDescRefCodeDesc"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.SrcGLAccountGLShortAcct:str = obj["SrcGLAccountGLShortAcct"]
      self.SrcGLAccountGLAcctDisp:str = obj["SrcGLAccountGLAcctDisp"]
      self.SrcGLAccountAccountDesc:str = obj["SrcGLAccountAccountDesc"]
      self.StatUOMStatUOMDesc:str = obj["StatUOMStatUOMDesc"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
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

class Erp_Tablesets_LegalNumGenOptsTableset:
   def __init__(self, obj):
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PITotalsRow:
   def __init__(self, obj):
      self.CashRcv:int = obj["CashRcv"]
      self.DocCashRcv:int = obj["DocCashRcv"]
      self.DocDscTaken:int = obj["DocDscTaken"]
      self.DocGainReal:int = obj["DocGainReal"]
      self.DocGainUnreal:int = obj["DocGainUnreal"]
      self.DscTaken:int = obj["DscTaken"]
      self.GainReal:int = obj["GainReal"]
      self.GainUnreal:int = obj["GainUnreal"]
      self.RevalDate:str = obj["RevalDate"]
      self.Rpt1CashRcv:int = obj["Rpt1CashRcv"]
      self.Rpt1DscTaken:int = obj["Rpt1DscTaken"]
      self.Rpt1GainReal:int = obj["Rpt1GainReal"]
      self.Rpt1GainUnreal:int = obj["Rpt1GainUnreal"]
      self.Rpt2CashRcv:int = obj["Rpt2CashRcv"]
      self.Rpt2DscTaken:int = obj["Rpt2DscTaken"]
      self.Rpt2GainReal:int = obj["Rpt2GainReal"]
      self.Rpt2GainUnreal:int = obj["Rpt2GainUnreal"]
      self.Rpt3CashRcv:int = obj["Rpt3CashRcv"]
      self.Rpt3DscTaken:int = obj["Rpt3DscTaken"]
      self.Rpt3GainReal:int = obj["Rpt3GainReal"]
      self.Rpt3GainUnreal:int = obj["Rpt3GainUnreal"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtAPPromissoryNotesTableset:
   def __init__(self, obj):
      self.APPNHead:list[Erp_Tablesets_APPNHeadRow] = obj["APPNHead"]
      self.APPNHeadAttch:list[Erp_Tablesets_APPNHeadAttchRow] = obj["APPNHeadAttch"]
      self.APPNDtl:list[Erp_Tablesets_APPNDtlRow] = obj["APPNDtl"]
      self.BankTran:list[Erp_Tablesets_BankTranRow] = obj["BankTran"]
      self.BankTranGLC:list[Erp_Tablesets_BankTranGLCRow] = obj["BankTranGLC"]
      self.APPNHeadTGLC:list[Erp_Tablesets_APPNHeadTGLCRow] = obj["APPNHeadTGLC"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.PITotals:list[Erp_Tablesets_PITotalsRow] = obj["PITotals"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GenerateAPPNDtl_input:
   """ Required : 
   groupID
   headNum
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Cash Group ID  """  
      self.headNum:int = obj["headNum"]
      """  Promissory Note HeadNum  """  
      pass

class GenerateAPPNDtl_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["returnObj"]
      pass

class GetAPPNMove_input:
   """ Required : 
   iGroupID
   iHeadNum
   """  
   def __init__(self, obj):
      self.iGroupID:str = obj["iGroupID"]
      """  The Group Number  """  
      self.iHeadNum:int = obj["iHeadNum"]
      """  The Header Number  """  
      pass

class GetAPPNMove_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APPNMoveTableset] = obj["returnObj"]
      pass

class GetAvailTranDocTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.listAvailTranDocTypes:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetBankAcctInfo_input:
   """ Required : 
   bankAcctID
   ds
   """  
   def __init__(self, obj):
      self.bankAcctID:str = obj["bankAcctID"]
      """  Proposed BankAcctID  """  
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

class GetBankAcctInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetBankFeeDefaultAccount_input:
   """ Required : 
   bankAcctID
   tranNum
   voided
   ds
   """  
   def __init__(self, obj):
      self.bankAcctID:str = obj["bankAcctID"]
      """  The Bank Account ID  """  
      self.tranNum:int = obj["tranNum"]
      """  The Bank Fee Tran Num  """  
      self.voided:bool = obj["voided"]
      """  voided  """  
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

class GetBankFeeDefaultAccount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   groupID
   headNum
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["returnObj"]
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

class GetData4ARPITracker_input:
   """ Required : 
   ipGroupID
   ipHeadNum
   ds
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  Group ID  """  
      self.ipHeadNum:int = obj["ipHeadNum"]
      """  Head Num  """  
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

class GetData4ARPITracker_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDefaultMoveTranDocType_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Default TranDocType  """  
      pass

class GetEndorsedARPILegalNumGenOpts_input:
   """ Required : 
   ipGroupID
   ipHeadNum
   tranDocTypeId
   ipGenOnSave
   ipStatusChange
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  AP Payment Instrument Group ID  """  
      self.ipHeadNum:int = obj["ipHeadNum"]
      """  AP Payment Instrument Head Number  """  
      self.tranDocTypeId:str = obj["tranDocTypeId"]
      """  Transaction document type ID  """  
      self.ipGenOnSave:bool = obj["ipGenOnSave"]
      """  Generate Legal Number on Save  """  
      self.ipStatusChange:bool = obj["ipStatusChange"]
      """  Call from AP Status Change  """  
      pass

class GetEndorsedARPILegalNumGenOpts_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LegalNumGenOptsTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opPromptForNum:bool = obj["opPromptForNum"]
      pass

      """  output parameters  """  

class GetGLJrnDtl_input:
   """ Required : 
   iGroupID
   iHeadNum
   """  
   def __init__(self, obj):
      self.iGroupID:str = obj["iGroupID"]
      """  The Group Number  """  
      self.iHeadNum:int = obj["iHeadNum"]
      """  The Header Number  """  
      pass

class GetGLJrnDtl_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLJrnlDtlMovTableset] = obj["returnObj"]
      pass

class GetGroupIDForPI_input:
   """ Required : 
   apPromNoteID
   """  
   def __init__(self, obj):
      self.apPromNoteID:str = obj["apPromNoteID"]
      """  AR Promissory Note ID  """  
      pass

class GetGroupIDForPI_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.groupID:str = obj["parameters"]
      self.headNum:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetGroupIDForPNI_input:
   """ Required : 
   apPromNoteID
   """  
   def __init__(self, obj):
      self.apPromNoteID:str = obj["apPromNoteID"]
      pass

class GetGroupIDForPNI_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["returnObj"]
      pass

class GetLegalNumGenOpts_input:
   """ Required : 
   ipGroupID
   ipHeadNum
   tranDocTypeId
   ipStatusChange
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  Group ID number  """  
      self.ipHeadNum:int = obj["ipHeadNum"]
      """  Header number  """  
      self.tranDocTypeId:str = obj["tranDocTypeId"]
      """  Transaction document type Id  """  
      self.ipStatusChange:bool = obj["ipStatusChange"]
      """  Status Change  """  
      pass

class GetLegalNumGenOpts_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LegalNumGenOptsTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opPromptForNum:bool = obj["opPromptForNum"]
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
      self.returnObj:list[Erp_Tablesets_APPNHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewAPPNDtl_input:
   """ Required : 
   ds
   groupID
   headNum
   invoiceNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      self.invoiceNum:str = obj["invoiceNum"]
      pass

class GetNewAPPNDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAPPNHeadAttch_input:
   """ Required : 
   ds
   groupID
   headNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      pass

class GetNewAPPNHeadAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAPPNHeadByGroupID_input:
   """ Required : 
   pcGroupID
   APPromissoryNotesTableset
   """  
   def __init__(self, obj):
      self.pcGroupID:str = obj["pcGroupID"]
      self.APPromissoryNotesTableset:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["APPromissoryNotesTableset"]
      pass

class GetNewAPPNHeadByGroupID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.APPromissoryNotesTableset:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["APPromissoryNotesTableset"]
      pass

      """  output parameters  """  

class GetNewAPPNHeadTGLC_input:
   """ Required : 
   ds
   groupID
   headNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      pass

class GetNewAPPNHeadTGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAPPNHead_input:
   """ Required : 
   ds
   groupID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      pass

class GetNewAPPNHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAPPNMoveByAPPNHead_input:
   """ Required : 
   ipGroupID
   ipHeadNum
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      self.ipHeadNum:int = obj["ipHeadNum"]
      pass

class GetNewAPPNMoveByAPPNHead_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APPNMoveTableset] = obj["returnObj"]
      pass

class GetNewBankTranByHeadNum_input:
   """ Required : 
   lvHeadNum
   lvBankAcctID
   APPromissoryNotesTableset
   """  
   def __init__(self, obj):
      self.lvHeadNum:int = obj["lvHeadNum"]
      self.lvBankAcctID:str = obj["lvBankAcctID"]
      self.APPromissoryNotesTableset:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["APPromissoryNotesTableset"]
      pass

class GetNewBankTranByHeadNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.APPromissoryNotesTableset:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["APPromissoryNotesTableset"]
      pass

      """  output parameters  """  

class GetNewBankTranGLC_input:
   """ Required : 
   ds
   bankAcctID
   tranNum
   voided
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      self.bankAcctID:str = obj["bankAcctID"]
      self.tranNum:int = obj["tranNum"]
      self.voided:bool = obj["voided"]
      pass

class GetNewBankTranGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBankTran_input:
   """ Required : 
   ds
   bankAcctID
   tranNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      self.bankAcctID:str = obj["bankAcctID"]
      self.tranNum:int = obj["tranNum"]
      pass

class GetNewBankTran_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEntityGLC_input:
   """ Required : 
   ds
   relatedToFile
   key1
   key2
   key3
   key4
   key5
   key6
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.key6:str = obj["key6"]
      pass

class GetNewEntityGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPostCodeByPIStatus_input:
   """ Required : 
   ipPIStatus
   """  
   def __init__(self, obj):
      self.ipPIStatus:str = obj["ipPIStatus"]
      """  ipPIStatus  """  
      pass

class GetPostCodeByPIStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPostCode:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRestartAPPNPrinting_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  GroupID  """  
      pass

class GetRestartAPPNPrinting_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.restartAPPNPrinting:bool = obj["restartAPPNPrinting"]
      pass

      """  output parameters  """  

class GetRowsTracker_input:
   """ Required : 
   whereClauseAPPNHead
   whereClauseAPPNHeadAttch
   whereClauseAPPNDtl
   whereClauseBankTran
   whereClauseBankTranGLC
   whereClauseAPPNHeadTGLC
   whereClauseEntityGLC
   whereClauseLegalNumGenOpts
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseAPPNHead:str = obj["whereClauseAPPNHead"]
      self.whereClauseAPPNHeadAttch:str = obj["whereClauseAPPNHeadAttch"]
      self.whereClauseAPPNDtl:str = obj["whereClauseAPPNDtl"]
      self.whereClauseBankTran:str = obj["whereClauseBankTran"]
      self.whereClauseBankTranGLC:str = obj["whereClauseBankTranGLC"]
      self.whereClauseAPPNHeadTGLC:str = obj["whereClauseAPPNHeadTGLC"]
      self.whereClauseEntityGLC:str = obj["whereClauseEntityGLC"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseAPPNHead
   whereClauseAPPNHeadAttch
   whereClauseAPPNDtl
   whereClauseBankTran
   whereClauseBankTranGLC
   whereClauseAPPNHeadTGLC
   whereClauseEntityGLC
   whereClauseLegalNumGenOpts
   whereClausePITotals
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseAPPNHead:str = obj["whereClauseAPPNHead"]
      self.whereClauseAPPNHeadAttch:str = obj["whereClauseAPPNHeadAttch"]
      self.whereClauseAPPNDtl:str = obj["whereClauseAPPNDtl"]
      self.whereClauseBankTran:str = obj["whereClauseBankTran"]
      self.whereClauseBankTranGLC:str = obj["whereClauseBankTranGLC"]
      self.whereClauseAPPNHeadTGLC:str = obj["whereClauseAPPNHeadTGLC"]
      self.whereClauseEntityGLC:str = obj["whereClauseEntityGLC"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.whereClausePITotals:str = obj["whereClausePITotals"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
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

class MassDelete_input:
   """ Required : 
   pcGroupID
   """  
   def __init__(self, obj):
      self.pcGroupID:str = obj["pcGroupID"]
      """  AP Promissory Note Group ID  """  
      pass

class MassDelete_output:
   def __init__(self, obj):
      pass

class NeedsLegalNumber_input:
   """ Required : 
   tranDocType
   """  
   def __init__(self, obj):
      self.tranDocType:str = obj["tranDocType"]
      pass

class NeedsLegalNumber_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class OnChangeBankFeeID_input:
   """ Required : 
   pcBankFeeID
   ds
   """  
   def __init__(self, obj):
      self.pcBankFeeID:str = obj["pcBankFeeID"]
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

class OnChangeBankFeeID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDocTranAmt_input:
   """ Required : 
   pdDocTranAmt
   ds
   """  
   def __init__(self, obj):
      self.pdDocTranAmt:int = obj["pdDocTranAmt"]
      """  Proposed Document Amount value  """  
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

class OnChangeDocTranAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeInvSelPayment_input:
   """ Required : 
   pdDocGrossPay
   pcRowIdent
   ds
   """  
   def __init__(self, obj):
      self.pdDocGrossPay:int = obj["pdDocGrossPay"]
      """  Proposeed Document Gross Payment value  """  
      self.pcRowIdent:str = obj["pcRowIdent"]
      """  Pass ttAPInvSel.RowIdent value here to uniquely identify the record to change.  """  
      self.ds:list[Erp_Tablesets_APInvSelTableset] = obj["ds"]
      pass

class OnChangeInvSelPayment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APInvSelTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeInvoiceNum_input:
   """ Required : 
   pcInvoiceNum
   pcChangeExchangeRateResponse
   ds
   """  
   def __init__(self, obj):
      self.pcInvoiceNum:str = obj["pcInvoiceNum"]
      """  Invoice Num  """  
      self.pcChangeExchangeRateResponse:str = obj["pcChangeExchangeRateResponse"]
      """  Response to the question pcChangeExchangeRateResponse. ? means question has not been asked.  Yes/No is considered a response.  """  
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

class OnChangeInvoiceNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      self.pcQuestion:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeTransDate_input:
   """ Required : 
   pdtTransDate
   ds
   """  
   def __init__(self, obj):
      self.pdtTransDate:str = obj["pdtTransDate"]
      """  Propopsed TransDate  """  
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

class OnChangeTransDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeType_input:
   """ Required : 
   pcType
   ds
   """  
   def __init__(self, obj):
      self.pcType:str = obj["pcType"]
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

class OnChangeType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeVendBankAcctID_input:
   """ Required : 
   pcVendBankAcctID
   ds
   """  
   def __init__(self, obj):
      self.pcVendBankAcctID:str = obj["pcVendBankAcctID"]
      """  Vendor Bank Acct ID - Bank Account ID for Vendor  """  
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

class OnChangeVendBankAcctID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeVendor_input:
   """ Required : 
   pcVendorID
   ds
   """  
   def __init__(self, obj):
      self.pcVendorID:str = obj["pcVendorID"]
      """  Vendor ID - character code for Vendor  """  
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

class OnChangeVendor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PrePost_input:
   """ Required : 
   inGroupID
   inHeadNum
   inPIStatusNew
   inTypeNew
   statusChgTranDocType
   appnDs
   ds
   """  
   def __init__(self, obj):
      self.inGroupID:str = obj["inGroupID"]
      """  Group ID number  """  
      self.inHeadNum:int = obj["inHeadNum"]
      """  Header number  """  
      self.inPIStatusNew:str = obj["inPIStatusNew"]
      """  new value of PIStatus  """  
      self.inTypeNew:str = obj["inTypeNew"]
      """  new value of Type  """  
      self.statusChgTranDocType:str = obj["statusChgTranDocType"]
      self.appnDs:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["appnDs"]
      self.ds:list[Erp_Tablesets_LegalNumGenOptsTableset] = obj["ds"]
      pass

class PrePost_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.outPostToGL:str = obj["parameters"]
      self.appnDs:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["appnDs"]
      self.ds:list[Erp_Tablesets_LegalNumGenOptsTableset] = obj["ds"]
      self.opLegalNumMsg:str = obj["parameters"]
      self.seqNum:int = obj["parameters"]
      pass

      """  output parameters  """  

class PreUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

class PreUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      self.requiresUserInput:bool = obj["requiresUserInput"]
      pass

      """  output parameters  """  

class SelectInvoiceToApplyToGroup_input:
   """ Required : 
   ipGroupID
   ipPayableAccountsList
   ipSupplierNum
   ipDueDate
   ipInvoicePM
   ipPaymentMethod
   ipIncludePartialPosted
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  AP Check Group ID  """  
      self.ipPayableAccountsList:str = obj["ipPayableAccountsList"]
      """  Delimited list of Payable Accounts  """  
      self.ipSupplierNum:int = obj["ipSupplierNum"]
      """  Select invoices for the supplier.  """  
      self.ipDueDate:str = obj["ipDueDate"]
      """  Select invoices due by this date.  """  
      self.ipInvoicePM:bool = obj["ipInvoicePM"]
      """  Select invoices without Payment Method.  """  
      self.ipPaymentMethod:str = obj["ipPaymentMethod"]
      """  Select payment methods for the specific.  """  
      self.ipIncludePartialPosted:bool = obj["ipIncludePartialPosted"]
      """  Select invoices including partially posted.  """  
      pass

class SelectInvoiceToApplyToGroup_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APInvSelTableset] = obj["returnObj"]
      pass

class SelectInvoices_input:
   """ Required : 
   pcGroupID
   pcPayableAccountsList
   pdtDueDate
   pdtInvoicePM
   pcSupplierList
   pcPaymentMethod
   """  
   def __init__(self, obj):
      self.pcGroupID:str = obj["pcGroupID"]
      """  AP Check Group ID  """  
      self.pcPayableAccountsList:str = obj["pcPayableAccountsList"]
      """  Delimited list of Payable Accounts  """  
      self.pdtDueDate:str = obj["pdtDueDate"]
      """  Select invoices due by this date.  """  
      self.pdtInvoicePM:bool = obj["pdtInvoicePM"]
      """  Select invoices without Payment Method.  """  
      self.pcSupplierList:str = obj["pcSupplierList"]
      """  Select invoices for the supplier list.  """  
      self.pcPaymentMethod:str = obj["pcPaymentMethod"]
      """  Select payment methods for the specific.  """  
      pass

class SelectInvoices_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APInvSelTableset] = obj["returnObj"]
      pass

class UpdateAPPNMove4WriteOff_input:
   """ Required : 
   ipGroupID
   ipHeadNum
   ds
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      self.ipHeadNum:int = obj["ipHeadNum"]
      self.ds:list[Erp_Tablesets_APPNMoveTableset] = obj["ds"]
      pass

class UpdateAPPNMove4WriteOff_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPNMoveTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateDueDateDescription_input:
   """ Required : 
   inGroupID
   inHeadNum
   inDueDateNew
   inDescriptionNew
   """  
   def __init__(self, obj):
      self.inGroupID:str = obj["inGroupID"]
      self.inHeadNum:int = obj["inHeadNum"]
      self.inDueDateNew:str = obj["inDueDateNew"]
      self.inDescriptionNew:str = obj["inDescriptionNew"]
      pass

class UpdateDueDateDescription_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAPPromissoryNotesTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAPPromissoryNotesTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidatePIBeforePrint_input:
   """ Required : 
   group
   """  
   def __init__(self, obj):
      self.group:str = obj["group"]
      """  Group ID to validate  """  
      pass

class ValidatePIBeforePrint_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ValidatePaymentInstruments_input:
   """ Required : 
   group
   """  
   def __init__(self, obj):
      self.group:str = obj["group"]
      """  Group ID to validate  """  
      pass

class ValidatePaymentInstruments_output:
   def __init__(self, obj):
      pass

class ValidateRequiredFields_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["ds"]
      pass

class ValidateRequiredFields_output:
   def __init__(self, obj):
      pass

class ValidateStatusAndType_input:
   """ Required : 
   groupId
   headNum
   newStatus
   newType
   """  
   def __init__(self, obj):
      self.groupId:str = obj["groupId"]
      """  Group ID  """  
      self.headNum:int = obj["headNum"]
      """  HeadNum  """  
      self.newStatus:str = obj["newStatus"]
      """  Status  """  
      self.newType:str = obj["newType"]
      """  Type  """  
      pass

class ValidateStatusAndType_output:
   def __init__(self, obj):
      pass

class ValidateUnpostedMovement_input:
   """ Required : 
   groupId
   headNum
   """  
   def __init__(self, obj):
      self.groupId:str = obj["groupId"]
      """  Group ID  """  
      self.headNum:int = obj["headNum"]
      """  HeadNum  """  
      pass

class ValidateUnpostedMovement_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.unpostedSeqNum:int = obj["parameters"]
      self.unpostedStatus:str = obj["parameters"]
      self.unpostedType:str = obj["parameters"]
      self.userMessage:str = obj["parameters"]
      self.postToGL:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateWithholdingExists_input:
   """ Required : 
   company
   vendorNum
   invoiceNum
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.vendorNum:int = obj["vendorNum"]
      self.invoiceNum:str = obj["invoiceNum"]
      pass

class ValidateWithholdingExists_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.exists:bool = obj["exists"]
      pass

      """  output parameters  """  

class VoidAPPNMoveLegalNumber_input:
   """ Required : 
   groupId
   headNum
   seqNum
   reason
   endorsedReason
   """  
   def __init__(self, obj):
      self.groupId:str = obj["groupId"]
      """  Group ID  """  
      self.headNum:int = obj["headNum"]
      """  HeadNum  """  
      self.seqNum:int = obj["seqNum"]
      """  Seq  """  
      self.reason:str = obj["reason"]
      """  void reason  """  
      self.endorsedReason:str = obj["endorsedReason"]
      """  void reason for endorsed movement legal number  """  
      pass

class VoidAPPNMoveLegalNumber_output:
   def __init__(self, obj):
      pass

class VoidLegalNumber_input:
   """ Required : 
   ipGroupID
   ipHeadNum
   ipVoidedReason
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  Group ID number  """  
      self.ipHeadNum:int = obj["ipHeadNum"]
      """  Header number  """  
      self.ipVoidedReason:str = obj["ipVoidedReason"]
      """  Reason for the void  """  
      pass

class VoidLegalNumber_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APPromissoryNotesTableset] = obj["returnObj"]
      pass

class selectFilterPIPayMethod_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

